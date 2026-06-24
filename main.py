from flask import Flask, render_template, request, redirect
import mysql.connector as a

db = a.connect(host='localhost', user='root', password='password', database='codes')
c = db.cursor()

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        url = request.form['url']
        code = request.form['code']
        if "https://" not in url and "http://" not in url:
            url = "http://"+url
        try:
            c.execute(f"insert into code values('{url}','{code}')")
            db.commit()
            error = "Created!"
        except:
            error = "code already exists"
        return render_template('index.html', error = error)

    return render_template('index.html')

@app.route('/<code>')
def open(code):
    try:
        c.execute(f"select url from code where code = '{code}'")
        url = c.fetchone()[0]
        return redirect(url)
    except:
        error = "No URL found"
        return render_template('error.html',error=error)
    
if __name__ == '__main__' :
    app.run(port=5000)