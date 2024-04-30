import random

from otree.api import *
from otree.app_template.models import Player, Subsession

author = 'PDH'
doc = """
Your app description
"""

class C(BaseConstants):
    ###important links##
    csv_link = "static/optimal_design.csv"

    #######################################################################
    # game settings
    #######################################################################
    # game is part of WP2A of the MultiTipProject
    NAME_IN_URL = 'stated_choice'
    # groups are only attached in cas of information of each other
    PLAYERS_PER_GROUP = None
    # only 1 round with three phases ('event phase', 'information phase', investment phase')
    NUM_ROUNDS = 1

    ##translation
    NEXT = "next"
    CHOICE = "choice"

    LANDING="landing"
    LOCAL="local"
    NATIONAL="national"
    MILITARY="military"

    FEE = "fee"
    DETECT = "detection rate"
    CORRUPTION = "corruption"
    ELECTION = "direct election"

    LOCAL_CURRENCY= "UGX"
    NO_CORRUPTION = "no corruption"
    LOW_CORRUPTION = "low corruption"
    HIGH_CORRUPTION = "high corruption"

    ELECT = "election"
    NO_ELECT = "no election"

    LANDING="landing"
    LOCAL="local"
    NATIONAL="national"
    MILITARY="military"






def creating_session(subsession: Subsession):
    subsession.optimal_design=get_stated_choice_list()
    max_Block = get_max_Block(subsession.optimal_design)

    for p in subsession.get_players():
        i = int(p.participant.id_in_session)
        for row in subsession.optimal_design:
            if (subsession.treatment == "left_down" or subsession.treatment == "right_down") and int(row['Block'])==i:
                p.all_choice_sets.append(row)
            elif (subsession.treatment == "left_up" or subsession.treatment == "right_up") and int(row['Block']) == max_Block+1-i:
                p.all_choice_sets.append(row)

        input_from_previous_games(p)
        set_stated_choice(p)

    pass


def get_stated_choice_list():
    import csv
    import random

    f = open(C.csv_link)
    data_csv = list(csv.DictReader(f))

    return data_csv

def get_max_Block(optimal_design: list):
    max_number = 0
    for row in optimal_design:
        if int(row['Block']) >max_number:
            max_number=int(row['Block'])

    return max_number

def input_from_previous_games(p: Player):
    p.yearly_payment=p.participant.vars['yearly_payment']
    pass

def set_treatment(subsession: Subsession):
    subsession.treatment = subsession.session.config['treatment']
    pass

def set_stated_choice(p: Player):
    choice_sets =p.all_choice_sets
    for j in range(len(choice_sets)):
        if j==0:
            p.choice_set_1 =choice_sets[j]
            set_choice_set_1(p)
            set_choice_value_1(p)
        elif j==1:
            p.choice_set_2 =choice_sets[j]
            set_choice_set_2(p)
            set_choice_value_2(p)
        elif j==2:
            p.choice_set_3 =choice_sets[j]
            set_choice_set_3(p)
            set_choice_value_3(p)
        elif j==3:
            p.choice_set_4 =choice_sets[j]
            set_choice_set_4(p)
            set_choice_value_4(p)
        elif j==4:
            p.choice_set_5 = choice_sets[j]
            set_choice_set_5(p)
            set_choice_value_5(p)
        elif j==5:
            p.choice_set_6 = choice_sets[j]
            set_choice_set_6(p)
            set_choice_value_6(p)
        elif j==6:
            p.choice_set_7 = choice_sets[j]
            set_choice_set_7(p)
            set_choice_value_7(p)
        elif j==7:
            p.choice_set_8 = choice_sets[j]
            set_choice_set_8(p)
            set_choice_value_8(p)




    pass




