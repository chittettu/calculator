from flask import Flask, render_template,request,jsonify
import json
app=Flask(__name__)
@app.route('/')

def welcome():
    return "welcome to flask"

@app.route('/cal', methods=["GET"])
def math_calculator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiplication":
        result=int(number1)*int(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    elif operation=="subtraction":
        result=int(number1)-int(number2)
    return f"the operation is {operation} and result is {result}"

    


if __name__=='__main__':
    app.run()

