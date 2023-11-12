from limit_requests import before_request
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
# using limiter from library
# limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "30 per hour"])

# my solution for limiter, uncoment if you want to use it
# @app.before_request
# def check_limit():
#     return before_request()

@app.route('/error', methods=['GET'])
#@app.route('/limited')
def error():
    return render_template('index.html', match_status='KO'), 400

@app.route('/succes', methods=['GET'])
def succes():
    return render_template('index.html', match_status='OK'), 200

@app.route('/', methods=['GET', 'POST'])
@app.route('/limited')
@app.route('/error', methods=['POST'])
@app.route('/succes', methods=['POST'])
def index():
    expected_string = "h4b2"
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
