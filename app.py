from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_ke

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

#homepage
@app.route('/', methods=['GET', 'POST'])
def homepage():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form Submitted Successfully')
    return render_template('index.html', name=name, form=form)

@app.route('/intro')
def intro():
    return render_template('intro.html')

#error handling 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#error handling 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
