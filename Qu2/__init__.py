import random

from otree.api import *
from otree.app_template.models import Player


author = 'PDH'
doc = """
Your app description
"""


class C(BaseConstants):
    #######################################################################
    # game settings
    #######################################################################
    # game is part of WP2A of the MultiTipProject
    NAME_IN_URL = 'Qu2'
    # groups are only attached in cas of information of each other
    PLAYERS_PER_GROUP = None
    # only 1 round with three phases ('event phase', 'information phase', investment phase')
    NUM_ROUNDS = 1

     #translation
    NEXT = "Next"
    WAIT = "Lindako"
    STYLE = "<style> .otree-body {font-size: 1.5em;} input.larger {transform: scale(1.5); margin: 5px;} </style>"
    YEARS = "years"
    CURRENCY = "UGX"
    TIMES = "times"
    NOT_WANT_TO_ANSWER= "I don't want to answer"

    ANSWER_ALL = "Answer all questions!"

    IDENTITY_INTRO= "In the next three questions, we ask you how much you identify with other people around you. This means feeling connected with others and being similar to others."

    SEVERITY_INTRO= "20. Based on your experience in the fishery, please rate how severe the following issues are for the earnings from fishing on Lake Victoria."

    WORRY_INTRO = "21. How much do the following things worry you?"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_much_field(**kwargs):
    ####
    # ident_field
    ###

    return models.CharField(
        choices=[
            ['0', '0 – Not at all'],
            ['1', '1 – very little'],
            ['2', '2 – a little'],
            ['3', '3 – somehow'],
            ['4', '4 - much'],
            ['5', '5 – Very much'],
            ['99', C.NOT_WANT_TO_ANSWER],
        ],
        blank=False,
        widget=widgets.RadioSelect,
        **kwargs,)

    pass



def make_yes_no_field(**kwargs):
    ####
    # Yes-No-Fields
    ###

    return models.CharField(
        choices=[
            ['yes', 'Yes'],
            ['no', 'No'],
            ['noanswer', C.NOT_WANT_TO_ANSWER]
        ],
        widget=widgets.RadioSelectHorizontal,
        **kwargs,)

    pass

def make_severity_field(**kwargs):
    ####
    # severity Fields
    ###

    return models.CharField(
        choices=[
            ['0', '0 – Not severe at all'],
            ['1', '1 - very unsevere'],
            ['2', '2 - moderately unsevere'],
            ['3', '3 - moderately severe'],
            ['4', '4 – very severe'],
            ['5', '5 – extremely severe'],
            ['99', C.NOT_WANT_TO_ANSWER],
        ],
        blank=False,
        widget=widgets.RadioSelect,
        **kwargs, )

    pass

def make_never_always_field(**kwargs):
    ####
    # severity Fields
    ###

    return models.CharField(
        choices=[
            ['0', '0 – never'],
            ['1', '1 – very few'],
            ['2', '2 – few times'],
            ['3', '3 - sometimes'],
            ['4', '4 - very often'],
            ['5', '5 – always'],
            ['99', C.NOT_WANT_TO_ANSWER],
        ],
        blank=False,
        widget=widgets.RadioSelect,
        **kwargs, )

    pass

def make_agree_field(**kwargs):
    ####
    # severity Fields
    ###

    return models.CharField(
        choices=[
            #['0', '0 – I totally disagree'],
            ['1', '1 - I strongly disagree'],
            ['2', '2 - I moderately disagree'],
            ['3', '3 - Undecided'],
            ['4', '4 - I moderately agree'],
            ['5', '5 – I strongly  agree'],
            #['5', '5 – I totally  agree'],
            ['99', C.NOT_WANT_TO_ANSWER],
        ],
        blank=False,
        widget=widgets.RadioSelect,
        **kwargs, )

    pass






