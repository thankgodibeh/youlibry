"""
Routes and views for the flask application.
"""
from flask import Flask
app = Flask(__name__)

from datetime import datetime
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='YouLibry eLearning Facility | Library Of Libraries',
        year=datetime.now().year,
    )

@app.route('/trending')
def trending():
    """Renders the contact page."""
    return render_template(
        'trending.html',
        title='Trending | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/home2')
def home2():
    """Renders the contact page."""
    return render_template(
        'index0.html',
        title='Home2 | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/explore')
def explore():
    """Renders the contact page."""
    return render_template(
        'explore.html',
        title='Explore | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/live')
def live():
    """Renders the contact page."""
    return render_template(
        'live.html',
        title='Live Classroom | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/view')
def view():
    """Renders the contact page."""
    return render_template(
        'view.html',
        title='View Video or Playlist | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/libraries')
def libraries():
    """Renders the contact page."""
    return render_template(
        'libraries.html',
        title='Libraries | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/categories')
def categories():
    """Renders the contact page."""
    return render_template(
        'categories.html',
        title='Categories | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/historypage')
def historypage():
    """Renders the contact page."""
    return render_template(
        'history-page.html',
        title='History | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/subscriptions')
def subscriptions():
    """Renders the contact page."""
    return render_template(
        'subscriptions.html',
        title='subscriptions',
        year=datetime.now().year
    )

@app.route('/library')
def library():
    """Renders the contact page."""
    return render_template(
        'library.html',
        title='library',
        year=datetime.now().year
    )

@app.route('/library2')
def library2():
    """Renders the contact page."""
    return render_template(
        'library2.html',
        title='library',
        year=datetime.now().year
    )


@app.route('/category')
def category():
    """Renders the contact page."""
    return render_template(
        'category.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
        title='Login | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/videopage')
def videopage():
    """Renders the contact page."""
    return render_template(
        'video-page.html',
        title='video page',
        year=datetime.now().year
    )

@app.route('/uploadvideo')
def uploadvideo():
    """Renders the contact page."""
    return render_template(
        'upload-video.html',
        title='upload video',
        year=datetime.now().year
    )

@app.route('/courses')
def courses():
    """Renders the contact page."""
    return render_template(
        'courses.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/account')
def account():
    """Renders the contact page."""
    return render_template(
        'account.html',
        title='account',
        year=datetime.now().year
    )

@app.route('/profile')
def profile():
    """Renders the contact page."""
    return render_template(
        'profile.html',
        title='Profile | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/upload')
def upload():
    """Renders the contact page."""
    return render_template(
        'upload.html',
        title='upload',
        year=datetime.now().year
    )


@app.route('/settings')
def settings():
    """Renders the contact page."""
    return render_template(
        'settings.html',
        title='settings',
        year=datetime.now().year
    )


@app.route('/library_account')
def library_account():
    """Renders the contact page."""
    return render_template(
        'library-account.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/register')
def register():
    """Renders the contact page."""
    return render_template(
        'login.html',
        title='library account',
        year=datetime.now().year
    )