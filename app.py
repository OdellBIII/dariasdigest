from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Sample article data
ARTICLES = [
    {
        'id': 1,
        'title': 'My First Blog Post',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'image': 'https://via.placeholder.com/300x200',
        'date': datetime(2024, 1, 15),
        'content': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.'''
    }
]

@app.route('/')
def construction():
    return render_template('construction.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', articles=ARTICLES)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in ARTICLES if a['id'] == article_id), None)
    if not article:
        return "Article not found", 404
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)