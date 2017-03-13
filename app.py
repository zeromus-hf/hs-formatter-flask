#!flask/bin/python
from flask import render_template, request, Flask
import importlib

app = Flask(__name__)

app.config.update({
    'target_script' : importlib.import_module('target_script')
})


@app.route('/')
@app.route('/index', methods=['POST','GET'])
def index():
    output = ''
    input  = ''
    stdout = ''
    errors = []

    target = app.config['target_script']

    if request.method == 'POST':
        if request.form.get('input') is None:
            print 'No data!'
        else:
            input  = request.form['input']

        try:
            stdout, output = target.execute(input)
        except Exception as e:
            errors.append('Error {}'.format(e))
            raise

    return render_template('index.html', errors=errors, input=input, stdout=stdout, output=output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
