# knowledge_base.py

from experta import *

class CrimeInvestigation(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action='evaluate')

    @Rule(Fact(action='evaluate'), Fact(struggle='yes'))
    def murder_struggle(self):
        self.declare(Fact(murder_score=3))

    @Rule(Fact(action='evaluate'), Fact(struggle='no'))
    def suicide_no_struggle(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(injuries='multiple'))
    def murder_multiple_injuries(self):
        self.declare(Fact(murder_score=2))

    @Rule(Fact(action='evaluate'), Fact(injuries='single'))
    def suicide_single_injury(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(weapon_present='no'))
    def murder_no_weapon(self):
        self.declare(Fact(murder_score=1))

    @Rule(Fact(action='evaluate'), Fact(defensive_wounds='yes'))
    def murder_defensive_wounds(self):
        self.declare(Fact(murder_score=2))

    @Rule(Fact(action='evaluate'), Fact(body_position='unnatural'))
    def murder_unnatural_position(self):
        self.declare(Fact(murder_score=1))

    @Rule(Fact(action='evaluate'), Fact(suicide_note='yes'))
    def suicide_note(self):
        self.declare(Fact(suicide_score=4))

    @Rule(Fact(action='evaluate'), Fact(foreign_dna='yes'))
    def murder_foreign_dna(self):
        self.declare(Fact(murder_score=1))

    @Rule(Fact(action='evaluate'), Fact(locked_room='yes'))
    def suicide_locked_room(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(forced_entry='no'))
    def suicide_no_forced_entry(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(time_of_death='inconsistent'))
    def murder_inconsistent_time(self):
        self.declare(Fact(murder_score=2))

    @Rule(Fact(action='evaluate'), Fact(toxicity_report='positive'))
    def murder_toxicity(self):
        self.declare(Fact(murder_score=1))

    @Rule(Fact(action='evaluate'), Fact(financial_issues='yes'))
    def suicide_financial_issues(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(mental_health_history='yes'))
    def suicide_mental_health(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(witness_statements='absent'))
    def murder_no_witness(self):
        self.declare(Fact(murder_score=1))

    @Rule(Fact(action='evaluate'), Fact(previous_threats='yes'))
    def suicide_previous_threats(self):
        self.declare(Fact(suicide_score=1))

    @Rule(Fact(action='evaluate'), Fact(social_media_posts='suicidal'))
    def suicide_social_media(self):
        self.declare(Fact(suicide_score=3))

    @Rule(Fact(action='evaluate'), Fact(history_of_violence='yes'))
    def murder_history_of_violence(self):
        self.declare(Fact(murder_score=2))
