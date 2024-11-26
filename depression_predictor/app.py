from flask import Flask, request, jsonify
import pickle
import numpy as np
import xgboost as xgb
from flask import Flask, request, jsonify, render_template
import pickle
import sqlite3
import os

app = Flask(__name__)



current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'best_xgboost.bin')

print(current_dir)
print(model_path)

# Load your pre-trained model
with open(model_path, 'rb') as model_file:
    dv, model = pickle.load(model_file)


# Home route with form input
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from POST request
    data = request.form
    try:
        person_data = {
          "age": int(data.get("age", 0)) if data.get("age") else -1,
            "gender": data.get("gender"),
            "city": data.get("city"),
            "academic_pressure": int(data.get("academic-pressure", -1)) if data.get("academic-pressure") else -1,
            "work_pressure": int(data.get("work-pressure", -1)) if data.get("work-pressure") else -1,
            "cgpa": float(data.get("cgpa", -1)) if data.get("cgpa") else -1,
            "study_satisfaction": int(data.get("study-satisfaction", -1)) if data.get("study-satisfaction") else -1,
            "job_satisfaction": int(data.get("job-satisfaction", -1)) if data.get("job-satisfaction") else -1,
            "work_study_hours": int(data.get("work-study-hours", 0)) if data.get("work-study-hours") else 0,
            "financial_stress": int(data.get("financial-stress", 0)) if data.get("financial-stress") else 0,
            "working_professional_or_student": data.get("working-professional-or-student"),
            "profession": data.get("profession"),
            "sleep_duration": data.get("sleep-duration"),
            "dietary_habits": data.get("dietary-habits"),
            "degree": data.get("degree"),
            "suicidal_thoughts": data.get("have-you-ever-had-suicidal-thoughts-?"),
            "family_history": data.get("family-history-of-mental-illness")
            }
    except ValueError as e:
        return f"Invalid input: {e}", 400

    try:
        X = dv.transform([person_data])
        features = list(dv.get_feature_names_out())
        dtest = xgb.DMatrix(X, feature_names=features)
        y_pred = model.predict(dtest)
        
        
        # Make a prediction
        prediction = round(y_pred[0], 2)
        prediction_result = f"The depression risk is: {prediction * 100}%"

        # If the request is JSON, return JSON response
        if request.is_json:
            return jsonify({"prediction": prediction_result}), 200
        else:
            # Otherwise, render the template with the result
            return render_template('index.html', prediction=prediction_result), 200

    except Exception as e:
        if request.is_json:
            return jsonify({"error": f"Error making prediction: {e}"}), 500
        else:
            return f"Error making prediction: {e}", 500


        
    


        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