class Subsession(BaseSubsession):
    optimal_design = list()
    treatment ="left_down"
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    ###breakpoint p19
    code_breakpoint = models.IntegerField(label="Please enter code")


    def code_breakpoint_error_message(player: Player, value):
        if value != 55:
            return 'You must enter the correct code (55)'

    #######################################################################
    # Choice_Set
    #######################################################################

    yearly_payment=models.IntegerField()

    all_choice_sets=list()

    choice_set_1 = dict()
    choice_set_2 = dict()
    choice_set_3 = dict()
    choice_set_4 = dict()
    choice_set_5 = dict()
    choice_set_6 = dict()
    choice_set_7 = dict()
    choice_set_8 = dict()

    #CHoices
    choice_cs1=models.IntegerField(choices=[1, 2, 3, 4],widget=widgets.RadioSelect)



    #Alternative specific values
    # Choice Set 1

    # Alternative 1
    alt1_A_cs1 = int()
    alt1_B_cs1 = int()
    alt1_C_cs1 = int()
    alt1_D_cs1 = int()
    # Alternative 2
    alt2_A_cs1 = int()
    alt2_B_cs1 = int()
    alt2_C_cs1 = int()
    alt2_D_cs1 = int()
    # Alternative 3
    alt3_A_cs1 = int()
    alt3_B_cs1 = int()
    alt3_C_cs1 = int()
    # Alternative 4
    alt4_A_cs1 = int()
    alt4_B_cs1 = int()
    alt4_C_cs1 = int()

    # Choice Set 2
    # Alternative 1
    alt1_A_cs2 = int()
    alt1_B_cs2 = int()
    alt1_C_cs2 = int()
    alt1_D_cs2 = int()
    # Alternative 2
    alt2_A_cs2 = int()
    alt2_B_cs2 = int()
    alt2_C_cs2 = int()
    alt2_D_cs2 = int()
    # Alternative 3
    alt3_A_cs2 = int()
    alt3_B_cs2 = int()
    alt3_C_cs2 = int()
    # Alternative 4
    alt4_A_cs2 = int()
    alt4_B_cs2 = int()
    alt4_C_cs2 = int()

    # Choice Set 3
    # Alternative 1
    alt1_A_cs3 = int()
    alt1_B_cs3 = int()
    alt1_C_cs3 = int()
    alt1_D_cs3 = int()
    # Alternative 2
    alt2_A_cs3 = int()
    alt2_B_cs3 = int()
    alt2_C_cs3 = int()
    alt2_D_cs3 = int()
    # Alternative 3
    alt3_A_cs3 = int()
    alt3_B_cs3 = int()
    alt3_C_cs3 = int()
    # Alternative 4
    alt4_A_cs3 = int()
    alt4_B_cs3 = int()
    alt4_C_cs3 = int()

    # Choice Set 4
    # Alternative 1
    alt1_A_cs4 = int()
    alt1_B_cs4 = int()
    alt1_C_cs4 = int()
    alt1_D_cs4 = int()
    # Alternative 2
    alt2_A_cs4 = int()
    alt2_B_cs4 = int()
    alt2_C_cs4 = int()
    alt2_D_cs4 = int()
    # Alternative 3
    alt3_A_cs4 = int()
    alt3_B_cs4 = int()
    alt3_C_cs4 = int()
    # Alternative 4
    alt4_A_cs4 = int()
    alt4_B_cs4 = int()
    alt4_C_cs4 = int()

    # Choice Set 5
    # Alternative 1
    alt1_A_cs5 = int()
    alt1_B_cs5 = int()
    alt1_C_cs5 = int()
    alt1_D_cs5 = int()
    # Alternative 2
    alt2_A_cs5 = int()
    alt2_B_cs5 = int()
    alt2_C_cs5 = int()
    alt2_D_cs5 = int()
    # Alternative 3
    alt3_A_cs5 = int()
    alt3_B_cs5 = int()
    alt3_C_cs5 = int()
    # Alternative 4
    alt4_A_cs5 = int()
    alt4_B_cs5 = int()
    alt4_C_cs5 = int()

    # Choice Set 6
    # Alternative 1
    alt1_A_cs6 = int()
    alt1_B_cs6 = int()
    alt1_C_cs6 = int()
    alt1_D_cs6 = int()
    # Alternative 2
    alt2_A_cs6 = int()
    alt2_B_cs6 = int()
    alt2_C_cs6 = int()
    alt2_D_cs6 = int()
    # Alternative 3
    alt3_A_cs6 = int()
    alt3_B_cs6 = int()
    alt3_C_cs6 = int()
    # Alternative 4
    alt4_A_cs6 = int()
    alt4_B_cs6 = int()
    alt4_C_cs6 = int()

    # Choice Set 7
    # Alternative 1
    alt1_A_cs7 = int()
    alt1_B_cs7 = int()
    alt1_C_cs7 = int()
    alt1_D_cs7 = int()
    # Alternative 2
    alt2_A_cs7 = int()
    alt2_B_cs7 = int()
    alt2_C_cs7 = int()
    alt2_D_cs7 = int()
    # Alternative 3
    alt3_A_cs7 = int()
    alt3_B_cs7 = int()
    alt3_C_cs7 = int()
    # Alternative 4
    alt4_A_cs7 = int()
    alt4_B_cs7 = int()
    alt4_C_cs7 = int()

    # Choice Set 8
    # Alternative 1
    alt1_A_cs8 = int()
    alt1_B_cs8 = int()
    alt1_C_cs8 = int()
    alt1_D_cs8 = int()
    # Alternative 2
    alt2_A_cs8 = int()
    alt2_B_cs8 = int()
    alt2_C_cs8 = int()
    alt2_D_cs8 = int()
    # Alternative 3
    alt3_A_cs8 = int()
    alt3_B_cs8 = int()
    alt3_C_cs8 = int()
    # Alternative 4
    alt4_A_cs8 = int()
    alt4_B_cs8 = int()
    alt4_C_cs8 = int()

