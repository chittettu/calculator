from flask import Flask, render_template,request
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
        result=number1+number2
    elif operation=="multiplication":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    elif operation=="subtraction":
        result=number1-number2
    


if __name__=='__main__':
    app.run()

