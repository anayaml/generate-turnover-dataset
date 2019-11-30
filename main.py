import os
import csv
import pandas as pd
import util
import time

reviews = open('dataset.csv', 'a', encoding='utf8')
reviews_writer = csv.writer(reviews, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

dataframe = pd.read_csv('input.csv',usecols=["job_title","employee_status","location","review_date","review_text"])

def verifyLocation(location):
    if(util.verifyInvalidAttr(location)):
        return False
    elif(util.verifySpamAttr(location)):
        return False
    else:
        return True

def verifyReviewText(review_text):
    if(util.verifyInvalidAttr(review_text)):
        return False
    elif(util.verifySpamAttr(review_text)):
        return False
    else:
        return True

def verifyJobTitle(job_title):
    if(util.verifyInvalidAttr(job_title)):
        return False
    elif(util.verifySpamAttr(job_title)):
        return False
    else:
        return True

def generateDataset():
    count = 14164
    for reg in dataframe.itertuples():
        if not verifyReviewText(reg.review_text):
            print('Review removed because contains an invalid review text.')
        elif not verifyJobTitle(reg.job_title):
            print('Review removed because contains an invalid job title.')
        elif not verifyLocation(reg.location):
            print('Review removed because contains an invalid location.')
        else:
            count +=1
            country = util.getCountry(reg.location)
            reviews_writer.writerow([count, reg.job_title, reg.employee_status, reg.location, country, reg.review_date, reg.review_text])
            print(str(count) + '/' + str(len(dataframe)))
generateDataset()