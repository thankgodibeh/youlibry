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
    """Renders the trending page."""
    return render_template(
        'trending.html',
        title='Trending | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/explore')
def explore():
    """Renders the explore page."""
    return render_template(
        'explore.html',
        title='Explore | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/live')
def live():
    """Renders the live page."""
    return render_template(
        'live.html',
        title='Live Classroom | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/view')
def view():
    """Renders the view page."""
    return render_template(
        'view.html',
        title='View Video or Playlist | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/libraries')
def libraries():
    """Renders the libraries page."""
    return render_template(
        'libraries.html',
        title='Libraries | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/categories')
def categories():
    """Renders the categories page."""
    return render_template(
        'categories.html',
        title='Categories | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/historypage')
def historypage():
    """Renders the history page."""
    return render_template(
        'history-page.html',
        title='History | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/subscriptions')
def subscriptions():
    """Renders the subscriptions page."""
    return render_template(
        'subscriptions.html',
        title='Subscriptions | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/subscriptions2')
def subscriptions2():
    """Renders the subscriptions page."""
    return render_template(
        'subscriptions2.html',
        title='Subscriptions | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/subscriptions3')
def subscriptions3():
    """Renders the subscriptions page."""
    return render_template(
        'subscriptions3.html',
        title='Subscriptions | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/subscriptions4')
def subscriptions4():
    """Renders the subscriptions page."""
    return render_template(
        'subscriptions4.html',
        title='Subscriptions | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/library')
def library():
    """Renders the library page."""
    return render_template(
        'library.html',
        title='Name of library | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/library2')
def library2():
    """Renders the library page."""
    return render_template(
        'library2.html',
        title='Name of library | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/category')
def category():
    """Renders the category page."""
    return render_template(
        'category.html',
        title='Name of category | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login | YouLibry eLearning Facility',
        year=datetime.now().year
    )

@app.route('/register')
def register():
    """Renders the register page."""
    return render_template(
        'register.html',
        title='Register | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/forgotpassword')
def forgotpassword():
    """Renders the forgot-password page."""
    return render_template(
        'forgot-password.html',
        title='Forgot Password | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/profile')
def profile():
    """Renders the profile page."""
    return render_template(
        'profile.html',
        title='Profile | YouLibry eLearning Facility ',
        year=datetime.now().year
    )

@app.route('/settings')
def settings():
    """Renders the settings page."""
    return render_template(
        'settings.html',
        title='Settings | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/notfound')
def notfound():
    """Renders the 404 page."""
    return render_template(
        '404.html',
        title='Page Not Found! | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


@app.route('/blank')
def blank():
    """Renders the blank page."""
    return render_template(
        'blank.html',
        title='Blank Page | YouLibry eLearning Facility ',
        year=datetime.now().year
    )


"""  Below consideration for Version/Stage 2  """

@app.route('/account')
def account():
    """Renders the contact page."""
    return render_template(
        'account.html',
        title='account',
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

@app.route('/uploadvideo')
def uploadvideo():
    """Renders the contact page."""
    return render_template(
        'upload-video.html',
        title='upload video',
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

@app.route('/videopage')
def videopage():
    """Renders the contact page."""
    return render_template(
        'video-page.html',
        title='video page',
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
