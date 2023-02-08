import flask
import base64

app = flask.Flask(__name__)

@app.route('/')
def main():
	return flask.send_file('index.html')

@app.route('/<path:path>')
def r(path):
#	with open(path,'r') as e:
#		return e.read()
	return flask.send_file(path)
@app.route('/check/<hash>')
def ha(hash):
	return flask.render_template('ls.html',kk=str(base64.b64decode(hash[::-1]),'utf-8'))
app.run("0.0.0.0",80)
