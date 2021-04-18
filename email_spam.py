import pandas as pd
import itertools as iter
import nltk
from nltk.corpus import stopwords

#import numpy as np

url = "https://raw.githubusercontent.com/mansoo-jobsdecoder/email-spam/main/emails.csv"
emails = pd.read_csv(url)

#print(emails.head())


##email dataset, text column
email_text = emails["text"]
#print(email_text)


#splitting the text data (goal is the split the subject and message
#initialize a dataframe with 5728 rows and 3 columns

#emails_data = pd.DataFrame(index=range(0,5727), columns=["subject","message","spam"])
emails_data = pd.DataFrame()

#fill the dataset with 0's
emails_data["subject"] = list(iter.repeat(0, len(email_text)))
emails_data["message"] = list(iter.repeat(0, len(email_text)))
emails_data["spam"] = list(iter.repeat(0, len(email_text)))

emails_data["spam"] = emails["spam"]

#split subjecg and message
for i in range(len(email_text)):
    text_split = email_text.iloc[i].split("  ", 1)
    #text_array = np.array(text_split)
    emails_data["subject"].iloc[i] = text_split[0]
    emails_data["message"].iloc[i] = text_split[-1]



#end of subject and message separation
#now remove stop words (i.e. not meaningful words like "the," "of," "etc.")

#download list of stopwords form NLTK library
nltk.download('stopwords')
#store the english stopwords in mystopwords
mystopwords = stopwords.words('english')

mystopwords.extend(['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '_', '=', '/',
                   '?', '~', '`', '[', ']', '{', '}', ':', ';'])

#for message
for i in range(len(emails_data)):
#target text (string)
    query = emails_data["message"].iloc[i]

#split the target string into individual words
    querywords = query.split()

#creates a new list with all the words of which the lower-case variant is not found in stopwords.
    resultwords  = [word for word in querywords if word.lower() not in mystopwords]
    result = ' '.join(resultwords)

    emails_data["message"].iloc[i] = result



#for subject
for i in range(len(emails_data)):
#target text (string)
    query = emails_data["subject"].iloc[i]

#split the target string into individual words
    querywords = query.split()

#creates a new list with all the words of which the lower-case variant is not found in stopwords.
    resultwords  = [word for word in querywords if word.lower() not in mystopwords]
    result = ' '.join(resultwords)

    emails_data["subject"].iloc[i] = result

emails_data.to_csv('emails-stopwords.csv')


#drop duplicate data
emails_data.drop_duplicates(inplace=True)
emails_data.shape
