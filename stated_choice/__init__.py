import random

from otree.api import *
from otree.app_template.models import Player, Subsession

author = 'PDH'
doc = """
Your app description
"""

class C(BaseConstants):
    ###important links##
    csv_link = "stated_choice/static/optimal_design.csv"

    #######################################################################
    # game settings
    #######################################################################
    NAME_IN_URL = 'stated_choice'
    PLAYERS_PER_GROUP = None

    NUM_ROUNDS = 1

    ##translation
    NEXT = "Next"
    CHOICE = "Decision"

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

    WAIT="Lindako"

    #style of table (including button#
    STYLETABLE="<style> .otree-body {font-size: 1.5em;} table {width: 100 %;} tr {border-bottom: 1px solid #ddd;} th, td {border-right: 1px solid #ddd;padding: 10px;text-align: center;}th {background-color: #D6EEEE; width: 20%;} input[type=radio] {width: 100%;height: 2em;}</style>"





def creating_session(subsession: Subsession):

    set_treatment(subsession)
    optimal_design=get_stated_choice_list()
    subsession.session.vars['optimal_design']= optimal_design
    max_Block = get_max_Block(optimal_design)

    for p in subsession.get_players():
        p.participant.vars['all_choice_sets'] = list()
        i = int(p.participant.id_in_session)
        for row in optimal_design:
            if (subsession.treatment == "left_down" or subsession.treatment == "right_down") and int(row['Block'])==i:
                p.participant.vars['all_choice_sets'].append(row)
            elif (subsession.treatment == "left_up" or subsession.treatment == "right_up") and int(row['Block']) == max_Block+1-i:
                p.participant.vars['all_choice_sets'].append(row)
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
    if 'yearly_payment' in p.participant.vars:
        p.yearly_payment = p.participant.vars['yearly_payment']
    pass

def set_treatment(subsession: Subsession):
    if 'treatment' in subsession.session.config:
        subsession.treatment = subsession.session.config['treatment']
    pass

def set_stated_choice(p: Player):
    choice_sets =p.participant.vars['all_choice_sets']
    for j in range(len(choice_sets)):
        if j==0:
            p.participant.vars['choice_set_1'] =choice_sets[j]
            p.block=int(choice_sets[j]['Block'])
            set_choice_set_1(p)
            set_choice_value_1(p)

        elif j==1:
            p.participant.vars['choice_set_2'] =choice_sets[j]
            set_choice_set_2(p)
            set_choice_value_2(p)
        elif j==2:
            p.participant.vars['choice_set_3'] =choice_sets[j]
            set_choice_set_3(p)
            set_choice_value_3(p)
        elif j==3:
            p.participant.vars['choice_set_4'] =choice_sets[j]
            set_choice_set_4(p)
            set_choice_value_4(p)
        elif j==4:
            p.participant.vars['choice_set_5'] = choice_sets[j]
            set_choice_set_5(p)
            set_choice_value_5(p)
        elif j==5:
            p.participant.vars['choice_set_6'] = choice_sets[j]
            set_choice_set_6(p)
            set_choice_value_6(p)
        elif j==6:
            p.participant.vars['choice_set_7'] = choice_sets[j]
            set_choice_set_7(p)
            set_choice_value_7(p)
        elif j==7:
            p.participant.vars['choice_set_8'] = choice_sets[j]
            set_choice_set_8(p)
            set_choice_value_8(p)




    pass




