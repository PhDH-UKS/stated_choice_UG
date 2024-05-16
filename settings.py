from os import environ

SESSION_CONFIGS = [
    dict(
         name='left_down',
         app_sequence=['Qu1','stated_choice'],
         num_demo_participants=2,
         treatment='left_down'
     ),
    dict(
         name='left_up',
         app_sequence=['Qu1','stated_choice'],
         num_demo_participants=2,
         treatment='left_up'
     ),
    dict(
         name='right_up',
         app_sequence=['Qu1','stated_choice'],
         num_demo_participants=2,
         treatment='right_up'
     ),
    dict(
         name='right_down',
         app_sequence=['Qu1','stated_choice'],
         num_demo_participants=2,
         treatment='right_down'
     ),

    dict(
         name='Qu2',
         app_sequence=['Qu2'],
         num_demo_participants=2
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'UGX'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3073746821723'
