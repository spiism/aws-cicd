import json
import os

def handler(event, context):
    version = os.environ.get("VERSION", "0.0")
    respond_body = {
        "message": "test",
        "version": {version }
    }
    return {
        "statusCode": 200, 
        "body": json.dumps(respond_body) 
    }