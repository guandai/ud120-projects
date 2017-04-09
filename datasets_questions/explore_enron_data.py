#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import matplotlib.pyplot as plt
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

ll = len(enron_data["SKILLING JEFFREY K"])
count = 0
for person in enron_data:
  if enron_data[person]["poi"]==1:
    count += 1
print(count)

stc =  enron_data["PRENTICE JAMES"]["total_stock_value"]
print(stc)


wc =  enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print(wc)


sjk = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print(sjk)


sjk_value = enron_data["SKILLING JEFFREY K"]["total_payments"]
lk_value = enron_data["LAY KENNETH L"]["total_payments"]
af_value = enron_data["FASTOW ANDREW S"]["total_payments"]
print(sjk_value)
print(lk_value)
print(af_value)

print enron_data["SKILLING JEFFREY K"]
salary_count = 0
email_count = 0
non_payment_count = 0
poi_non_pay = 0
poi_count = 0
for person in enron_data:
  if enron_data[person]["salary"] != "NaN":
  	salary_count += 1
  if enron_data[person]["email_address"] != "NaN":
    email_count += 1
  if enron_data[person]["total_payments"] == "NaN":
    non_payment_count += 1
  if enron_data[person]["total_payments"] == "NaN" and enron_data[person]["poi"] == True:
    poi_non_pay += 1
  if enron_data[person]["poi"] == True:
    poi_count += 1
  
print salary_count
print email_count
print non_payment_count
print non_payment_count / float(len(enron_data))
print poi_non_pay
print poi_count
print poi_non_pay / float(poi_count)

total = len(enron_data)
print total