#displayed values choice sets

    # Choice Set 1

    # Alternative 1
    value_alt1_A_cs1 = int()
    value_alt1_B_cs1 = int()
    value_alt1_C_cs1 = int()
    value_alt1_D_cs1 = int()
    # Alternative 2
    value_alt2_A_cs1 = int()
    value_alt2_B_cs1 = int()
    value_alt2_C_cs1 = int()
    value_alt2_D_cs1 = int()
    # Alternative 3
    value_alt3_A_cs1 = int()
    value_alt3_B_cs1 = int()
    value_alt3_C_cs1 = int()
    # Alternative 4
    value_alt4_A_cs1 = int()
    value_alt4_B_cs1 = int()
    value_alt4_C_cs1 = int()

    # Choice Set 2
    # Alternative 1
    value_alt1_A_cs2 = int()
    value_alt1_B_cs2 = int()
    value_alt1_C_cs2 = int()
    value_alt1_D_cs2 = int()
    # Alternative 2
    value_alt2_A_cs2 = int()
    value_alt2_B_cs2 = int()
    value_alt2_C_cs2 = int()
    value_alt2_D_cs2 = int()
    # Alternative 3
    value_alt3_A_cs2 = int()
    value_alt3_B_cs2 = int()
    value_alt3_C_cs2 = int()
    # Alternative 4
    value_alt4_A_cs2 = int()
    value_alt4_B_cs2 = int()
    value_alt4_C_cs2 = int()

    # Choice Set 3
    # Alternative 1
    value_alt1_A_cs3 = int()
    value_alt1_B_cs3 = int()
    value_alt1_C_cs3 = int()
    value_alt1_D_cs3 = int()
    # Alternative 2
    value_alt2_A_cs3 = int()
    value_alt2_B_cs3 = int()
    value_alt2_C_cs3 = int()
    value_alt2_D_cs3 = int()
    # Alternative 3
    value_alt3_A_cs3 = int()
    value_alt3_B_cs3 = int()
    value_alt3_C_cs3 = int()
    # Alternative 4
    value_alt4_A_cs3 = int()
    value_alt4_B_cs3 = int()
    value_alt4_C_cs3 = int()

    # Choice Set 4
    # Alternative 1
    value_alt1_A_cs4 = int()
    value_alt1_B_cs4 = int()
    value_alt1_C_cs4 = int()
    value_alt1_D_cs4 = int()
    # Alternative 2
    value_alt2_A_cs4 = int()
    value_alt2_B_cs4 = int()
    value_alt2_C_cs4 = int()
    value_alt2_D_cs4 = int()
    # Alternative 3
    value_alt3_A_cs4 = int()
    value_alt3_B_cs4 = int()
    value_alt3_C_cs4 = int()
    # Alternative 4
    value_alt4_A_cs4 = int()
    value_alt4_B_cs4 = int()
    value_alt4_C_cs4 = int()

    # Choice Set 5
    # Alternative 1
    value_alt1_A_cs5 = int()
    value_alt1_B_cs5 = int()
    value_alt1_C_cs5 = int()
    value_alt1_D_cs5 = int()
    # Alternative 2
    value_alt2_A_cs5 = int()
    value_alt2_B_cs5 = int()
    value_alt2_C_cs5 = int()
    value_alt2_D_cs5 = int()
    # Alternative 3
    value_alt3_A_cs5 = int()
    value_alt3_B_cs5 = int()
    value_alt3_C_cs5 = int()
    # Alternative 4
    value_alt4_A_cs5 = int()
    value_alt4_B_cs5 = int()
    value_alt4_C_cs5 = int()

    # Choice Set 6
    # Alternative 1
    value_alt1_A_cs6 = int()
    value_alt1_B_cs6 = int()
    value_alt1_C_cs6 = int()
    value_alt1_D_cs6 = int()
    # Alternative 2
    value_alt2_A_cs6 = int()
    value_alt2_B_cs6 = int()
    value_alt2_C_cs6 = int()
    value_alt2_D_cs6 = int()
    # Alternative 3
    value_alt3_A_cs6 = int()
    value_alt3_B_cs6 = int()
    value_alt3_C_cs6 = int()
    # Alternative 4
    value_alt4_A_cs6 = int()
    value_alt4_B_cs6 = int()
    value_alt4_C_cs6 = int()

    # Choice Set 7
    # Alternative 1
    value_alt1_A_cs7 = int()
    value_alt1_B_cs7 = int()
    value_alt1_C_cs7 = int()
    value_alt1_D_cs7 = int()
    # Alternative 2
    value_alt2_A_cs7 = int()
    value_alt2_B_cs7 = int()
    value_alt2_C_cs7 = int()
    value_alt2_D_cs7 = int()
    # Alternative 3
    value_alt3_A_cs7 = int()
    value_alt3_B_cs7 = int()
    value_alt3_C_cs7 = int()
    # Alternative 4
    value_alt4_A_cs7 = int()
    value_alt4_B_cs7 = int()
    value_alt4_C_cs7 = int()

    # Choice Set 8
    # Alternative 1
    value_alt1_A_cs8 = int()
    value_alt1_B_cs8 = int()
    value_alt1_C_cs8 = int()
    value_alt1_D_cs8 = int()
    # Alternative 2
    value_alt2_A_cs8 = int()
    value_alt2_B_cs8 = int()
    value_alt2_C_cs8 = int()
    value_alt2_D_cs8 = int()
    # Alternative 3
    value_alt3_A_cs8 = int()
    value_alt3_B_cs8 = int()
    value_alt3_C_cs8 = int()
    # Alternative 4
    value_alt4_A_cs8 = int()
    value_alt4_B_cs8 = int()
    value_alt4_C_cs8 = int()



