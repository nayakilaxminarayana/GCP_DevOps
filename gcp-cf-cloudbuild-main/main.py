# import os
# from datetime import datetime
# import mysql.connector

# def return_basic(request):
#   now = datetime.now()
#   return '<h1>Welcome to Cloud Functions and Cloud Build demo</h1><br/>' + str(now)


def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    return 'Hello, World!'
