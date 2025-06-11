import json
import os

def handler(event, context):
    
    profile_data = {
        "name": "Michael Ho", 
        "job": "Full-Stack Software Engineer",
    }
    
    try:
        # Get HTTP method
        http_method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'GET'))
        
        if http_method == 'GET':
            response_body = {
                "success": True,
                "data": profile_data,
                "version": os.environ.get("VERSION", "1.0.0"),
                "note": "This is a simple version without database integration"
            }
            status_code = 200
        else:
            response_body = {
                "success": False,
                "message": f"Method {http_method} not allowed",
                "version": os.environ.get("VERSION", "1.0.0")
            }
            status_code = 405
            
        return {
            "statusCode": status_code,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(response_body, default=str)
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": False,
                "message": "Internal server error",
                "error": str(e),
                "version": os.environ.get("VERSION", "1.0.0")
            })
        }