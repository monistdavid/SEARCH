from flask import render_template, Blueprint, request

searching_bp = Blueprint('searching', __name__)


@searching_bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = '斗罗大陆'  # Replace with your actual search function
        return render_template('search.html', results=results)
    else:
        return render_template('search.html')
