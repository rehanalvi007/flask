from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>this is my home page</h1>"


@app.route('/welcome')
def welcome():
    return "welcome to flask tutorial"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and score is "  + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and score is" + str(score)
@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
         physics=float(request.form['physics'])
         chemistry=float(request.form['chemistry'])
         maths=float(request.form['maths'])

         avg_marks = round((physics+chemistry+maths)/3,2)

         results=""
         
         if avg_marks>=33:
             results="success" 
         else:
             results="fail"

         #return redirect(url_for(results,score=avg_marks))
                

         return render_template('result.html',result = avg_marks)

if __name__ == "__main__":
    app.run(debug=True)