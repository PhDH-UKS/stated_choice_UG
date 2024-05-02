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
    NAME_IN_URL = 'Qu1'
    # groups are only attached in cas of information of each other
    PLAYERS_PER_GROUP = None
    # only 1 round with three phases ('event phase', 'information phase', investment phase')
    NUM_ROUNDS = 1

    ##translation
    NEXT = "Next"
    STYLE = "<style> .otree-body {font-size: 1.5em;}</style>"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_yes_no_field(**kwargs):
    ####
    # Yes-No-Fields
    ###

    return models.CharField(
        choices=[
            ['yes', 'Yee'],
            ['no', 'Nedda'],
            ['noanswer', 'Tewali kiddibwaamu']
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal,
        **kwargs,)

    pass


class Player(BasePlayer):
    ###breakpoint p19
    code_breakpoint = models.IntegerField(label="Please enter code")


    def code_breakpoint_error_message(player: Player, value):
        if value != 55:
            return 'You must enter the correct code (55)'

    #######################################################################
    # Demographics
    #######################################################################

    # 1. How old are you?

    age = models.PositiveIntegerField(
        min=18,
        max=120,
        label="1. Oli mukulu kwenkana wa?",
        doc="We collect age data, between 0 and +120.",
    )

    # 2. What is your gender?

    gender = models.CharField(
        # label="What is your gender?"
        label="2. Oli wa kikula ki?",
        # choices=['Male', 'Female', 'Other'],
        choices=[['male', 'Musajja'],
                 ['female', 'Mukazi']],
        widget=widgets.RadioSelect(),
        blank=False,

    )
    # 3. How many years have you lived at this landing site?
    landingyears = models.PositiveIntegerField(
        label="3. Myaka emeka gyomaze ku mwalo guno?",
        # label="4. Umekuwa mvuvi kwa miaka mingapi sasa?",
        blank=False,

    )

    # 4. How many years have you been a fisher?
    fishyears = models.PositiveIntegerField(
        label="4. Myaka emeka gyomaze mu buvubi?",
        # label="4. Umekuwa mvuvi kwa miaka mingapi sasa?",
        blank=False,

    )

    # 5. What is your region of origin?
    region_origin = models.CharField(
        choices=[['Central Uganda', 'Central Uganda'],
                 ['North Uganda', 'Northern Uganda'],
                 ['East Uganda', 'Eastern Uganda'],
                 ['Western Uganda', 'Western Uganda'],
                 ['Non-Ugandan', 'Siri munna Ugandan'],
                 ['No Answer', 'Tewali kiddibwaamu']
                 ],
        widget=widgets.RadioSelect,
        blank=False,
        label="5. Kitundu ki mwosibuka?"
        #label="3. Wewe ni mzaliwa wa mkoa gani?"
    )
    # 6.Which gear do you use?

    gear = models.CharField(
        label='6. Weeyambisa ki?',
        choices=[['gillnet', 'Obutimba'],
                 ['hook', 'Ddobo'],
                 ['small_seine', 'Ekitimba bwa mukene'],
                 ['other gear', 'Ebirala'],
                 ['noanswer', 'Tewali kiddibwaamu']],
        widget=widgets.RadioSelect,
        blank=False

    )
    # mesh size?

    mesh_size_gillnet = models.CharField(
        label='7. Which mesh size (gillnet) do you normally use?',
        choices=[['2.5’’ and below', '2.5’’ and below'],
                 ['3’’ or 3.5’’', '3’’ or 3.5’’'],
                 ['4’’ or 4.5’’', '4’’ or 4.5’’'],
                 ['5’’ or 5.5’’', '5’’ or 5.5’’'],
                 ['6’’ or 6.5’’', '6’’ or 6.5’’'],
                 ['7’’ or 7.5’’', '7’’ or 7.5’’'],
                 ['8’’ or 8.5’’', '8’’ or 8.5’’'],
                 ['9’’ or 9.5’’'    ,'9’’ or 9.5’’'],
                 ['10’’ and above', '10’’ and above'],
                 ['No answer', 'No answer']],

        widget=widgets.RadioSelect,
        initial='',
        blank=False

    )
    mesh_size_small_seine = models.CharField(
        label='7. Which mesh size (small_seine_net) do you normally use?',
        choices=[['< 5mm', '< 5mm'],
                 ['6-7 mm', '6-7mm'],
                 ['8-10 mm', '8-10 mm'],
                 ['No answer', 'No answer']],

        widget=widgets.RadioSelect,
        initial='',
        blank=False

    )
    hook_size = models.CharField(
        label='7. Which hook size do you normally use?',
        choices=[['7 and below','7 and below'],
         ['8','8'],
         ['9','9'],
         ['10','10'],
		 ['11','11'],
         ['12','12'],
         ['13','13'],
         ['14 and above','14 and above'],
		 ['No answer','No answer']],

        widget=widgets.RadioSelect,
        initial='',
        blank=False

    )

    # 8.	What is your main target fish?

    target_fish = models.CharField(
        label='8. Oluubirira by’enyanja ki?',
        choices=[['nileperch', 'Mpuuta'],
                 ['mukene', 'Mukene'],
                 ['tilapia', 'Ngege'],
                 ['other', 'Birala']],
        widget=widgets.RadioSelect,
        blank=False

    )

    # 9.	What is the propulsion method of the boat you currently work on?

    propulsion = models.CharField(
        label='9. Nkola ki eryato gyerikozesa okuseyeeya lyokolako ennaku zino?',
        choices=[['paddle', 'Ekansi'],
                 ['sail', 'Etanga'],
                 ['engine', 'Yingini'],
                 ['noanswer', 'Tewali kiddibwaamu']],
        widget=widgets.RadioSelect,
        blank=False

    )

    #10 What is your role on the boat you currently work on?",
    crewrole = models.CharField(
        # label="What is your role on the boat you currently work on?",
        label="What is your role on the boat you currently work on?",
        # choices=['Owner', 'Captain', 'Crew', 'No answer'],
        # choices=[['owner', 'Mmiliki'],
        #         ['captain', 'Shoferi'],
        #        ['crewmember', 'Mvuvi'],
        #       ['noanswer', 'Hakuna jibu']
        #      ],
        choices=[['owner', 'Owner'],
                 ['captain', 'Captain'],
                 ['crewmember', 'Crewmember'],
                 ['noanswer', 'No answer']
                 ],
        widget=widgets.RadioSelect(),
        blank=False,

    )
    # 11. How much do you pay for a boat license annually?
    yearly_payment = models.PositiveIntegerField(
        label="11. How much do you pay for a boat license annually? (in UGX)",
        blank=False,
    )



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





###############################################################################
# testing type of action
###############################################################################
# PAGES

class Demographics1Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['age', 'gender']

    pass


class Demographics2Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['landingyears', 'fishyears']

    pass

class Demographics3Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['region_origin', 'gear','target_fish']

    pass

class FishPracticePage(Page):
    form_model = 'player'
    form_fields = ['mesh_size_gillnet','mesh_size_small_seine','hook_size','propulsion','yearly_payment']


    def is_displayed(player: Player):
        return display_group(player)

    pass




class Wait(WaitPage):
    wait_for_all_groups = True
    title_text = "Lindako!"
    body_text = ""

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        forward_information(subsession)
        pass

def forward_information(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.vars['yearly_payment'] = p.yearly_payment

class BreakpointPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not display_group(player)

    form_model = 'player'
    form_fields = ['code_breakpoint']
    pass


page_sequence = [
    Demographics1Page,
    Demographics2Page,
    Demographics3Page,
    FishPracticePage,
    BreakpointPage,
    Wait,
]
