from flask import Flask, render_template
from flask_wtf import FlaskForm   #Importing the FlaskForm class
from wtforms import StringField, SubmitField


app=Flask(__name__)


app.config['SECRET_KEY']='mysecretkey' #This is required for security reasons


class InfoForm(FlaskForm):       #Inheriting FlaskForm in the InfoForm class
    breed = StringField("What Breed are you?")  #Here we are passing the label in the argument
    submit = SubmitField("Submit")



@app.route('/', methods=['GET','POST'])
def index():
    breed = False

    form = InfoForm()  #Storing the instance of the InfoForm in the form variable

    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = '' #Storing an empty string in the variable

    return render_template('index.html',form=form,breed=breed)


if __name__=='__main__':
    app.run(debug=True)    





