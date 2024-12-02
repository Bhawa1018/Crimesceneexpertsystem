# engine.py

from knowledge_base import CrimeInvestigation, Fact

MURDER_THRESHOLD = 4
SUICIDE_THRESHOLD = 3

class InferenceEngine:
    def evaluate_case(self, form_data):
        # Create an instance of the expert system engine
        engine = CrimeInvestigation()

        # Reset the engine to ensure it's clean for each case
        engine.reset()

        # Declare facts based on form data
        engine.declare(Fact(struggle=form_data['struggle']))
        engine.declare(Fact(injuries=form_data['injuries']))
        engine.declare(Fact(weapon_present=form_data['weapon_present']))
        engine.declare(Fact(defensive_wounds=form_data['defensive_wounds']))
        engine.declare(Fact(body_position=form_data['body_position']))
        engine.declare(Fact(suicide_note=form_data['suicide_note']))
        engine.declare(Fact(foreign_dna=form_data['foreign_dna']))
        engine.declare(Fact(locked_room=form_data['locked_room']))
        engine.declare(Fact(forced_entry=form_data['forced_entry']))
        engine.declare(Fact(time_of_death=form_data['time_of_death']))
        engine.declare(Fact(toxicity_report=form_data['toxicity_report']))
        engine.declare(Fact(financial_issues=form_data['financial_issues']))
        engine.declare(Fact(mental_health_history=form_data['mental_health_history']))
        engine.declare(Fact(witness_statements=form_data['witness_statements']))
        engine.declare(Fact(previous_threats=form_data['previous_threats']))
        engine.declare(Fact(social_media_posts=form_data['social_media_posts']))
        engine.declare(Fact(history_of_violence=form_data['history_of_violence']))

        # Run the expert system
        engine.run()

        # Calculate the total scores for murder and suicide
        murder_score = sum([fact.get('murder_score', 0) for fact in engine.facts.values()])
        suicide_score = sum([fact.get('suicide_score', 0) for fact in engine.facts.values()])

        # Determine the result based on the threshold values
        if murder_score >= MURDER_THRESHOLD:
            return "Murder is more likely based on the evidence."
        elif suicide_score >= SUICIDE_THRESHOLD:
            return "Suicide is more likely based on the evidence."
        else:
            return "Insufficient data to draw a conclusion."
