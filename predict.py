import pickle
import xgboost as xgb
import time
t0=time.time()
# Loading the model with pickle
with open('./depression_predictor/best_xgboost.bin', 'rb') as file:
    dv, loaded_model = pickle.load(file)

# Make predictions using the loaded model

person ={'age': 25.0,
         'academic-pressure': 5,
         'work-pressure': 5.0,
         'cgpa':-1,
         'study-satisfaction': -1,
         'job-satisfaction': 5.0,
         'work-study-hours': 15.0,
         'financial-stress': 3.0,
         'gender': 'male',
         'city': 'pune',
         'working-professional-or-student': 'working professional',
         'profession': 'designer',
         'sleep-duration': 'less than 5 hours',
         'dietary-habits': 'healthy',
         'degree': 'b.tech',
         'have-you-ever-had-suicidal-thoughts-?': 'no',
         'family-history-of-mental-illness': 'no'}

X= dv.transform(person)
features = list(dv.get_feature_names_out())
dtest = xgb.DMatrix(X, feature_names=features)
y_pred = loaded_model.predict(dtest)
t1=time.time()
print(f'Input:{person}')
print(f'Depression Risk Probability is {y_pred[0]}')
t=t1-t0
print(f'Duration taken is {t} in seconds')