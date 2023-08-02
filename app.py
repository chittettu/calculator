from flask import Flask, render_template,request,jsonify
import json
app=Flask(__name__)


@app.route('/')
def welcome():
    return "welcome to flask"

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        number1=float(request.form["number1"])
        number2=float(request.form["number2"])
        operation=request.form["operation"]


        if operation=="add":
            result=int(number1)+int(number2)
        elif operation=="multiplication":
             result=int(number1)*int(number2)
        elif operation=="division":
            result=int(number1)/int(number2) 
        elif operation=="subtraction":
            result=int(number1)-int(number2)

    return render_template('result.html',results=result)


   


    


if __name__=='__main__':
    app.run(debug=True)

