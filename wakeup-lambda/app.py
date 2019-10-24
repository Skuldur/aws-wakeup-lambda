import requests
from chalice import Chalice
import boto3

app = Chalice(app_name='wakeup-lambda')
lambda_client = boto3.client('lambda')

LAMBDAS_TO_WAKEUP = [
	'https://hkgb1tvfwd.execute-api.eu-west-1.amazonaws.com/api/'
]
LAMBDAS_TO_INVOKE = [
	'athena-play_intent-lambda-dev-index',
    'athena-increase_volume_intent-lambda-dev-index',
    'athena-resume_intent-lambda-dev-index',
    'athena-decrease_volume_intent-lambda-dev-index',
    'athena-ask_wiki_intent-lambda-dev-index',
    'athena-pause_intent-lambda-dev-index',
    'athena-next_intent-lambda-dev-index',
    'athena-party_intent-lambda-dev-index',
    'athena-set_volume_intent-lambda-dev-index',
    'athena-change_spotify_device_intent-lambda-dev-index',
    'athena-christmas_time_intent-lambda-dev-index'
]

@app.lambda_function()
def index(event, context):
    for lambda_url in LAMBDAS_TO_WAKEUP:
    	requests.post(lambda_url, data=[])
    for lambda_name in LAMBDAS_TO_INVOKE:
    	response = lambda_client.invoke(
            FunctionName=lambda_name,
            InvocationType='Event',
            LogType='None',
            Payload='',
            Qualifier='$LATEST'
        )


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
