from flask import Flask,render_template, request
import weightPredict 

app = Flask(__name__)

def cm_to_inches(cm):
    inches = cm / 2.54
    return inches


@app.route('/',methods =['GET','POST'])
def hello():
    if request.method == 'POST':
        height = request.form['height']
        print(height)
        height_inch = cm_to_inches(float(height))
        weight = weightPredict.weigthPredict([[float(height_inch)]])
    return render_template("index.html" , height = height ,inches = height_inch ,weight=weight)

if __name__ == "__main__":
    app.run()