#####
# display if not master player
####
def display_group(player: Player):
    if player.participant.session.num_participants % 2 == 1:
        if player.participant.id_in_session == player.participant.session.num_participants:
            return False
        else:
            return True
    else:
        return True

# PAGES
class ChoiceSet1Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    #form_fields = ['value_alt1_A_cs1','value_alt1_B_cs1','value_alt1_C_cs1','value_alt1_D_cs1','value_alt2_A_cs1','value_alt2_B_cs1','value_alt2_C_cs1','value_alt2_D_cs1','value_alt3_A_cs1','value_alt3_B_cs1','value_alt3_C_cs1','value_alt4_A_cs1','value_alt4_B_cs1','value_alt4_C_cs1']
    form_fields = ['choice_cs1']

    pass

class Wait(WaitPage):
    wait_for_all_groups = True
    title_text = "Lindako!"
    body_text = ""

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        pass


class BreakpointPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not display_group(player)

    form_model = 'player'
    form_fields = ['code_breakpoint']
    pass


page_sequence = [
    ChoiceSet1Left
]


def set_choice_set_1(p: Player):
    choice_set = p.choice_set_1

    # Alternative 1
    p.alt1_A_cs1 = int(choice_set['alt1_A'])
    p.alt1_B_cs1 = int(choice_set['alt1_B'])
    p.alt1_C_cs1 = int(choice_set['alt1_C'])
    p.alt1_D_cs1 = int(choice_set['alt1_D'])
    # Alternative 2
    p.alt2_A_cs1 = int(choice_set['alt2_A'])
    p.alt2_B_cs1 = int(choice_set['alt2_B'])
    p.alt2_C_cs1 = int(choice_set['alt2_C'])
    p.alt2_D_cs1 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs1 = int(choice_set['alt3_A'])
    p.alt3_B_cs1 = int(choice_set['alt3_B'])
    p.alt3_C_cs1 = int(choice_set['alt3_C'])
    # Alternative 4
    p.alt4_A_cs1 = int(choice_set['alt4_A'])
    p.alt4_B_cs1 = int(choice_set['alt4_B'])
    p.alt4_C_cs1 = int(choice_set['alt4_C'])