class Player(BasePlayer):
    #Answer stated choice opinion
    #12. Who do you think is currently mainly responsible for the monitoring of fishers’ behavior?
    responsible_monitoring = models.CharField(
        label="12. Who do you think is currently mainly responsible for the monitoring of fishers’ behavior?",
        choices=[['landing', 'landing site management'],
                 ['local', 'Fisheries department on district level'],
                 ['national', 'National fisheries department in Entebbe (UG'],
                 ['military', 'National Fisheries Protection Unit (FPU)'],
                 ],
        widget=widgets.RadioSelect,
        blank=False,)
    # 13 Are you a member of the local beach management/landing site management?

    bmu_member = make_yes_no_field(label='Are you a member of the local landing site management?')

    # 14.What do you think is the current probability of being detected when using illegal gears?
    prob_detect = models.PositiveIntegerField(
        label='14.	What do you think is the current probability of being detected when using illegal gears?',
        blank=True,
        initial=None
    )
    prob_detect_na = models.BooleanField(blank=True, label=C.NOT_WANT_TO_ANSWER, initial=False)

    #15.In your opinion, how high is the current level of corruption by the law enforcement institutions at Lake Victoria?
    corruption_level = models.CharField(
        label="15. In your opinion, how high is the current level of corruption by the law enforcement institutions at Lake Victoria?",
        choices=[['0', '0 - no corruption'],
                 ['1', '1 - very low corruption'],
                 ['2', '2 - low corruption'],
                 ['3', '3 - medium corruption '],
                 ['4', '4 - high corruption'],
                 ['5', '5 - very high corruption'],
                 ['99', C.NOT_WANT_TO_ANSWER],
                 ],
        widget=widgets.RadioSelect,
        blank=False, )


    #######################################################################
    # Identity
    #######################################################################

    # 16. How much do you identify with the fishers at Lake Victoria?
    ident_lv = make_agree_field(label='16. How much do you agree with the following statement?	I identify with all fishers at Lake Victoria.')

    # 17. I identify with the Nile Perch fishers at Lake Victoria
    ident_np = make_agree_field(label='17. How much do you agree with the following statement? I identify with the Nile Perch fishers at Lake Victoria.')

    # 18. I identify with the Mukene fishers at Lake Victoria.
    ident_d = make_agree_field(label='18. How much do you agree with the following statement? I identify with the Mukene fishers at Lake Victoria.')

    #######################################################
    # Lake perception / Scarcity
    ######################################################
    # 19. Do you think that the number of Mukene in Lake Victoria has declined in the last 10 years?
    mukene_decline = make_much_field(
        label='19. Do you think that the number of Mukene in Lake Victoria has declined in the last 10 years?')

    # 20 Do you think that the number of Nile Perch in Lake Victoria has declined in the last 10 years?
    np_decline = make_much_field(
        label='20. Do you think that the number of Nile Perch in Lake Victoria has declined in the last 10 years?')

    ##Severity/Worry

    #21.	Based on your experience in the fishery, please rate how severe the following issues are for the earnings from fishing on Lake Victoria.
    conflicts_fishers=make_severity_field(label='a. Conflicts between fishers of different species.')
    increase_illegal=make_severity_field(label='b. Increasing use of illegal gears.')
    change_weather=make_severity_field(label='c. Changing weather conditions')


    #22.	How much do the following things worry you?
    worry_stocks = make_much_field(label='a. Declining fish stocks in Lake Victoria')
    worry_arrest = make_much_field(label='b. Arrest by law enforcement')

    ###########################
    # financial perception
    ###########################

    # 23. Do you think you earn more or less than other fishermen at this landing site?
    earn_more = make_much_field(label='23. Do you think you earn more or less than other fishermen at this landing site?')

    # 24. Do you think that using illegal gear leads to more or less earning than using legal gear?
    illegal_more = make_much_field(label = "24. Do you think that using illegal gear leads to more or less earning than using legal gear?")

    ##################################
    # illegal behavior
    #################################

    #25.	How often does a typical Nile Perch fisher at your landing site violate existing rules and regulations?
    compl_NP=make_never_always_field(label='25.	How often does a typical Nile Perch fisher at your landing site violate existing rules and regulations?')

    #26.	How often does a typical Mukene fisher at your landing site violate existing rules and regulations?
    compl_D = make_never_always_field(
        label='26. How often does a typical Mukene fisher at your landing site violate existing rules and regulations?')

    # 27.	Did you ever use illegal gears?
    use_illegal=make_yes_no_field(label='27.	Did you ever use illegal gears?')

    share_illegal=models.PositiveIntegerField(label='In which share of your fishing trips during the last 12 months did you use illegal gear?',
        blank = True,
        initial= None)

    # 28.	Did you ever pay someone to not control or not punish you?
    use_corruption=make_yes_no_field(label='28.	Did you ever pay someone to not control or not punish you?')

    num_corruption=models.PositiveIntegerField(label='Approximately how many times during the last 12 months did you pay someone to not control or not punish you?',
        blank = True,
        initial= None)



    # 29.	How often have you been charged for violating existing rules and regulations since August last year?
    numcharge = models.PositiveIntegerField(
        label='29. How often have you been charged for violating existing rules and regulations since August last year?',
        blank=True,
        initial=None
    )
    numcharge_na = models.BooleanField(blank=True,label='No answer', initial=False)


