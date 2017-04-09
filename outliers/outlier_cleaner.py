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
    for index, predict in enumerate(predictions):
      error = (predict - net_worths[index])**2
      cleaned_data.append([ages[index], net_worths[index], error])

    cleaned_data = sorted(cleaned_data, key=lambda k: k[2])
    length = len(cleaned_data) * .9

    return cleaned_data[0:int(length)]
