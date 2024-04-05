from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def hello():
	# print path
	return render_template('index.html')

@app.route('/get_path')
def get_path():
	# list directory
	return os.listdir('.')
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)