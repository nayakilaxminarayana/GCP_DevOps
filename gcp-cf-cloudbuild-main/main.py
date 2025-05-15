# import os
# from datetime import datetime
# import mysql.connector

# def return_basic(request):
#   now = datetime.now()
#   return '<h1>Welcome to Cloud Functions and Cloud Build demo</h1><br/>' + str(now)


# def hello_world(request):
#     """HTTP Cloud Function.
#     Args:
#         request (flask.Request): The request object.
#     Returns:
#         The response text, or any set of values that can be turned into a
#         Response object using `make_response`
#         <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
#     """
#     return 'Hello, World!'


import os
from flask import jsonify

def hello_world(request):
    """HTTP Cloud Function that reads from environment variables"""
    return jsonify({
        'repository': os.getenv('REPO_NAME', 'GCP-DevOps'),
        'test_variables': {
            'test1': os.getenv('TEST_VAR1', 'test-1'),
            'test2': os.getenv('TEST_VAR2', 'test-2')
        },
        'build_info': {
            'build_id': os.getenv('BUILD_ID', 'not_available'),
            'trigger_id': os.getenv('TRIGGER_ID', 'not_available')
        },
        'message': 'Environment variables loaded successfully!'
    })
