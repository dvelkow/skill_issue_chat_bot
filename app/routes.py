from app import app
from flask import render_template

@app.route('placeholer')
@app.route('/placeholer')
def index():
    return render_template('placeholer.html', title='Home', content='This is a placeholder.')
