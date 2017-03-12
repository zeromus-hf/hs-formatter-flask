from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index', methods=['POST','GET'])
def index():
    output = ''
    input  = ''
    errors = []

    target = app.config['target_script']

    if request.method == 'POST':
        print request.form
        if request.form.get('input') is None:
            print 'No data!'
        else:
            input  = request.form['input']

        try:
            output = target.execute(input)
        except Exception as e:
            errors.append('Error {}'.format(e))

    return render_template('index.html', errors=errors, input=input, output=output)

