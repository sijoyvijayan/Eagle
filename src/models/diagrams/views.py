from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.utils import redirect

from src.models.users.user import User
import src.models.users.errors as UserErrors
import src.models.users.decorators as user_decorators


from src.log_parsing import *

from src.models.diagrams.diagram import Transaction


log_obj=log_analyzer()	

diagram_blueprint = Blueprint('diagrams', __name__)


@diagram_blueprint.route('/show_sequence_diagram/<string:ue_id>')



def display_sequence_diagram(ue_id):

    trn_list = []
    print("UE ID received from GUI is in display sequency dia",ue_id)
    trn_list=get_fsm_list(int(ue_id))
   
    print ("LADDER DIAGRAM IN VIEWS") 
    for line in trn_list :

        print(line)

    
    #trn_list.append(Transaction("UE", "AshisheNB", "RRC Connection Request"))
    #trn_list.append(Transaction("eNB", "UE", "RRC Connection Setup"))
    #trn_list.append(Transaction("UE", "eNB", "RRC Connection Setup Complete"))
    return render_template('diagrams/diagram_template.html', trn_list=trn_list)

@diagram_blueprint.route('/show_ue_id_l3_logs')
def display_ue_ids_l3_logs():
    
    global log_obj

    print (dir(log_obj.ue_id_list[1]))
    print ("UE_IDS-------------in display ue ids l3 logs")
    for ue in log_obj.ue_id_list :

        print("ue_id==>",ue.ue_id)

    
    #trn_list.append(Transaction("UE", "AshisheNB", "RRC Connection Request"))
    #trn_list.append(Transaction("eNB", "UE", "RRC Connection Setup"))
    #trn_list.append(Transaction("UE", "eNB", "RRC Connection Setup Complete"))
    return render_template('diagrams/show_ue_id_template.html', ue_id_list=log_obj.ue_id_list)

@diagram_blueprint.route('/logout')
def logout_user():

    session['email'] = None
    return redirect(url_for('home'))


@diagram_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass


def get_fsm_list(ue_id):
    global log_obj
    #clean_l3_logs()
    #ue_id_list=get_ue_ids_l3_logs()
    #show_ue_ids(ue_id_list)
    print("UE ID in get_fsm_list",ue_id)
    trn_list=log_obj.show_ladder_diagram(log_obj.ue_id_list[ue_id])

    return trn_list

def get_ue_l3_ue_ids():

    ue_id_list=get_ue_ids_l3_logs()

    return ue_id_list