def set_choice_set_2(p:Player):
	choice_set=p.choice_set_2

	# Alternative 1
	p.alt1_A_cs2 = int(choice_set['alt1_A'])
	p.alt1_B_cs2 = int(choice_set['alt1_B'])
	p.alt1_C_cs2 = int(choice_set['alt1_C'])
	p.alt1_D_cs2 = int(choice_set['alt1_D'])
	# Alternative 2
	p.alt2_A_cs2 = int(choice_set['alt2_A'])
	p.alt2_B_cs2 = int(choice_set['alt2_B'])
	p.alt2_C_cs2 = int(choice_set['alt2_C'])
	p.alt2_D_cs2 = int(choice_set['alt2_D'])
	# Alternative 3
	p.alt3_A_cs2 = int(choice_set['alt3_A'])
	p.alt3_B_cs2 = int(choice_set['alt3_B'])
	p.alt3_C_cs2 = int(choice_set['alt3_C'])
	# Alternative 4
	p.alt4_A_cs2 = int(choice_set['alt4_A'])
	p.alt4_B_cs2 = int(choice_set['alt4_B'])
	p.alt4_C_cs2 = int(choice_set['alt4_C'])


def set_choice_set_3(p:Player):
	#Choice Set 3
	choice_set=p.choice_set_3
	# Alternative 1
	p.alt1_A_cs3 = int(choice_set['alt1_A'])
	p.alt1_B_cs3 = int(choice_set['alt1_B'])
	p.alt1_C_cs3 = int(choice_set['alt1_C'])
	p.alt1_D_cs3 = int(choice_set['alt1_D'])
	# Alternative 2
	p.alt2_A_cs3 = int(choice_set['alt2_A'])
	p.alt2_B_cs3 = int(choice_set['alt2_B'])
	p.alt2_C_cs3 = int(choice_set['alt2_C'])
	p.alt2_D_cs3 = int(choice_set['alt2_D'])
	# Alternative 3
	p.alt3_A_cs3 = int(choice_set['alt3_A'])
	p.alt3_B_cs3 = int(choice_set['alt3_B'])
	p.alt3_C_cs3 = int(choice_set['alt3_C'])
	# Alternative 4
	p.alt4_A_cs3 = int(choice_set['alt4_A'])
	p.alt4_B_cs3 = int(choice_set['alt4_B'])
	p.alt4_C_cs3 = int(choice_set['alt4_C'])


def set_choice_set_4(p: Player):
    # Choice Set 4
    choice_set = p.choice_set_4

    # Alternative 1
    p.alt1_A_cs4 = int(choice_set['alt1_A'])
    p.alt1_B_cs4 = int(choice_set['alt1_B'])
    p.alt1_C_cs4 = int(choice_set['alt1_C'])
    p.alt1_D_cs4 = int(choice_set['alt1_D'])
    # Alternative 2
    p.alt2_A_cs4 = int(choice_set['alt2_A'])
    p.alt2_B_cs4 = int(choice_set['alt2_B'])
    p.alt2_C_cs4 = int(choice_set['alt2_C'])
    p.alt2_D_cs4 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs4 = int(choice_set['alt3_A'])
    p.alt3_B_cs4 = int(choice_set['alt3_B'])
    p.alt3_C_cs4 = int(choice_set['alt3_C'])
    # Alternative 4
    p.alt4_A_cs4 = int(choice_set['alt4_A'])
    p.alt4_B_cs4 = int(choice_set['alt4_B'])
    p.alt4_C_cs4 = int(choice_set['alt4_C'])


