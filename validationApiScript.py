import json
import requests
import re
from http.server import BaseHTTPRequestHandler, HTTPServer

def is_non_empty_string(value,user_id):
    if not isinstance(value(str)) or not value.string():
        return print('user_id must be a non-empty string')
    return None

def is_valid_email(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return print('email must be in a valid email format')
    return None

def is_valid_timestamp(timestamp):
    if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', timestamp):
        return print('timestamp must be in ISO 8601 format')
    return None

def is_valid_price(price):
    if not re.match(r'^\d+\.\d{2}$', price):
        return print('price must be a positive float')
    return None


def Validate_JsonData(data):
    required_fields = ['user_id', 'email', 'timestamp', 'items']
    for field in required_fields:
        if field not in data:
            return print('Missing required field: {}'.format(field))
        

    if error:= is_non_empty_string(data['user_id']):
        return error
    
    if error:= is_valid_email(data['email']):
        return error

    if error:= is_valid_timestamp(data['timestamp']):
        return error
    
    if error:= is_valid_price(data['is_valid_price']):
        return error
    

class ValidateApiJson(BaseHTTPRequestHandler):

    def _set_headers(self,code=200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def Api_Post(self):
        self._set_headers()
        data_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(data_length)    

        try:
            data = json.loads(post_data)
            error = Validate_JsonData(data)
            if error:
                self.send_response(400)
                response = {'error400': error}

            else:
                response = {'status': 'success','message': 'Data is valid'}


        except json.JSONDecodeError:
                response = {'error': 'Invalid JSON data'}
                self._set_headers(400)
                self.wfile.write(b'Invalid JSON data')
                return
            
def Validate_Data():
     print()
