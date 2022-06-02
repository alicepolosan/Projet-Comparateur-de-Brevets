from flask_wtf import FlaskForm
from wtforms import (StringField, SelectMultipleField)
from wtforms.validators import InputRequired, Length


class BrevetForm(FlaskForm):
    annee_depot = StringField('Annee de depot', validators=[InputRequired(),
                                             Length(min=4, max=4)])
    annee_delivrance = StringField('Annee de delivrance',
                                validators=[InputRequired(),
                                            Length(min = 4, max = 4)])
    pays = SelectMultipleField('Pays', choices = ['Albanie', 'Allemagne', 'Autriche'], validators=[InputRequired()])