#################################
    #Legitimacy of regulation
    ############################

#30.	How much do you agree with this statement: The mesh size regulation improves the well-being of all fishers?
    improve_fisher = make_agree_field(label='30. How much do you agree with this statement: The mesh size regulation improves the well-being of all fishers?')

# 31. How much do you agree with this statement: The current punishment for violations of existing rules and regulations is too severe.'
    improve_np = make_agree_field(
        label='31. How much do you agree with this statement: The mesh size regulation improves the well-being of Nile Perch fishers?')
# 32. How much do you agree with this statement: The mesh size regulation improves the well-being of Mukene fishers?
    improve_d = make_agree_field(
        label='32. How much do you agree with this statement: The mesh size regulation improves the well-being of Mukene fishers?')

#33. How much do you agree with this statement: The mesh size regulation only improves the well-being of well-established fishers?

    improve_establish= make_agree_field(
        label='33.	How much do you agree with this statement: The mesh size regulation only improves the well-being of well-established fishers?')
#34. How much do you agree with this statement: The mesh size regulation is a fair regulation?

    fair_regulation= make_agree_field(
        label='34.	How much do you agree with this statement: The mesh size regulation is a fair regulation?')


#35. How much do you agree with this statement: The enforcement in your fishing area is adequate?

    adequate_enforcement= make_agree_field(
        label='35.	How much do you agree with this statement: The enforcement in your fishing area is adequate?')



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


class InstitutionPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['responsible_monitoring', 'bmu_member','prob_detect','prob_detect_na','corruption_level']

    def error_message(player: Player, values):
        if values['prob_detect'] == None and values['prob_detect_na'] == False:
            return C.ANSWER_ALL


    pass

class IdentityPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['ident_lv', 'ident_np','ident_d']


    pass


class ScarcityPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['mukene_decline', 'np_decline']


    pass

class SeverityWorryPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['conflicts_fishers','increase_illegal','change_weather','worry_stocks','worry_arrest']


    pass


class FinancialPerceptionPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['earn_more','illegal_more']


    pass


class Compliance1Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['compl_NP', 'compl_D','use_illegal','use_corruption']


    pass



class Compliance2Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['share_illegal','num_corruption','numcharge','numcharge_na']

    def error_message(player: Player, values):
        if player.use_illegal=='yes' and values['share_illegal'] == None:
            return C.ANSWER_ALL
        if player.use_corruption=='yes' and values['num_corruption'] == None:
            return C.ANSWER_ALL
        if values['numcharge'] == None and values['numcharge_na'] == False:
            return C.ANSWER_ALL




    pass




class LegitPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['improve_fisher', 'improve_np','improve_d','improve_establish','fair_regulation','adequate_enforcement']


    pass





#############


###############################################################################
# testing type of action
###############################################################################
# PAGES
class Wait(WaitPage):
    wait_for_all_groups = True
    title_text = "Please Wait!"
    body_text = ""

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        pass

page_sequence = [
    Wait,
    InstitutionPage,
    IdentityPage,
    ScarcityPage,
    SeverityWorryPage,
    FinancialPerceptionPage,
    Compliance1Page,
    Compliance2Page,
    LegitPage
]
