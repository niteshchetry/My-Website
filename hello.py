from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/github')
def GitHub():
    return redirect('https://github.com/niteshchetry')

if __name__ == '__main__':
    app.run(debug=TRUE)
