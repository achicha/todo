from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from flask_login import login_required, current_user
from .models import db, Post

bp_todo = Blueprint('todo', __name__,
                    #url_prefix='/todo_list',
                    template_folder='templates')


@bp_todo.route('/', methods=['GET', 'POST'])
@login_required
def todo_lst():
    error = None
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text=text, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('todo_list.html', posts=posts, error=error)

