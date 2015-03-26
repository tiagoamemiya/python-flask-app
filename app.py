"""
Name: Simple Blog
Desc: Flask App
<<<<<<< HEAD
"""
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def view_home():
	return 'Blog Home Page'

@app.route('/post/<post_id>')
def view_post(post_id):
	return 'Post %s' % post_id

if __name__ == '__main__':
	app.debug = True
	app.run()
=======
"""
>>>>>>> 3228b13a5b32797b9e49f72ef78570f2904c9e9f
