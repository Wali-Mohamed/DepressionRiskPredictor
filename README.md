# Depression Risk Prediction Project

![Alt text](/images/depressionimage.jpg)

## Problem Statement

Depression is a common but serious mood disorder that affects millions of people worldwide. Early identification of individuals at risk can lead to timely interventions, potentially mitigating severe outcomes. Traditionally, assessing depression risk involves clinical evaluations, which may not be accessible to everyone due to various barriers such as cost, stigma, and availability of mental health professionals.

This project aims to develop a predictive model that can identify adults at risk of depression based on survey data collected from a broad demographic. The survey includes a range of factors such as age, gender, job satisfaction, study/work hours, and family health history, which are non-clinical but have been shown to correlate with mental health risks.

The dataset used in this project is synthetic, generated from a deep learning model trained on an original survey dataset. The synthetic nature of the data ensures privacy and enables wide distribution for academic and research purposes without compromising individual data security.

## Solution Overview

The goal of this project is to build a machine learning model that predicts the risk of depression ('Yes' or 'No'). The model will be trained on the synthetic dataset, with the option to augment this data with the original dataset to improve accuracy and robustness. This approach not only helps in understanding the impact of synthetic data on model performance but also explores how closely synthetic data can mimic real-world data in the context of mental health.

### Key Objectives:
- **Model Development**: Develop a robust machine learning model to predict depression risk.
- **Data Analysis**: Analyze the differences between the synthetic and original datasets to understand the limitations and capabilities of synthetic data.
- **Visualization**: Implement various data visualization techniques to uncover underlying patterns and insights in the data.

This project is intended for researchers and practitioners in mental health, data science communities interested in the applications of machine learning in public health, and potentially for policymakers looking to understand more about population health management.

# How to Run Application

### Build and Run the Application Using Docker
```bash
docker build -t depression_app .
docker run -it --rm -p 5000:9696 depression_app
```



## Run locally
```bash
git clone https://github.com/Wali-Mohamed/DepressionRiskPredictor.git
cd depression_predictor
pip install pipenv
```
### Install Dependencies

```bash
pipenv install
```
### Activate virtual environment
```bash
pipenv shell
```

### Run the Application
```
```bash
python app.py

```

### Deactivate the environment
```bash
exit
```
* Web Service

```
Start service:  python app.py
In jupyter notebook, issue following statements:

- import requests
- url = 'http://localhost:9696/predict'
- person ={
    "age": 6.0,
    "academic-pressure": -1,
    "work-pressure": 5,
    "cgpa": -1,
    "study-satisfaction": -1,
    "job-satisfaction": 1,
    "work-study-hours": 15.0,
    "financial-stress": 5.0,
    "gender": "male",
    "city": "pune",
    "working-professional-or-student": "working professional",
    "profession": "teacher",
    "sleep-duration": "less than 5 hours",
    "dietary-habits": "unhealthy",
    "degree": "b.tech",
    "have-you-ever-had-suicidal-thoughts-?": "no",
    "family-history-of-mental-illness": "yes"
}
	- requests.post(url, json=person).json()

```
On command line

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "age": 60.0,
    "academic-pressure": -1,
    "work-pressure": 5,
    "cgpa": -1,
    "study-satisfaction": -1,
    "job-satisfaction": 1,
    "work-study-hours": 15.0,
    "financial-stress": 5.0,
    "gender": "male",
    "city": "pune",
    "working-professional-or-student": "working professional",
    "profession": "teacher",
    "sleep-duration": "less than 5 hours",
    "dietary-habits": "unhealthy",
    "degree": "b.tech",
    "have-you-ever-had-suicidal-thoughts-?": "yes",
    "family-history-of-mental-illness": "yes"

}'  http://localhost:9696/predict
```

### On cloud
The app has been deployed on **AWS EC2**
[Depression Risk Predictor](http://3.10.221.130:5000)

for training the model on command line 

```

python train.py 

```

For predicting using sample data

```

python predict.py
```

## Project File Structure

parent_directory/  
├── data/  
│   ├── train.csv  
│   ├── final_depression_dataset_1.csv  
├── depression_predictor/  
│   ├── app.py  
│   ├── best_xgboost.bin  
│   ├── static/  
│   ├── templates/  
├── notebook.ipynb  
├── train.py  
├── predict.py  
├── Dockerfile  
├── Pipfile  
└── Pipfile.lock  










## Handling Missing Values: A Structured and Tailored Approach

Upon detailed analysis, distinct patterns of missing values were identified in the dataset, correlating strongly with the participants' categories—students and working professionals. This categorization guided the data cleaning and preparation process:

### Pattern Identification:
- **Fields Not Applicable to Professionals:** 'Study Satisfaction', 'Academic Pressure', and 'CGPA' were predominantly missing for working professionals, indicating non-applicability to this group.
- **Fields Irrelevant for Students:** Conversely, 'Profession', 'Work Pressure', and 'Job Satisfaction' showed significant missingness among students, marking these fields as irrelevant for this subgroup.

### Targeted Data Imputation Strategies:
- **For Students:**
  - Entries not applicable to students, such as professional features, were imputed with "Not Applicable", accurately reflecting the data's irrelevance for this subgroup.
- **For Working Professionals:**
  - Missing data in 'Profession', where essential, was imputed with the mode value of this variable among working professionals, ensuring consistency and filling gaps with the most frequently observed category.
  
### Specific Imputation Methods Chosen:
- **Numerical Data:**
  - Numerical fields where data was not applicable (e.g., 'CGPA' for professionals) were set to `-1`, marking them distinctly as non-applicable.
  - Applicable numerical values missing among students were imputed using the median of the respective fields to maintain a balanced data distribution.
- **Categorical Data:**
  - "Not Applicable" was used for fields irrelevant to certain groups, maintaining clear differentiation.
  - For applicable categorical data among professionals, missing entries were filled using the mode, preserving characteristic consistency within the group.

This methodical approach to managing missing data ensured the dataset's robustness and representativeness, enhancing the accuracy of analyses and modeling. By recognizing the structured absence of data due to distinct participant groups and applying context-specific imputation methods, the integrity and reliability of the subsequent analytical procedures were upheld. Such rigor in the methodological approach is essential to avoid misinterpretation and ensure the validity and applicability of the findings to the respective groups within the dataset.



### Summary: Metric Selection in Depression Risk Prediction

In developing our depression risk prediction model, we prioritize key metrics to align with medical field demands:

- **Recall:** Chosen as the primary metric due to its critical role in minimizing false negatives and addressing class imbalance with the 20% at-risk prevalence. Essential for preventing severe consequences by identifying at-risk individuals.
- **AUC (Area Under the ROC Curve):** Evaluates the model’s discriminative ability across decision thresholds and aids in model comparison.

Secondary metrics like **accuracy, precision,** and **F1 Score** are less emphasized:
- **Accuracy** is less relevant due to data imbalance.
- **Precision** and **F1 Score** help balance recall but are secondary to ensuring all potential cases are captured.

### Conclusion:
**Recall** is paramount in our model to ensure no at-risk individual is missed, aligning with the high stakes of medical diagnostics and ethical standards of healthcare analytics.

## Model Performance Report

* Logistic Regression  (Validation Data): Recall 82.4%
* ![Alt text](/plots/cond_recall.png)


* Random Forest  (Validation Data): Recall 78.4%
![Alt text](/plots/randomforest.png)
* XGBoost (Validation Data): Recall 83.34%
![Alt text](/plots/xgb_eta.png)
  Trained the model again with training and validation data combined

* XGBoost (Test Data): Recall 81.9%


