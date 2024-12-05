import csv
import datetime
from dateutil.relativedelta import relativedelta

def get_last_month_date():
    today = datetime.date.today()
    last_month = today - relativedelta(months=1)
    return last_month

def read_skip_emails_from_file(filename):
    with open(filename, 'r') as f:
        return [email.strip() for email in f.readlines()]

def read_csv_and_print(csv_filename, skip_email_file):
    skip_emails = read_skip_emails_from_file(skip_email_file)
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        last_month_date = get_last_month_date()

        for row in reader:
            if row['user_email'] not in skip_emails and '@' in row['user_email']:
                last_access_date = datetime.datetime.strptime(row['last_access'], '%Y-%m-%d %H:%M:%S.%f %Z')
                last_access_date = last_access_date.date()

                if last_access_date < last_month_date:
                    print(f"User: {row['user_email']}, Last Access: {row['last_access']}")

# Replace 'your_csv_file.csv' and 'skip_emails.txt' with the actual filenames
read_csv_and_print('your_csv_file.csv', 'skip_emails.txt')
