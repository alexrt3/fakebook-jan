from app import db
from flask import render_template, request, redirect, url_for
from app.blueprints.auth.models import User
from app.blueprints.blog.models import Post
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as main_bp

@main_bp.route('/')
def home():
    context = {
        'user': current_user,
        'posts': current_user.followed_posts().all()
        # 'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    return render_template('home.html', **context)

@main_bp.route('/profile')
@login_required
def profile():
    context = {
        'posts': [p for p in Post.query.order_by(Post.date_created.desc()).all() if p.user_id == current_user.id]
    }
    return render_template('profile.html', **context)

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/explore')
@login_required
def explore():
    context = {
        'users': [user for user in User.query.all() if current_user.id != user.id]
    }
    return render_template('explore.html', **context)