class Subsession(BaseSubsession):
    treatment = models.StringField(initial='left_down')
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

    yearly_payment = models.IntegerField(initial=100000)
    #CHoices
    choice_cs1 = models.IntegerField(choices=[1, 2, 3, 4],widget=widgets.RadioSelect)
    choice_cs2 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs3 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs4 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs5 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs6 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs7 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    choice_cs8 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)

    #Alternative specific values
    # Choice Set 1
    block= models.IntegerField()

    # Alternative 1
    alt1_A_cs1 = models.IntegerField()
    alt1_B_cs1 = models.IntegerField()
    alt1_C_cs1 = models.IntegerField()
    alt1_D_cs1 = models.IntegerField()
    # Alternative 2
    alt2_A_cs1 = models.IntegerField()
    alt2_B_cs1 = models.IntegerField()
    alt2_C_cs1 = models.IntegerField()
    alt2_D_cs1 = models.IntegerField()
    # Alternative 3
    alt3_A_cs1 = models.IntegerField()
    alt3_B_cs1 = models.IntegerField()
    alt3_C_cs1 = models.IntegerField()
    # Alternative 4
    alt4_A_cs1 = models.IntegerField()
    alt4_B_cs1 = models.IntegerField()
    alt4_C_cs1 = models.IntegerField()

    # Choice Set 2
    # Alternative 1
    alt1_A_cs2 = models.IntegerField()
    alt1_B_cs2 = models.IntegerField()
    alt1_C_cs2 = models.IntegerField()
    alt1_D_cs2 = models.IntegerField()
    # Alternative 2
    alt2_A_cs2 = models.IntegerField()
    alt2_B_cs2 = models.IntegerField()
    alt2_C_cs2 = models.IntegerField()
    alt2_D_cs2 = models.IntegerField()
    # Alternative 3
    alt3_A_cs2 = models.IntegerField()
    alt3_B_cs2 = models.IntegerField()
    alt3_C_cs2 = models.IntegerField()
    # Alternative 4
    alt4_A_cs2 = models.IntegerField()
    alt4_B_cs2 = models.IntegerField()
    alt4_C_cs2 = models.IntegerField()

    # Choice Set 3
    # Alternative 1
    alt1_A_cs3 = models.IntegerField()
    alt1_B_cs3 = models.IntegerField()
    alt1_C_cs3 = models.IntegerField()
    alt1_D_cs3 = models.IntegerField()
    # Alternative 2
    alt2_A_cs3 = models.IntegerField()
    alt2_B_cs3 = models.IntegerField()
    alt2_C_cs3 = models.IntegerField()
    alt2_D_cs3 = models.IntegerField()
    # Alternative 3
    alt3_A_cs3 = models.IntegerField()
    alt3_B_cs3 = models.IntegerField()
    alt3_C_cs3 = models.IntegerField()
    # Alternative 4
    alt4_A_cs3 = models.IntegerField()
    alt4_B_cs3 = models.IntegerField()
    alt4_C_cs3 = models.IntegerField()

    # Choice Set 4
    # Alternative 1
    alt1_A_cs4 = models.IntegerField()
    alt1_B_cs4 = models.IntegerField()
    alt1_C_cs4 = models.IntegerField()
    alt1_D_cs4 = models.IntegerField()
    # Alternative 2
    alt2_A_cs4 = models.IntegerField()
    alt2_B_cs4 = models.IntegerField()
    alt2_C_cs4 = models.IntegerField()
    alt2_D_cs4 = models.IntegerField()
    # Alternative 3
    alt3_A_cs4 = models.IntegerField()
    alt3_B_cs4 = models.IntegerField()
    alt3_C_cs4 = models.IntegerField()
    # Alternative 4
    alt4_A_cs4 = models.IntegerField()
    alt4_B_cs4 = models.IntegerField()
    alt4_C_cs4 = models.IntegerField()

    # Choice Set 5
    # Alternative 1
    alt1_A_cs5 = models.IntegerField()
    alt1_B_cs5 = models.IntegerField()
    alt1_C_cs5 = models.IntegerField()
    alt1_D_cs5 = models.IntegerField()
    # Alternative 2
    alt2_A_cs5 = models.IntegerField()
    alt2_B_cs5 = models.IntegerField()
    alt2_C_cs5 = models.IntegerField()
    alt2_D_cs5 = models.IntegerField()
    # Alternative 3
    alt3_A_cs5 = models.IntegerField()
    alt3_B_cs5 = models.IntegerField()
    alt3_C_cs5 = models.IntegerField()
    # Alternative 4
    alt4_A_cs5 = models.IntegerField()
    alt4_B_cs5 = models.IntegerField()
    alt4_C_cs5 = models.IntegerField()

    # Choice Set 6
    # Alternative 1
    alt1_A_cs6 = models.IntegerField()
    alt1_B_cs6 = models.IntegerField()
    alt1_C_cs6 = models.IntegerField()
    alt1_D_cs6 = models.IntegerField()
    # Alternative 2
    alt2_A_cs6 = models.IntegerField()
    alt2_B_cs6 = models.IntegerField()
    alt2_C_cs6 = models.IntegerField()
    alt2_D_cs6 = models.IntegerField()
    # Alternative 3
    alt3_A_cs6 = models.IntegerField()
    alt3_B_cs6 = models.IntegerField()
    alt3_C_cs6 = models.IntegerField()
    # Alternative 4
    alt4_A_cs6 = models.IntegerField()
    alt4_B_cs6 = models.IntegerField()
    alt4_C_cs6 = models.IntegerField()

    # Choice Set 7
    # Alternative 1
    alt1_A_cs7 = models.IntegerField()
    alt1_B_cs7 = models.IntegerField()
    alt1_C_cs7 = models.IntegerField()
    alt1_D_cs7 = models.IntegerField()
    # Alternative 2
    alt2_A_cs7 = models.IntegerField()
    alt2_B_cs7 = models.IntegerField()
    alt2_C_cs7 = models.IntegerField()
    alt2_D_cs7 = models.IntegerField()
    # Alternative 3
    alt3_A_cs7 = models.IntegerField()
    alt3_B_cs7 = models.IntegerField()
    alt3_C_cs7 = models.IntegerField()
    # Alternative 4
    alt4_A_cs7 = models.IntegerField()
    alt4_B_cs7 = models.IntegerField()
    alt4_C_cs7 = models.IntegerField()

    # Choice Set 8
    # Alternative 1
    alt1_A_cs8 = models.IntegerField()
    alt1_B_cs8 = models.IntegerField()
    alt1_C_cs8 = models.IntegerField()
    alt1_D_cs8 = models.IntegerField()
    # Alternative 2
    alt2_A_cs8 = models.IntegerField()
    alt2_B_cs8 = models.IntegerField()
    alt2_C_cs8 = models.IntegerField()
    alt2_D_cs8 = models.IntegerField()
    # Alternative 3
    alt3_A_cs8 = models.IntegerField()
    alt3_B_cs8 = models.IntegerField()
    alt3_C_cs8 = models.IntegerField()
    # Alternative 4
    alt4_A_cs8 = models.IntegerField()
    alt4_B_cs8 = models.IntegerField()
    alt4_C_cs8 = models.IntegerField()

