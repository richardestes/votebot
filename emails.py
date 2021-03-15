import csv
import random

def get_emails():
    f = open('./data/emails.csv','r')
    reader = csv.reader(f)
    next(reader) # skip first line (header)
    email_list = []
    for row in reader:
      email_list.append(row)
    shuffled_emails = shuffle_emails(email_list)
    return shuffled_emails
    
def shuffle_emails(emails):
    emails_copy = emails.copy()
    random.shuffle(emails_copy)
    return emails_copy

# Credit to ChristopheD from StackOverflow for this beaut
# https://stackoverflow.com/a/752562/9306879
def split_emails(emails,num_blocks):
  length = len(emails)
  return [ emails[i*length // num_blocks: (i+1)*length // num_blocks] for i in range(num_blocks) ]
  