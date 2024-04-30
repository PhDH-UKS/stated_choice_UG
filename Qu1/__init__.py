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

    #1.  What percentage of your friends are fishers?

    friends_fisher = models.FloatField()


    # 2. How old are you?

    age = models.PositiveIntegerField(
        min=18,
        max=120,
        label="2. Oli mukulu kwenkana wa?",
        doc="We collect age data, between 0 and +120.",
    )

    # 3. What is your gender?

    gender = models.CharField(
        # label="What is your gender?"
        label="3. Oli wa kikula ki?",
        # choices=['Male', 'Female', 'Other'],
        choices=[['male', 'Musajja'],
                 ['female', 'Mukazi']],
        widget=widgets.RadioSelect(),
        blank=False,

    )

    # 4. What is your region of origin?
    region_origin = models.CharField(
        choices=[['Central Uganda', 'Massekkati ga Uganda'],
                 ['North Uganda', 'Mambuka ga Uganda'],
                 ['East Uganda', 'Bukiika ddyo bwa Uganda'],
                 ['Southern Uganda', 'Bukiika kkono bwa Uganda’'],
                 ['Non-Ugandan', 'Siri munna Ugandan'],
                 ['No Answer', 'Tewali kiddibwaamu']
                 ],
        widget=widgets.RadioSelect,
        blank=False,
        label="4. Kitundu ki mwosibuka?"
        #label="3. Wewe ni mzaliwa wa mkoa gani?"
    )

    # 5 How many years have you lived at this landing site?
    landingyears = models.PositiveIntegerField(
        label="5. Myaka emeka gyomaze ku mwalo guno?",
        # label="4. Umekuwa mvuvi kwa miaka mingapi sasa?",
        blank=False,

    )

    # 6. How many years have you been a fisher?
    fishyears = models.PositiveIntegerField(
        label="6. Myaka emeka gyomaze mu buvubi?",
        #label="4. Umekuwa mvuvi kwa miaka mingapi sasa?",
        blank=False,

    )

    # 7. Were your parents fisher? (Did your parents grew up being a fisher?)
    parentsfisher = make_yes_no_field(label='7. Bazaddebo baali bavubi/babaliya?')


    # 8. What other occupations do you have? Specify the one with the highest income share?

    other_occupation = models.CharField(
        label="8. Mirimu ki emirala gy’olina? Yawulako ogusinga okukuwa enyingiza.",
       # choices=[['farmer', 'Mkulima'],
        #         ['livestock rearing', 'Mfugaji'],
         #        ['salesman /businessman', 'Mfanybiashara'],
          #       ['I am only a fisher', 'Ni mvuvi tu'],
           #      ['No answer', 'Hakuna jibu']
            #     ],

        choices=[['farmer', 'Mulimi'],
                 ['livestock', 'Bulunzi'],
                 ['sales', 'Kitunzi / Musuubuzi'],
                 ['fisher', 'Ndi muvubi/mubaliya kyokka'],
                 ['noanswer', 'Tewali kiddibwaamu']
                 ],
        widget=widgets.RadioSelect,
        blank=False
    )
    # What percentage of the total income in your household comes from fishing?

    hhfracfish = models.IntegerField(
        label='9. Kyenkana ki ku nyingiza y’omumaka go ekiva mu buvubi?',
        #label="Uvuvi unachangia asilimia ngapi ya pato kwenye kaya yako?",

        blank=False
        # min=0,
        # max=100,
    )

    #11.	Are you a member of a savings organization?

    sav_member=make_yes_no_field(label='10. Oli kitundu ku bitongole ebifissa/ebitereka sente?')

    #11.	Have you participated in a survey before?

    survey_before = make_yes_no_field(label='11. Wali weetabyeko mu kunoonyereza?')


####
##B. Fishing practices##
###

    #12..Which gear do you use?

    gear = models.CharField(
        label='12. Weeyambisa ki?',
        choices=[['gillnet', 'Obutimba'],
                ['hook','Ddobo'],
                ['small_seine', 'Ekitimba bwa mukene'],
                ['other gear', 'Ebirala'],
                ['noanswer', 'Tewali kiddibwaamu']],
        widget=widgets.RadioSelect,
        blank=False

    )
    #13.	What is your main target fish?

    target_fish = models.CharField(
        label='13. Oluubirira by’enyanja ki?',
        choices=[['nileperch', 'Mpuuta'],
                 ['mukene', 'Mukene'],
                 ['tilapia', 'Ngege'],
                 ['other', 'Birala']],
        widget=widgets.RadioSelect,
        blank=False

    )
#14.	What is the propulsion method of the boat you currently work on?

    propulsion = models.CharField(
        label ='14. Nkola ki eryato gyerikozesa okuseyeeya lyokolako ennaku zino?',
        choices=[['paddle', 'Ekansi'],
                  ['sail','Etanga'],
                  ['engine', 'Yingini'],
                  ['noanswer', 'Tewali kiddibwaamu']],
        widget=widgets.RadioSelect,
        blank=False

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
class FisherFriendsPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['friends_fisher']

    pass

class Demographics1Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['age', 'gender','region_origin']

    pass


class Demographics2Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['landingyears', 'fishyears','parentsfisher']

    pass

class Demographics3Page(Page):
    @staticmethod
    def is_displayed(player: Player):
        return display_group(player)

    form_model = 'player'
    form_fields = ['other_occupation', 'hhfracfish','sav_member','survey_before']

    pass

class FishPracticePage(Page):
    form_model = 'player'
    form_fields = ['gear','target_fish','propulsion']


    def is_displayed(player: Player):
        return display_group(player)

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
    FisherFriendsPage,
    Demographics1Page,
    Demographics2Page,
    Demographics3Page,
    FishPracticePage,
    BreakpointPage,
    Wait,
]
