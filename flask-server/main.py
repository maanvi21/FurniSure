from flask import Flask, render_template

app = Flask(__name__)



@app.route('/scan')
def scan():
    return render_template("scan.html")

@app.route('/productdesc')
def productdesc():
    return render_template("productdesc.html")

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)