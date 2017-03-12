from app import app
from flask import render_template, request

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

