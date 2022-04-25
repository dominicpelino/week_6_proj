from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login.utils import login_required
from hero_inventory.models import Hero, db
from flask_login import current_user
from hero_inventory.forms import HeroBuilderForm

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')


@site.route('/profile')
@login_required
def profile():
    heroes = Hero.query.filter_by(user_token=current_user.token).all()
    return render_template('profile.html', heroes = heroes)


@site.route('/build', methods = ['GET', 'POST'])
@login_required
def build():
    form = HeroBuilderForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            alias = form.alias.data
            species = form.species.data
            description = form.description.data
            powers = form.powers.data
            max_speed = form.max_speed.data
            max_strength = form.max_strength.data
            print(name, powers)

            BuiltHero = Hero(name, alias, species, description, powers, max_speed, max_strength, user_token=current_user.token)


            db.session.add(BuiltHero)
            db.session.commit()

            return redirect(url_for('site.build'))

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')


    return render_template('build.html', form = form )