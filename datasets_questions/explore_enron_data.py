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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print('Total number of people: ' + str(len(enron_data)))
print('Number of features: ' + str(len(enron_data["SKILLING JEFFREY K"])))
print('Features: ' + repr([key for key in enron_data['PRENTICE JAMES']]))
print('Number of POIs: ' + str([enron_data[x]["poi"] for x in enron_data].count(True)))

print("James Prentice's stock value: " + str(enron_data['PRENTICE JAMES']['total_stock_value']))
print("Number of emails from Wesley Colwell to POIs: " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
print("Value of stock options exercised by Jeffrey K Skilling: " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print("Jeff Skilling's (CEO) total payments: " + str(enron_data["SKILLING JEFFREY K"]['total_payments']))
print("Kenneth Lay's (Chairman) total payments: " + str(enron_data["LAY KENNETH L"]['total_payments']))
print("Andrew Fastow's (CFO) total payments: " + str(enron_data["FASTOW ANDREW S"]['total_payments']))

print("People with known salaries: " + str(len(filter(None, [str(enron_data[p]['salary']).isdigit() for p in enron_data]))))
print("People with known email addresses: "+ str(len(enron_data) - [enron_data[p]['email_address'] for p in enron_data].count('NaN')))

print("Percentage of people with unknown total_payments: " + str(1.0*[str(enron_data[p]['total_payments']) for p in enron_data].count('NaN')/len(enron_data) * 100) + '%')
print("Percentage of POIs with unknown total_payments: " + str(1.0*[str(enron_data[p]['total_payments']) if enron_data[p]['poi'] else '0' for p in enron_data].count('NaN')/len(filter(None, [enron_data[p]['poi'] for p in enron_data])) * 100) + '%')
