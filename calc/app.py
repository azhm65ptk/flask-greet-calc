# Put your app in here.
from flask import Flask, request
from operations import sub, add, mult, div

app=Flask(__name__)


@app.route('/add')
def do_add():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(a+b)


@app.route('/sub')
def subtrt():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(a-b)

@app.route('/mult')
def do_multi():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(a*b)

@app.route('/div')
def divide():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(a/b)

OPERATOR={
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<oper>')
def math(oper):
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    result=OPERATOR[oper](a,b)
    return str(result)