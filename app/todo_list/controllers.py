from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from .models import db, Post

bp_todo = Blueprint('todo', __name__,
                    #url_prefix='/todo_list',
                    template_folder='templates')


@bp_todo.route('/', methods=['GET', 'POST'])
def todo_lst():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

# @bp_todo.route('/')
# def index():
#     flash('Redirect to todo_list.')
#     return redirect(url_for('todo_list'))
