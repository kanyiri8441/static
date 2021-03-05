from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("mystatic.html")



if __name__=='__main__':
  app.run(debug=True) 
