# app.py

from flask import Flask, render_template, request
from engine import InferenceEngine
from datetime import datetime

app = Flask(__name__)

def generate_investigation_report(form_data, result):
    investigation_no = "INV-" + str(hash(form_data['victim_name']) % 10000)  # Auto-generated investigation number
    report = f"""
    Investigation Report
    
    Investigation Number: {investigation_no}
    Investigation Time: {form_data['investigation_time']} hours
    
    --- 
    Victim Information:
    Name: {form_data['victim_name']}
    Time of Incident: {form_data['investigation_time']}
    
    --- 
    Conclusion: Based on the collected evidence, it is concluded that {result}.
    """
    return report

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    report = None
    
    if request.method == 'POST':
        form_data = {
            'victim_name': request.form['victim_name'],
            'investigation_time': request.form['investigation_time'],
            'struggle': request.form['struggle'],
            'injuries': request.form['injuries'],
            'weapon_present': request.form['weapon_present'],
            'defensive_wounds': request.form['defensive_wounds'],
            'body_position': request.form['body_position'],
            'suicide_note': request.form['suicide_note'],
            'foreign_dna': request.form['foreign_dna'],
            'locked_room': request.form['locked_room'],
            'forced_entry': request.form['forced_entry'],
            'time_of_death': request.form['time_of_death'],
            'toxicity_report': request.form['toxicity_report'],
            'financial_issues': request.form['financial_issues'],
            'mental_health_history': request.form['mental_health_history'],
            'witness_statements': request.form['witness_statements'],
            'previous_threats': request.form['previous_threats'],
            'social_media_posts': request.form['social_media_posts'],
            'history_of_violence': request.form['history_of_violence'],
        }

        # Create the inference engine instance
        engine = InferenceEngine()

        # Evaluate the case
        result = engine.evaluate_case(form_data)

        # Generate the investigation report
        report = generate_investigation_report(form_data, result)

    return render_template('index.html', result=result, report=report)

if __name__ == '__main__':
    app.run(debug=True)