def set_choice_set_5(p: Player):
    # Choice Set 5
    choice_set = p.choice_set_5
    # Alternative 1
    p.alt1_A_cs5 = int(choice_set['alt1_A'])
    p.alt1_B_cs5 = int(choice_set['alt1_B'])
    p.alt1_C_cs5 = int(choice_set['alt1_C'])
    p.alt1_D_cs5 = int(choice_set['alt1_D'])
    # Alternative 2
    p.alt2_A_cs5 = int(choice_set['alt2_A'])
    p.alt2_B_cs5 = int(choice_set['alt2_B'])
    p.alt2_C_cs5 = int(choice_set['alt2_C'])
    p.alt2_D_cs5 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs5 = int(choice_set['alt3_A'])
    p.alt3_B_cs5 = int(choice_set['alt3_B'])
    p.alt3_C_cs5 = int(choice_set['alt3_C'])
    # Alternative 4
    p.alt4_A_cs5 = int(choice_set['alt4_A'])
    p.alt4_B_cs5 = int(choice_set['alt4_B'])
    p.alt4_C_cs5 = int(choice_set['alt4_C'])


def set_choice_set_6(p: Player):
    # Choice Set 6
    choice_set = p.choice_set_6

    # Choice Set 6
    # Alternative 1
    p.alt1_A_cs6 = int(choice_set['alt1_A'])
    p.alt1_B_cs6 = int(choice_set['alt1_B'])
    p.alt1_C_cs6 = int(choice_set['alt1_C'])
    p.alt1_D_cs6 = int(choice_set['alt1_D'])
     # Alternative 2
    p.alt2_A_cs6 = int(choice_set['alt2_A'])
    p.alt2_B_cs6 = int(choice_set['alt2_B'])
    p.alt2_C_cs6 = int(choice_set['alt2_C'])
    p.alt2_D_cs6 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs6 = int(choice_set['alt3_A'])
    p.alt3_B_cs6 = int(choice_set['alt3_B'])
    p.alt3_C_cs6 = int(choice_set['alt3_C'])
     # Alternative 4
    p.alt4_A_cs6 = int(choice_set['alt4_A'])
    p.alt4_B_cs6 = int(choice_set['alt4_B'])
    p.alt4_C_cs6 = int(choice_set['alt4_C'])


def set_choice_set_7(p: Player):
    # Choice Set 7
    choice_set = p.choice_set_7
    # Choice Set 7
    # Alternative 1
    p.alt1_A_cs7 = int(choice_set['alt1_A'])
    p.alt1_B_cs7 = int(choice_set['alt1_B'])
    p.alt1_C_cs7 = int(choice_set['alt1_C'])
    p.alt1_D_cs7 = int(choice_set['alt1_D'])
    # Alternative 2
    p.alt2_A_cs7 = int(choice_set['alt2_A'])
    p.alt2_B_cs7 = int(choice_set['alt2_B'])
    p.alt2_C_cs7 = int(choice_set['alt2_C'])
    p.alt2_D_cs7 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs7 = int(choice_set['alt3_A'])
    p.alt3_B_cs7 = int(choice_set['alt3_B'])
    p.alt3_C_cs7 = int(choice_set['alt3_C'])
    # Alternative 4
    p.alt4_A_cs7 = int(choice_set['alt4_A'])
    p.alt4_B_cs7 = int(choice_set['alt4_B'])
    p.alt4_C_cs7 = int(choice_set['alt4_C'])


