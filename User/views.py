import json
from urllib.parse import urlparse

from urlextract import URLExtract
import praw
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Utils.reddit_instance import reddit_instance
from User.models import Auth, Post, Author, Domain, Subreddit
from concurrent.futures import ThreadPoolExecutor


@csrf_exempt
def store_token(refresh_token, user):
    token = Auth(refresh_token=refresh_token, user=user)
    token.save()


def get_pushshiftdata(sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?size=1000&subreddit=' + str(sub)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


def auth_view(request, *args, **kwargs):
    if request.method == 'GET':
        state = request.GET.get('state')
        code = request.GET.get('code')
        reddit = reddit_instance(request)
        store_token(reddit.auth.authorize(code), request.user)
        return redirect('/subreddit')


def data_fetch(request):
    reddit = reddit_instance(request)
    subreddits = reddit.user.subreddits(limit=None)
    posts = []
    temp = []
    for item in subreddits:
        usr = Subreddit(name=item.display_name, user=request.user)
        usr.save()
        posts = get_pushshiftdata(item.display_name)
        for thing in posts:
            if 'selftext' in thing:
                if Author.objects.filter(name=thing['author']).exists():
                    z = Author.objects.get(name=thing['author'])
                    i = Post(user=request.user,
                             post_id=thing['id'],
                             post_subreddit=thing['subreddit'],
                             post_text=thing['selftext'],
                             post_author=z,
                             post_title=thing['title'])
                else:
                    authr = Author.create(thing['author'])
                    authr.save()
                    i = Post(user=request.user,
                             post_id=thing['id'],
                             post_subreddit=thing['subreddit'],
                             post_text=thing['selftext'],
                             post_author=authr,
                             post_title=thing['title'])

                temp.append(i)

    Post.objects.bulk_create(temp)


def subreddit_view(request, *args, **kwargs):
    if request.method == 'GET':
        data_fetch(request)
        return redirect("/profile")


def profile_view(request, *args, **kwargs):
    if request.method == 'GET':
        reddit = reddit_instance(request)
        link_post(request)
        domain_add(request)
        data = {
            "response": reddit.user.me()
        }
        return render(request, './components/profile.html', {
            "response": reddit.user.me()
        })


def link_post(request):
    user_post = Post.objects.filter(user=request.user.id)
    extractor = URLExtract()
    for post in user_post:
        urls = extractor.find_urls(post.post_text)
        if urls:
            post.link_contain = True

    Post.objects.bulk_update(user_post, ['link_contain'])


def extract_domain(url, remove_http=True):
    uri = urlparse(url)
    if remove_http:
        domain_name = f"{uri.netloc}"
    else:
        domain_name = f"{uri.netloc}://{uri.netloc}"
    return domain_name


def domain_add(request):
    posts_with_link = Post.objects.filter(user=request.user.id, link_contain=True)
    extractor = URLExtract()
    for post in posts_with_link:
        urls = extractor.find_urls(post.post_text + post.post_title)
        for url in urls:
            url_n = extract_domain(url)
            if not Domain.objects.filter(name=url_n, user=request.user.id).exists():
                new_domain = Domain(name=url_n, user=request.user)
                new_domain.save()
            domain = Domain.objects.get(name=url_n, user=request.user.id)
            domain.post.add(post)


def get_subreddit_view(request, *args, **kwargs):
    if request.method == 'GET':
        reddit = reddit_instance(request)
        subreddits = reddit.user.subreddits(limit=None)

        subredds_list = [{"subreddit": x.display_name, "subs": x.subscribers}
                         for x in subreddits]
        return render(request, './components/subreddit.html', {
            "response": subredds_list
        })


def get_post_with_link_view(request, subreddit_name, *args, **kwargs):
    if request.method == 'GET':
        posts_with_link = Post.objects.filter(user=request.user.id, link_contain=True, post_subreddit=subreddit_name)

        post_list = [
            {"title": x.post_title, "text": x.post_text, "author": x.post_author.name, "subreddit": x.post_subreddit}
            for x in posts_with_link]
        count_domain = most_shared_link(request, subreddit_name)
        count_author = author_with_most_link(request, subreddit_name, posts_with_link)
        data = {
            "response": post_list,
            "link_count": count_domain,
            "author_count": count_author
        }

        # return JsonResponse(data)
        return render(request, './components/getsubreddit.html', {
            "response": post_list,
            "link_count": count_domain,
            "author_count": count_author
        })


def most_shared_link(request,subreddit_name):
    domains = Domain.objects.filter(user=request.user.id)
    count_contain = [{"domain": x.name, "count": Post.objects.filter(domain=x,post_subreddit=subreddit_name).count()} for x in domains]
    return count_contain


def author_with_most_link(request, subreddit_name, posts):
    authors = Author.objects.all()
    count_contain = [{"author": x.name, "count": validate_user(x.id, posts)} for x in authors]
    f_count = []
    for e in count_contain:
        if e['count'] != 0:
            f_count.append({"author": e['author'], "count": e['count']})

    return f_count


def validate_user(x, posts):
    count = 0
    for post in posts:

        if x == post.post_author.id:
            count = count + 1

    return count
