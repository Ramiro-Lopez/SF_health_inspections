# Individual-Project
---

# Project Description

Every year, cities all throughout the United States receive health inspection scores or grades. During these
inspections, trained public health professionsals evaluate the establishment's sanitary condictions, paying specific attentions to issues such as:
    - Hygine
    - Food sources
    - Food handling and storage practices 
    - Cleaning and sanitization practices 

Health departments that use letter grades generally assign restaurants an A, B, or C grade. These letters typically mean:

A: The restaurant has minimal to no food safety rule violations.
B: The restaurant has minor food safety rule violations that need to be corrected.
C: The restaurant has numerous food safety rule violations that put it at risk of closure.

Several issues can impact these grades. Critical issues that carry higher penalty points may include:

    - Storing food at the wrong temperature
    - Using the same cutting board to prepare raw meat and other foods
    - Using bare hands instead of utensils on “ready to eat” food
    - Food workers failing to wash their hands after handling raw poultry
    - Storing toxic chemicals next to food

Less critical violations that still carry penalty points may include:

    - Improperly thawing food
    - Inaccurate thermometers in a refrigerator
    - No sign at a hand-washing facility reminding employees they must wash their hands
    - Improperly installed ventilation systems 

Health departments often determine how frequently to inspect a restaurant based on the restaurant’s grade. The better the grade, the less frequent the inspections. In general, all restaurants should expect at least one inspection every 10 to 12 months.

I employed time series analysis to forecast the results of health inspections in order to assist public health professionals in the city of San Francisco.
With these predictions they can easly identify low graded establishment and prioratize their inspection schedual with minimal wasted time and recorces.   

    - Targeted inspections on low graded establishments can benefit public health and safty by preventing foodborn illnesses and diseases. 
    - Posted grades can help raise public awarness of food safty and resturant safty. 
 
Through feature engenering and time series analysis, I want to accurately forecast the results of county-level health inspection grades.  

---

# Goals

Accurately predict health inspection scores for Educational Facilities, Cafe & Bakeries, and Restaurants. 

Use a RMSE, MAE, or MAPD to quantify improvment over baseline models. 

Utilize the following time series models: moving average, simple average, and last observed

Expand the models: ARIMA, SARIMA, Prophet, or LSTM neural networks

Outline plans for operationlizing the models if inteded for real-world usage. How will they adapt to new data?
How can their predictions trigger interventions? 

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

# Recommendations
- Give resturants incentives to meet the highest safty standard possible

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