#displayed values choice sets

    # Choice Set 1

    # Alternative 1
    value_alt1_A_cs1 = models.StringField()
    value_alt1_B_cs1 = models.StringField()
    value_alt1_C_cs1 = models.StringField()
    value_alt1_D_cs1 = models.StringField()
    # Alternative 2
    value_alt2_A_cs1 = models.StringField()
    value_alt2_B_cs1 = models.StringField()
    value_alt2_C_cs1 = models.StringField()
    value_alt2_D_cs1 = models.StringField()
    # Alternative 3
    value_alt3_A_cs1 = models.StringField()
    value_alt3_B_cs1 = models.StringField()
    value_alt3_C_cs1 = models.StringField()
    # Alternative 4
    value_alt4_A_cs1 = models.StringField()
    value_alt4_B_cs1 = models.StringField()
    value_alt4_C_cs1 = models.StringField()

    # Choice Set 2
    # Alternative 1
    value_alt1_A_cs2 = models.StringField()
    value_alt1_B_cs2 = models.StringField()
    value_alt1_C_cs2 = models.StringField()
    value_alt1_D_cs2 = models.StringField()
    # Alternative 2
    value_alt2_A_cs2 = models.StringField()
    value_alt2_B_cs2 = models.StringField()
    value_alt2_C_cs2 = models.StringField()
    value_alt2_D_cs2 = models.StringField()
    # Alternative 3
    value_alt3_A_cs2 = models.StringField()
    value_alt3_B_cs2 = models.StringField()
    value_alt3_C_cs2 = models.StringField()
    # Alternative 4
    value_alt4_A_cs2 = models.StringField()
    value_alt4_B_cs2 = models.StringField()
    value_alt4_C_cs2 = models.StringField()

    # Choice Set 3
    # Alternative 1
    value_alt1_A_cs3 = models.StringField()
    value_alt1_B_cs3 = models.StringField()
    value_alt1_C_cs3 = models.StringField()
    value_alt1_D_cs3 = models.StringField()
    # Alternative 2
    value_alt2_A_cs3 = models.StringField()
    value_alt2_B_cs3 = models.StringField()
    value_alt2_C_cs3 = models.StringField()
    value_alt2_D_cs3 = models.StringField()
    # Alternative 3
    value_alt3_A_cs3 = models.StringField()
    value_alt3_B_cs3 = models.StringField()
    value_alt3_C_cs3 = models.StringField()
    # Alternative 4
    value_alt4_A_cs3 = models.StringField()
    value_alt4_B_cs3 = models.StringField()
    value_alt4_C_cs3 = models.StringField()

    # Choice Set 4
    # Alternative 1
    value_alt1_A_cs4 = models.StringField()
    value_alt1_B_cs4 = models.StringField()
    value_alt1_C_cs4 = models.StringField()
    value_alt1_D_cs4 = models.StringField()
    # Alternative 2
    value_alt2_A_cs4 = models.StringField()
    value_alt2_B_cs4 = models.StringField()
    value_alt2_C_cs4 = models.StringField()
    value_alt2_D_cs4 = models.StringField()
    # Alternative 3
    value_alt3_A_cs4 = models.StringField()
    value_alt3_B_cs4 = models.StringField()
    value_alt3_C_cs4 = models.StringField()
    # Alternative 4
    value_alt4_A_cs4 = models.StringField()
    value_alt4_B_cs4 = models.StringField()
    value_alt4_C_cs4 = models.StringField()

    # Choice Set 5
    # Alternative 1
    value_alt1_A_cs5 = models.StringField()
    value_alt1_B_cs5 = models.StringField()
    value_alt1_C_cs5 = models.StringField()
    value_alt1_D_cs5 = models.StringField()
    # Alternative 2
    value_alt2_A_cs5 = models.StringField()
    value_alt2_B_cs5 = models.StringField()
    value_alt2_C_cs5 = models.StringField()
    value_alt2_D_cs5 = models.StringField()
    # Alternative 3
    value_alt3_A_cs5 = models.StringField()
    value_alt3_B_cs5 = models.StringField()
    value_alt3_C_cs5 = models.StringField()
    # Alternative 4
    value_alt4_A_cs5 = models.StringField()
    value_alt4_B_cs5 = models.StringField()
    value_alt4_C_cs5 = models.StringField()

    # Choice Set 6
    # Alternative 1
    value_alt1_A_cs6 = models.StringField()
    value_alt1_B_cs6 = models.StringField()
    value_alt1_C_cs6 = models.StringField()
    value_alt1_D_cs6 = models.StringField()
    # Alternative 2
    value_alt2_A_cs6 = models.StringField()
    value_alt2_B_cs6 = models.StringField()
    value_alt2_C_cs6 = models.StringField()
    value_alt2_D_cs6 = models.StringField()
    # Alternative 3
    value_alt3_A_cs6 = models.StringField()
    value_alt3_B_cs6 = models.StringField()
    value_alt3_C_cs6 = models.StringField()
    # Alternative 4
    value_alt4_A_cs6 = models.StringField()
    value_alt4_B_cs6 = models.StringField()
    value_alt4_C_cs6 = models.StringField()

    # Choice Set 7
    # Alternative 1
    value_alt1_A_cs7 = models.StringField()
    value_alt1_B_cs7 = models.StringField()
    value_alt1_C_cs7 = models.StringField()
    value_alt1_D_cs7 = models.StringField()
    # Alternative 2
    value_alt2_A_cs7 = models.StringField()
    value_alt2_B_cs7 = models.StringField()
    value_alt2_C_cs7 = models.StringField()
    value_alt2_D_cs7 = models.StringField()
    # Alternative 3
    value_alt3_A_cs7 = models.StringField()
    value_alt3_B_cs7 = models.StringField()
    value_alt3_C_cs7 = models.StringField()
    # Alternative 4
    value_alt4_A_cs7 = models.StringField()
    value_alt4_B_cs7 = models.StringField()
    value_alt4_C_cs7 = models.StringField()

    # Choice Set 8
    # Alternative 1
    value_alt1_A_cs8 = models.StringField()
    value_alt1_B_cs8 = models.StringField()
    value_alt1_C_cs8 = models.StringField()
    value_alt1_D_cs8 = models.StringField()
    # Alternative 2
    value_alt2_A_cs8 = models.StringField()
    value_alt2_B_cs8 = models.StringField()
    value_alt2_C_cs8 = models.StringField()
    value_alt2_D_cs8 = models.StringField()
    # Alternative 3
    value_alt3_A_cs8 = models.StringField()
    value_alt3_B_cs8 = models.StringField()
    value_alt3_C_cs8 = models.StringField()
    # Alternative 4
    value_alt4_A_cs8 = models.StringField()
    value_alt4_B_cs8 = models.StringField()
    value_alt4_C_cs8 = models.StringField()



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
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up" ):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else: return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs1']

    pass
