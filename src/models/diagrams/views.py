from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.utils import redirect

from src.models.users.user import User
import src.models.users.errors as UserErrors
import src.models.users.decorators as user_decorators

from src.models.diagrams.diagram import Transaction

diagram_blueprint = Blueprint('diagrams', __name__)


@diagram_blueprint.route('/show_sequence_diagram')
def display_sequence_diagram():
    trn_list = []
    trn_list.append(Transaction("UE", "eNB", "RRC Connection Request"))
    trn_list.append(Transaction("eNB", "UE", "RRC Connection Setup"))
    trn_list.append(Transaction("UE", "eNB", "RRC Connection Setup Complete"))
    return render_template('diagrams/diagram_template.html', trn_list=trn_list)


@diagram_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('home'))


@diagram_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass
