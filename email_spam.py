import pandas as pd
import itertools as iter
#import numpy as np

url = "https://raw.githubusercontent.com/mansoo-jobsdecoder/email-spam/main/emails.csv"
emails = pd.read_csv(url)

#print(emails.head())


##email dataset, text column
email_text = emails["text"]
#print(email_text)


#splitting the text data (goal is the split the subject and message
#initialize a dataframe with 5728 rows and 3 columns

emails_data = pd.DataFrame()


emails_data["subject"] = list(iter.repeat(0, len(email_text)))
emails_data["message"] = list(iter.repeat(0, len(email_text)))
emails_data["spam"] = list(iter.repeat(0, len(email_text)))

emails_data["spam"] = emails["spam"]


for i in range(len(email_text)):
    text_split = email_text.iloc[i].split("  ", 1)
    #text_array = np.array(text_split)



    emails_data["subject"].iloc[i] = text_split[0]
    emails_data["message"].iloc[i] = text_split[-1]


display(emails_data)
print(emails_data["message"])
