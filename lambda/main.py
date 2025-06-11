def handler(event, context):
    respond_body = {
        "message": "test",
        "version": "1.0.0"
    }
    return {
        "statusCode": 200, 
        "body": json.dumps(respond_body) 
    }