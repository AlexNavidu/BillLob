from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
    return app.send_static_file('index.html')
@app.route('/echo/<things>')
def echo(things):
    return "Say hello to my little friend: %s" % things
app.run(port=8001, debug=True)

