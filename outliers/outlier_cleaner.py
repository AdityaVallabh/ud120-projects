#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    for pred, age, worth in zip(predictions, ages, net_worths):
        cleaned_data.append((age[0], worth[0], abs(worth[0] - pred[0])))
    cleaned_data.sort(key=lambda tup: tup[2])
    cleaned_data = cleaned_data[:int(len(cleaned_data)*.9)]
    return cleaned_data

