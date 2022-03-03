#import libraries
from flask import Flask, render_template, url_for, request, redirect
#Initialize the flask App
app = Flask(__name__)

#default page of our web-app
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)