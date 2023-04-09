
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods = ['GET'])
def upload_page():
    return render_template('index.html')


@app.route('/upload_file', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		file.save(secure_filename(file.filename))
		return redirect('/upload')

if __name__ == '__main__':
	app.run(debug=True)