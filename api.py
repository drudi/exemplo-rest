import bottle
from bottle import request, response
from bottle import post, get, put, delete

@post('/post')
def post_endpoint():
    response.status = 201
    return

@get('/get')
def get_endpoint():
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    return '{"ola": "Mundo"}'

@put('/put')
def put_endpoint():
    response.status = 201
    return

@delete('/delete')
def delete_endpoint():
    response.status = 204
    return
