from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    email=request.form['email']
    year=request.form['year']
    return render_template('successful.html', name=name, year=year)
if __name__=='__main__':
    app.run(host="127.0.0.1",debug=True)



