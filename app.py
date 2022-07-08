from flask import Flask
from flask import render_template
from flask import request, url_for, redirect
app = Flask(__name__,template_folder='template')

@app.route('/dashboard/<name>')
def dashboard(name):
    print(name)
    return 'Welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'Post':
        user = request.form('name')
        return redirect(url_for('dashboard',name=user))
    else:
        user = request.args.get('name')
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

