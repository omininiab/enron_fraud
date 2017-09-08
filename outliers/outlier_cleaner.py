#!/usr/bin/python

def takeLast(elem):
    return elem[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    for i in range(0, len(ages)):
        cleaned_data.append((ages[i], net_worths[i], abs(predictions[i] - net_worths[i])))

    cleaned_data = sorted(cleaned_data, key=takeLast, reverse=False)

    cleaned_data = cleaned_data[0:int(0.9*len(cleaned_data))]

    return cleaned_data
