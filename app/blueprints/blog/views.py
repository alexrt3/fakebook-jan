from .import bp as blog_bp
from flask import request, flash, redirect, url_for

@blog_bp.route('/post/create', methods=['POST'])
def create_post():
    if request.method == 'POST':
        print(request.form)
        flash('Post was created successfully', 'info')
        return redirect(url_for('main.home'))