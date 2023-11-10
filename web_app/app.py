import time

from flask import Flask, render_template, request, make_response, redirect, jsonify
from flask import Flask, render_template, request, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager, UserMixin
import api

from web_app.RateLimiter import RateLimiter

app = Flask(__name__)
# limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "30 per hour"])
MAX_REQUESTS = 5
TIME_INTERVAL = 60  # in seconds

# Token bucket for rate limiting
token_bucket = {
    'tokens': MAX_REQUESTS,
    'last_refill_time': time.time(),
}

def refill_tokens():
    current_time = time.time()
    time_passed = current_time - token_bucket['last_refill_time']
    tokens_to_add = time_passed / TIME_INTERVAL
    token_bucket['tokens'] = min(MAX_REQUESTS, token_bucket['tokens'] + tokens_to_add)
    token_bucket['last_refill_time'] = current_time

@app.before_request
def before_request():
    refill_tokens()

    if token_bucket['tokens'] >= 1:
        token_bucket['tokens'] -= 1
    else:
        return jsonify({'error': 'Rate limit exceeded. Please try again later.'}), 429
# Predefined string to match user input

@app.route('/error', methods=['GET'])
@app.route('/limited')
def error():
    # Render an error.html template and then redirect back to the root URL
    return render_template('index.html', match_status='KO'), 400

@app.route('/succes', methods=['GET'])
def succes():
    # Render an error.html template and then redirect back to the root URL
    return render_template('index.html', match_status='OK'), 200

@app.route('/', methods=['GET', 'POST'])

@app.route('/error', methods=['POST'])
@app.route('/succes', methods=['POST'])
def index():
    expected_string = "1234"
    #limiter.check_request()
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input == expected_string:
            return redirect('/succes')

        elif user_input == '':
            pass
        else:
            return redirect('/error')

    return render_template('index.html', match_status=''), 200



if __name__ == '__main__':
    app.run(debug=True)
