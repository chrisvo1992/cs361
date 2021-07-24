from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuration

app = Flask(__name__)

# Routes
all_posts = [
    {
        'title' : 'Post 1',
        'content': 'This is the content of post 1.',
        'author': 'chris'
    },
    {
        'title' : 'Post 2',
        'content': 'This is the content of post 2.'
    }
]



@app.route("/aboutus")
def hello():
    return render_template("about.html")

@app.route('/')
def root():
    return render_template("base.html")

@app.route("/home")
def result():
    return render_template("result1.html")


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author='Aron')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts = all_posts)


# Listener

if __name__ == "__main__":
    app.run(debug=True)

