# Individual-Project
---

# Project Description

Every year, cities all throughout the United States receive health inspection scores. I employed time series analysis to forecast the results of health inspections in order to assist the city of San Francisco. This method can be used to deploy inspectors to the sections of the city that require them the most when resources are limited. Through feature engenering and time series analysis, I want to accurately forecast the results of county-level health inspections.  

---

# Goals

Accurately predict health inspection scores for Educational Facilities, Cafe & Bakeries, and Restaurants. 

Utilize the following time series models: moving average, simple average, and last observed

---

# Data Dictionary

|Feature|Description|
|-|-|
|business_category|Either Education, Restaurant, or Cafe & Bakery|
|inspection score|scores assined after an inspection|
|risk category|Either low, moderate, or high risk based on the violation|
|violation_description|brief discription of what the violation was|
|business_postal_code|the postal code in San Francisco|
|inspection_date|Year, month, and day of inspection|



---

# Project plan

- Acuire San Francisco Health Inspection score data as a csv file
- Bring file into python
- Take initial looks and get a brief understanding of features
- Begin cleaning data
- Create new dataframes based on restaurant type
- Split data for each new dataframe
- Establish Initial Hypotheses 
- Explore new dataframes and perform feature selection
- Model with established baseline


---

# Initial assumptions
- Restaraunts/businesses in the inner parts of the city have lower inspection scores. 
- Restaraunts have lower inspection scores than educational facilities. 
---

# Conclusion

- Able to forcast inspection scores for restaraunts, cafe & bakery, and educational facilities using time series analysis.
- With the violation discription and risk categpory I am San Francisco .

---

# How to reproduce your work
- Visit https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8i?row_index=0 and explore data as csv.
- pull data using functions from wrangle.py
- create 3 new dataframes for restaraunts, cafe & baker, and education. 
- split data to train, validate, and test using funtions from wrangle.py
- model useing functions from model.py
---
