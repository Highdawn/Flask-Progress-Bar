'''This is the main flask python file'''
import time
from flask import Flask, Response, render_template
import flask_progress_bar.flask_progress_bar as FPB

app = Flask(__name__)


def example_generator():
    ''''
    This function is an example of the structure you must have

    You must yield a array with the [current_value, limit_value]
    '''
    x = 0
    y = 50
    while x < y:
        x += 1
        yield [x, y]
        time.sleep(0.5)


@app.route('/')
def index():
    '''This function redirects the user to the index page'''
    return render_template('index.html')


@app.route('/completed')
def complete():
    '''This function redirects the user to the complete process  page'''
    return render_template('complete.html')


@app.route('/progress')
def progress():
    ''' 
    Function that return the ammount of photos taken for the progress bar 

    Follow this structure and replace the example_generator function with your own
    '''
    return Response(FPB.progress(example_generator()), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