def set_choice_set_8(p: Player):
    # Choice Set 8
    choice_set = p.choice_set_8

    # Choice Set 8

    # Alternative 1
    p.alt1_A_cs8 = int(choice_set['alt1_A'])
    p.alt1_B_cs8 = int(choice_set['alt1_B'])
    p.alt1_C_cs8 = int(choice_set['alt1_C'])
    p.alt1_D_cs8 = int(choice_set['alt1_D'])
    # Alternative 2
    p.alt2_A_cs8 = int(choice_set['alt2_A'])
    p.alt2_B_cs8 = int(choice_set['alt2_B'])
    p.alt2_C_cs8 = int(choice_set['alt2_C'])
    p.alt2_D_cs8 = int(choice_set['alt2_D'])
    # Alternative 3
    p.alt3_A_cs8 = int(choice_set['alt3_A'])
    p.alt3_B_cs8 = int(choice_set['alt3_B'])
    p.alt3_C_cs8 = int(choice_set['alt3_C'])
    # Alternative 4
    p.alt4_A_cs8 = int(choice_set['alt4_A'])
    p.alt4_B_cs8 = int(choice_set['alt4_B'])
    p.alt4_C_cs8 = int(choice_set['alt4_C'])

def set_choice_value_1(p: Player):
    choice_set = p.choice_set_1

    # Alternative 1
    p.value_alt1_A_cs1 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs1 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs1 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs1 = value_election(int(choice_set['alt1_D']))
    # Alternative 2
    p.value_alt2_A_cs1 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs1 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs1 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs1 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs1 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs1 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs1 = value_corruption(int(choice_set['alt3_C']))
    # Alternative 4
    p.value_alt4_A_cs1 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs1 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs1 = value_corruption(int(choice_set['alt4_C']))

def set_choice_value_2(p:Player):
	choice_set=p.choice_set_2

	# Alternative 1
	p.value_alt1_A_cs2 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
	p.value_alt1_B_cs2 = value_detection(int(choice_set['alt1_B']))
	p.value_alt1_C_cs2 = value_corruption(int(choice_set['alt1_C']))
	p.value_alt1_D_cs2 = value_election(int(choice_set['alt1_D']))
	# Alternative 2
	p.value_alt2_A_cs2 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
	p.value_alt2_B_cs2 = value_detection(int(choice_set['alt2_B']))
	p.value_alt2_C_cs2 = value_corruption(int(choice_set['alt2_C']))
	p.value_alt2_D_cs2 = value_election(int(choice_set['alt2_D']))
	# Alternative 3
	p.value_alt3_A_cs2 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
	p.value_alt3_B_cs2 = value_detection(int(choice_set['alt3_B']))
	p.value_alt3_C_cs2 = value_corruption(int(choice_set['alt3_C']))
	# Alternative 4
	p.value_alt4_A_cs2 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
	p.value_alt4_B_cs2 = value_detection(int(choice_set['alt4_B']))
	p.value_alt4_C_cs2 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_3(p:Player):
	#Choice Set 3
	choice_set=p.choice_set_3
	# Alternative 1
	p.value_alt1_A_cs3 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
	p.value_alt1_B_cs3 = value_detection(int(choice_set['alt1_B']))
	p.value_alt1_C_cs3 = value_corruption(int(choice_set['alt1_C']))
	p.value_alt1_D_cs3 = value_election(int(choice_set['alt1_D']))
	# Alternative 2
	p.value_alt2_A_cs3 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
	p.value_alt2_B_cs3 = value_detection(int(choice_set['alt2_B']))
	p.value_alt2_C_cs3 = value_corruption(int(choice_set['alt2_C']))
	p.value_alt2_D_cs3 = value_election(int(choice_set['alt2_D']))
	# Alternative 3
	p.value_alt3_A_cs3 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
	p.value_alt3_B_cs3 = value_detection(int(choice_set['alt3_B']))
	p.value_alt3_C_cs3 = value_corruption(int(choice_set['alt3_C']))
	# Alternative 4
	p.value_alt4_A_cs3 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
	p.value_alt4_B_cs3 = value_detection(int(choice_set['alt4_B']))
	p.value_alt4_C_cs3 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_4(p: Player):
    # Choice Set 4
    choice_set = p.choice_set_4

    # Alternative 1
    p.value_alt1_A_cs4 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs4 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs4 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs4 = value_election(int(choice_set['alt1_D']))
    # Alternative 2
    p.value_alt2_A_cs4 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs4 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs4 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs4 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs4 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs4 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs4 = value_corruption(int(choice_set['alt3_C']))
    # Alternative 4
    p.value_alt4_A_cs4 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs4 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs4 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_5(p: Player):
    # Choice Set 5
    choice_set = p.choice_set_5
    # Alternative 1
    p.value_alt1_A_cs5 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs5 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs5 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs5 = value_election(int(choice_set['alt1_D']))
    # Alternative 2
    p.value_alt2_A_cs5 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs5 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs5 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs5 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs5 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs5 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs5 = value_corruption(int(choice_set['alt3_C']))
    # Alternative 4
    p.value_alt4_A_cs5 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs5 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs5 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_6(p: Player):
    # Choice Set 6
    choice_set = p.choice_set_6

    # Choice Set 6
    # Alternative 1
    p.value_alt1_A_cs6 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs6 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs6 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs6 = value_election(int(choice_set['alt1_D']))
     # Alternative 2
    p.value_alt2_A_cs6 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs6 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs6 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs6 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs6 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs6 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs6 = value_corruption(int(choice_set['alt3_C']))
     # Alternative 4
    p.value_alt4_A_cs6 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs6 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs6 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_7(p: Player):
    # Choice Set 7
    choice_set = p.choice_set_7
    # Choice Set 7
    # Alternative 1
    p.value_alt1_A_cs7 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs7 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs7 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs7 = value_election(int(choice_set['alt1_D']))
    # Alternative 2
    p.value_alt2_A_cs7 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs7 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs7 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs7 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs7 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs7 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs7 = value_corruption(int(choice_set['alt3_C']))
    # Alternative 4
    p.value_alt4_A_cs7 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs7 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs7 = value_corruption(int(choice_set['alt4_C']))