class ChoiceSet1Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs1']

    pass
class ChoiceSet2Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs2']

    pass
class ChoiceSet2Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs2']

    pass

class ChoiceSet3Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs3']

    pass
class ChoiceSet3Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs3']

    pass

class ChoiceSet4Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs4']

    pass
class ChoiceSet4Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs4']

    pass
class ChoiceSet5Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs5']

    pass
class ChoiceSet5Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs5']

class ChoiceSet6Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs6']

    pass
class ChoiceSet6Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs6']

    pass

class ChoiceSet7Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs7']

    pass
class ChoiceSet7Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs7']

    pass
class ChoiceSet8Left(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return True
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return False
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs8']

    pass
class ChoiceSet8Right(Page):
    @staticmethod
    def is_displayed(player: Player):
        if display_group(player):
            if (player.subsession.treatment == "left_down" or player.subsession.treatment == "left_up"):
                return False
            elif (player.subsession.treatment == "right_down" or player.subsession.treatment == "right_up"):
                return True
        else:
            return display_group(player)

    form_model = 'player'
    form_fields = ['choice_cs8']

    pass



class WaitStartChoice(WaitPage):
    wait_for_all_groups = True
    title_text = C.WAIT
    body_text = ""

    def after_all_players_arrive(subsession: Subsession):
        for p in subsession.get_players():
            input_from_previous_games(p)
            set_stated_choice(p)
        pass




page_sequence = [
    WaitStartChoice,
    ChoiceSet1Left,
    ChoiceSet1Right,
    ChoiceSet2Left,
    ChoiceSet2Right,
    ChoiceSet3Left,
    ChoiceSet3Right,
    ChoiceSet4Left,
    ChoiceSet4Right,
    ChoiceSet5Left,
    ChoiceSet5Right,
    ChoiceSet6Left,
    ChoiceSet6Right,
    ChoiceSet7Left,
    ChoiceSet7Right,
    ChoiceSet8Left,
    ChoiceSet8Right

]


def set_choice_set_1(p: Player):
    choice_set = p.participant.vars['choice_set_1']

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
	choice_set=p.participant.vars['choice_set_2']

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
	choice_set=p.participant.vars['choice_set_3']
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
    choice_set = p.participant.vars['choice_set_4']

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
    choice_set = p.participant.vars['choice_set_5']
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
    choice_set = p.participant.vars['choice_set_6']

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
    choice_set = p.participant.vars['choice_set_7']
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
    choice_set = p.participant.vars['choice_set_8']

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
    choice_set = p.participant.vars['choice_set_1']

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
	choice_set=p.participant.vars['choice_set_2']

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
	choice_set=p.participant.vars['choice_set_3']
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
    choice_set = p.participant.vars['choice_set_4']

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
    choice_set = p.participant.vars['choice_set_5']
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
    choice_set = p.participant.vars['choice_set_6']

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
    choice_set = p.participant.vars['choice_set_7']
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
    choice_set = p.participant.vars['choice_set_8']

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
    price = percent*0.01*fee
    currency = C.LOCAL_CURRENCY
    return currency+" "+str(price)

def value_detection(rate: int):
    return str(rate)+ " %"

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
