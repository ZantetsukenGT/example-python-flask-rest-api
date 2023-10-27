from flask import jsonify
import json

# unused
def to_json(dict):
    return json.dumps(dict, sort_keys=True, default=str)

def http_ok_json_200(dict):
    res = jsonify(dict)
    res.status = 200
    return res

def http_ok_message_200(message):
    res = jsonify( { 'message': str(message) } )
    res.status = 200
    return res

def http_error_400(message):
    res = jsonify( { 'message': str(message) } )
    res.status = 400
    return res

def http_error_500(message):
    res = jsonify( { 'message': str(message) } )
    res.status = 500
    return res
