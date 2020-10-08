# Reddit Top Link Webapp
---------------------------------------
### Problem Statement
For user auth with reddit account and fetch all submissions from each subreddit user have joined, and give following details:

a. Actual posts containing links

b. Which user has shared the most links

c. List of Top Domains that have been shared so far


### Technology Stack
##### Django Application
This app uses a number of open source projects to work properly:
* **[Django](https://www.djangoproject.com/)** - HTML enhanced for web apps! (FrontEnd/UI)
* **[Praw](https://praw.readthedocs.io/)** - reddit API
* **[Heroku](https://dashboard.heroku.com)** - Hosting Platform
* **[Pushshift](https://pushshift.io/)** - API for reddit search


### Installation

This app requires [Django](https://www.djangoproject.com/) v3+ to run, PIP for handling python package. You should require Python3, PIP ans pipenv installed on your system

1: Clone this Repository
```sh
$ git clone https://github.com/Parth910/RedditTL.git
```
2: Change diractory
```sh
$ cd RedditTL
```
3: Start virtual environment

```sh
$ pipenv shell
```

4: Install dependencies

```sh
$  pip install
```
5: Run server

```sh
$  ./manage.py runserver
```
Now your server is running at localhost:8000

### Database Models

User Model

Auth Model

Subreddit Model

Post Model

Author Model

### App flow

First you have to register yourself with app. After registration you have to link reddit account with app(you can delink also), after linking you can visit home page for your subreddits information.

##(if there is some application error occurs please go to the home page and delink your Reddit and try to relink your reddit account )

### Live demo
This app is hosted on Heroku at [Here](https://reddit-tl.herokuapp.com/)

### Conatact Details
* Name: **Parth Patel**
* Phone: **+91 6354813121**
* Email: **prp4203@gmail.com**
* altEmail: **17ucs107@lnmiit.ac.in**
* website: **[Parth910.github.io](https://Parth910.github.io)**

## Want to Contribute!!
  First off, thanks for taking the time to contribute! 


### Development Setup
* To contribute in this you have this application locally.so first install from [here](https://github.com/Parth910/RedditTL/blob/master/README.md#installation).
### Styleguides

#### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

#### Python Styleguide

* All Python must adhere to Python Standard Style.
#### Git Issues and Pull request
 * Feel free to submit issues and enhancement requests.

