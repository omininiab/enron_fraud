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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("Num. people in dataset", len(enron_data))
print("Num. info on each person", len(enron_data['METTS MARK']))
poi = 0
max_payout = 0
thief = None
salary = 0
email = 0
no_payments = 0
no_payments_poi = 0
for person in enron_data:
    if enron_data[person]['poi']:
        poi += 1
        if enron_data[person]['total_payments'] == 'NaN':
            no_payments_poi += 1
    if enron_data[person]['salary'] != 'NaN':
        salary += 1
    if enron_data[person]['email_address'] != 'NaN':
        email += 1
    if enron_data[person]['total_payments'] == 'NaN':
        no_payments += 1
    try:
        if person!= 'TOTAL' and int(enron_data[person]['total_payments']) > max_payout:
            max_payout = enron_data[person]['total_payments']
            thief = person
    except:
        pass

print("Number of POI", poi)
print("James Prentice Stock", enron_data['PRENTICE JAMES']['total_stock_value'])
print("Colwell Wesley Emails", enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print("Jeffrey K Skilling Stock", enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print(thief, max_payout)
print(salary, email)
print(no_payments/len(enron_data))
print(no_payments_poi/poi)
