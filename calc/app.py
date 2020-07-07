# Put your app in here.
from flask import Flask, request
import operations as op
app = Flask(__name__)

# http://127.0.0.1:5000/add?a=1&b=2


@app.route('/add')
def add():

    a = request.args['a']
    b = request.args['b']
    add_sum = op.add(int(a), int(b))
    return f"{add_sum}"


@app.route('/sub')
def sub():

    a = request.args['a']
    b = request.args['b']
    sub_num = op.sub(int(a), int(b))
    return f"{sub_num}"


@app.route('/mult')
def mult():

    a = request.args['a']
    b = request.args['b']
    mult_num = op.mult(int(a), int(b))
    return f"{mult_num}"


@app.route('/div')
def div():

    a = request.args['a']
    b = request.args['b']
    div_num = op.div(int(a), int(b))
    return f"{div_num}"


OPS = {
    'add': op.add,
    'sub': op.sub,
    'mult': op.mult,
    'div': op.div
}


@app.route('/math/<op>')
def math_op(op):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPS[op](a, b)
    return str(result)
