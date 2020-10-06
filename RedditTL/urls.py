"""RedditTL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from Home.views import reddit_login_view, home_view, get_token_view, delink_reddit
from User.views import auth_view, subreddit_view, get_subreddit_view, get_post_with_link_view, profile_view, data_fetch
from Accouts.views import login_view, logout_view, registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('gettoken/', get_token_view),
    path('redditlink/', reddit_login_view),
    path('delinkreddit/', delink_reddit),
    path('auth/', auth_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', registration_view),
    path('subreddit/', subreddit_view),
    path('login/', login_view),
    path('getsubreddit/', get_subreddit_view),
    path('getsubreddit/<str:subreddit_name>', get_post_with_link_view),
    path('profile/', profile_view),
    path('test/', data_fetch),

]
