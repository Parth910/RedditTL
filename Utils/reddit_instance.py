import praw
from User.models import Auth


def reddit_instance(request):
    if Auth.objects.filter(user=request.user.id).exists():
        t = Auth.objects.get(user=request.user.id)
        reddit = praw.Reddit(client_id="3FjsoKD81_ybSQ",
                             client_secret="PuFL1pa58PQECbgj2lqzTTOsBRw",
                             redirect_uri="http://localhost:8000/auth",
                             user_agent="redditTop",
                             refresh_token=t.refresh_token

                             )

    else:
        reddit = praw.Reddit(client_id="3FjsoKD81_ybSQ",
                             client_secret="PuFL1pa58PQECbgj2lqzTTOsBRw",
                             redirect_uri="http://localhost:8000/auth",
                             user_agent="redditTop",

                             )

    return reddit
