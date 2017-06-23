# project/recipes/views.py
 
#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import Recipe
from .forms import AddRecipeForm, flash_errors
from app import db
 
################
#### config ####
################
 
recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')
 
 
################
#### routes ####
################
 
@recipes_blueprint.route('/')
def index():
    all_recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=all_recipes)


@recipes_blueprint.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = AddRecipeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_recipe = Recipe(form.recipe_title.data, form.recipe_description.data)
            db.session.add(new_recipe)
            db.session.commit()
            flash('New recipe, {}, added!'.format(new_recipe.recipe_title), 'success')
            return redirect(url_for('recipes.index'))
        else:
            flash_errors(form)
            flash('ERROR! Recipe was not added.', 'error')

    return render_template('add_recipe.html',
                           form=form)