from flask import Flask, render_template

# app is a object(instrance) Flask (class)
app = Flask(__name__)
# @app.route('/') the @ makes a decorator the / is a arguemnt to it, if someone requests the webapp homepage(/) it will run index
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/pageone')
def pageone():
    return render_template("pageone.html")


#host 0.0.0.0 makes it run on the network and the port 5000 is what port is open on my pc
app.run(host="0.0.0.0", port=25565, debug=True)
