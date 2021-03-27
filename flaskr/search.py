import functools

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('search', __name__)

@bp.route('/')
def index():
  return redirect(url_for('search.search'))

@bp.route('/search', methods=('GET', 'POST'))
def search(vendors=None):
  if request.method == 'POST':
    vendors = get_vendors(request.form['distance'])
    return render_template('search/search.html', vendors=vendors)

  return render_template('search/search.html')

@bp.route('/info', methods=('GET', 'POST'))
def info():
  if request.method == 'POST':
    return

  return render_template('search/info.html')

def get_vendors(distance):
  # Make request to external api
  data = [
    {
      'name': "Brady's hotdog stand",
      'address': '123 Main Street, Windsor',
      'rating': 4.3,
      'open': True,
    },
    {
      'name': "Yusuf's rental burgers",
      'address': '456 Main Street, Windsor',
      'rating': 4.9,
      'open': True,
    },
  ]
  return data