def set_choice_value_8(p: Player):
    # Choice Set 8
    choice_set = p.choice_set_8

    # Choice Set 8

    # Alternative 1
    p.value_alt1_A_cs8 = value_price(int(choice_set['alt1_A']), p.yearly_payment)
    p.value_alt1_B_cs8 = value_detection(int(choice_set['alt1_B']))
    p.value_alt1_C_cs8 = value_corruption(int(choice_set['alt1_C']))
    p.value_alt1_D_cs8 = value_election(int(choice_set['alt1_D']))
    # Alternative 2
    p.value_alt2_A_cs8 = value_price(int(choice_set['alt2_A']), p.yearly_payment)
    p.value_alt2_B_cs8 = value_detection(int(choice_set['alt2_B']))
    p.value_alt2_C_cs8 = value_corruption(int(choice_set['alt2_C']))
    p.value_alt2_D_cs8 = value_election(int(choice_set['alt2_D']))
    # Alternative 3
    p.value_alt3_A_cs8 = value_price(int(choice_set['alt3_A']), p.yearly_payment)
    p.value_alt3_B_cs8 = value_detection(int(choice_set['alt3_B']))
    p.value_alt3_C_cs8 = value_corruption(int(choice_set['alt3_C']))
    # Alternative 4
    p.value_alt4_A_cs8 = value_price(int(choice_set['alt4_A']), p.yearly_payment)
    p.value_alt4_B_cs8 = value_detection(int(choice_set['alt4_B']))
    p.value_alt4_C_cs8 = value_corruption(int(choice_set['alt4_C']))


def value_price(percent: int, fee:int):
    price=percent*0.01*fee
    currency = C.LOCAL_CURRENCY
    return currency+str(price)

def value_detection(rate: int):
    return str(rate+ " %")

def value_corruption(indicator: int):
    if indicator==0:
        return C.NO_CORRUPTION
    elif indicator==1:
        return C.LOW_CORRUPTION
    elif indicator==2:
        return C.HIGH_CORRUPTION

def value_election(indicator:int):
    if indicator==0:
        return C.NO_ELECT
    elif indicator==1:
        return C.ELECT
