from flask import Flask, render_template

from vsearch import searc4vowels

app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask'

@app.route('/searhc4')
def do_search() -> str:
    return str(searc4vowels('life, universe and everthing'))

@app.route('/enter')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search41etters on the web!')

app.run()