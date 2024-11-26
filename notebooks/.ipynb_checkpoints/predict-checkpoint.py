import pickle
import xgboost as xgb

# Loading the model with pickle
with open('../depression_predictor/best_xgboost.bin', 'rb') as file:
    dv, loaded_model = pickle.load(file)

# Make predictions using the loaded model

person ={'age': 26.0,
         'academic-pressure': 3.0,
         'work-pressure': -1.0,
         'cgpa': 7.53,
         'study-satisfaction': 4.0,
         'job-satisfaction': -1.0,
         'work-study-hours': 8.0,
         'financial-stress': 4.0,
         'gender': 'female',
         'city': 'pune',
         'working-professional-or-student': 'student',
         'profession': 'not applicable',
         'sleep-duration': 'less than 5 hours',
         'dietary-habits': 'unhealthy',
         'degree': 'b.tech',
         'have-you-ever-had-suicidal-thoughts-?': 'no',
         'family-history-of-mental-illness': 'yes'}

X= dv.transform(person)
features = list(dv.get_feature_names_out())
dtest = xgb.DMatrix(X, feature_names=features)
y_pred = loaded_model.predict(dtest)

print(f'Input:{person}')
print(f'Depression Risk Probability is {y_pred[0]}')