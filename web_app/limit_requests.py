import time
from flask import jsonify

MAX_REQUESTS = 5
TIME_INTERVAL = 20  # in seconds

token_bucket = {
    'tokens': MAX_REQUESTS, # how many tokens are available
    'last_refill_time': time.time(),
}

def refill_tokens():
    current_time = time.time()
    time_passed = current_time - token_bucket['last_refill_time']
    tokens_to_add = time_passed / TIME_INTERVAL
    # if the time passed is greater than the time interval, add tokens, but never more than the max requests
    token_bucket['tokens'] = min(MAX_REQUESTS, token_bucket['tokens'] + tokens_to_add)
    token_bucket['last_refill_time'] = current_time

def before_request():
    # check how many tokens are available
    refill_tokens()

    # check if limit for tokens exceeded
    if token_bucket['tokens'] >= 1:
        token_bucket['tokens'] -= 1 # if not, decrement the available tokens
    else:
        return jsonify({'error': 'Rate limit exceeded. Please try again later.'}), 429# if so return 429
