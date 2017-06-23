# project/recipes/forms.py

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')

class AddRecipeForm(FlaskForm):
    recipe_title = StringField('Recipe Title', validators=[DataRequired()])
    recipe_description = StringField('Recipe Description', validators=[DataRequired()])