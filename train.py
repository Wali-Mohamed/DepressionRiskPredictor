import pickle
import time
import pandas as pd
import numpy as np
import warnings
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, confusion_matrix, accuracy_score, roc_auc_score, ConfusionMatrixDisplay, precision_score, recall_score,classification_report

def wrangle(path, impute=None,  drop_features=[]):
    print('Preparing data.....')
    df=pd.read_csv(path)
    
     # Change columns titles to lower case
    df.columns=df.columns.str.lower().str.replace(' ', '-').str.replace('/', '-').to_list()
    # get numerical columns
    numerical = [col for col in df.select_dtypes(np.number).columns if col!= 'id' and col!='depression']
   
    # get categorical columns
    categorical=[col for col in df.select_dtypes('object').columns if col!='name' and col!='depression']
    # Change categorical column content to lower case
    for col in categorical:
        df[col]=df[col].str.lower()
    if impute=='conditional':
        # Impute missing values conditionally all working professional with -1 for NaN in these three fields to indicate          that they are not applicable
        df.loc[df['working-professional-or-student'] == 'working professional' , ['study-satisfaction', 'academic-     pressure','cgpa']]=-1
        # Impute missing values conditionally all student with - for NaN in these three fields to indicate that they are not applicable
        df.loc[df['working-professional-or-student'] == 'student' , ['work-pressure','job-satisfaction']]=-1
        # Condition for students (assuming all student entries should have 'Not Applicable' irrespective of current 'profession' value)
        df.loc[df['working-professional-or-student'] == 'student', 'profession'] = 'not applicable'
        # fill NaN with mode for remaining categorical values
        for col in categorical:
            # fill in all NaN by the mode
            mode=df[col].mode()
            df[col] = df[col].fillna(mode.iloc[0])
            # fill NaN with median for remaining numerical values
        for col in numerical:
            # fill in all NaN by the median
            median=df[col].median()
            df[col] = df[col].fillna(median)
    elif impute=='general':
        # fill NaN with mode for remaining categorical values
        for col in categorical:
            # fill in all NaN by the mode
            mode=df[col].mode()
            df[col] = df[col].fillna(mode.iloc[0])
        # fill NaN with median for remaining numerical values
        for col in numerical:
            # fill in all NaN by the median
            median=df[col].median()
            df[col] = df[col].fillna(median)
    else:
        logging.warning("No imputation performed. 'impute' parameter did not match 'conditional' or 'general'.")
        
    # features
    features=numerical +categorical
    # features to be dropped
    removed_cols = drop_features
    # Remove all instances in removed_cols
    features = [x for x in features if x not in removed_cols]
    
    return df, features   
def split_data(df, features):
    df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=1)
    df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=1)
    print(f'Train Data: {round(df_train.shape[0]/df.shape[0],2)*100}%; Validation Data: {round(df_val.shape[0]/df.shape[0],2)*100}%; Test Data:{round(df_test.shape[0]/df.shape[0],2)*100}%')

    # reset index 
    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)
    # get the target values
    y_train = df_train.depression.values
    y_val = df_val.depression.values
    y_test=df_test.depression.values
    # drop target
    del df_train['depression']
    del df_val['depression']
    del df_test['depression']
    print('Training Model...')
    train_dict=df_train[features].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)
    val_dict=df_val[features].to_dict(orient='records')
    X_val = dv.transform(val_dict)
    test_dict=df_test[features].to_dict(orient='records')
    X_test = dv.transform(test_dict)
    print( df_train.shape,df_val.shape, df_test.shape)
    return X_train, y_train, X_val, y_val, X_test, y_test 
t0=time.time()

eta=0.8
max_depth=2
min_child_weight=1

df, features =wrangle('data/train.csv', impute='conditional')
dv= DictVectorizer()

X_train,y_train, X_val, y_val, X_test, y_test= split_data(df, features)


features = list(dv.get_feature_names_out())
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)

# Define the custom evaluation function for binary recall
def recall_eval(preds, dtrain):
    labels = dtrain.get_label()
    # Convert log odds to probabilities using the sigmoid function
    probabilities = 1 / (1 + np.exp(-preds))
    # Determine binary outcome with threshold 0.5
    predictions = np.where(probabilities >= 0.5, 1, 0)
    recall = recall_score(labels, predictions)
    return 'recall', recall

xgb_params = {
    'eta': eta, 
    'max_depth':max_depth,
    'min_child_weight': min_child_weight,
    'objective': 'binary:logistic',
    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, 
                  num_boost_round=70         
                 
                 )
y_pred=model.predict(dval)
print('validation results:')    
print("XGBoost: {:.5}".format(recall_score(y_val, y_pred>=0.5)))

print('Training the Final Model...')
dv = DictVectorizer(sparse=False)

# train final model with train and val data
# Train the final model with training and validation data
df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train_full = df_train_full.reset_index(drop=True)
y_train_full = df_train_full.depression.values
del df_train_full['depression']

dicts_train_full = df_train_full.to_dict(orient='records')

dv = DictVectorizer(sparse=True)
X_train_full = dv.fit_transform(dicts_train_full)

dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

features = list(dv.get_feature_names_out())
dfulltrain = xgb.DMatrix(X_train_full, label=y_train_full,
                    feature_names=features)

dtest = xgb.DMatrix(X_test, feature_names=features)

model = xgb.train(xgb_params, dfulltrain, 
                  num_boost_round=70         
                 
                 )
y_pred = model.predict(dtest)

print('final model results:')    
print("XGBoost: {:.5}".format(recall_score(y_test, y_pred>=0.5)))

# ## Save the Model
output_file = './depression_predictor/best_xgboost.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'Model saved to {output_file}!')    
t1=time.time()
t=t1-t0
print(f'The total duration was {t} seconds')

