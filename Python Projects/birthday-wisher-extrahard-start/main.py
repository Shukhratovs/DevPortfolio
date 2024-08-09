##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random

df = pd.read_csv("birthdays.csv")
birthday_dict = df.to_dict(orient="records")

now = dt.datetime.now()
files = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

my_email = "khumoyunshukhratov@gmail.com"
my_password = "ywls djot phvi clgd"

for date in birthday_dict:
    name_to_insert = date['name']
    if date['month'] == now.month and date['day'] == now.day:
        selected_file = random.choice(files)
        with open(selected_file, "r") as letter_file:
            content = letter_file.read()
            modified_letter = content.replace('[NAME]', name_to_insert)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="khumoyunshukhratov@yahoo.com",
                                msg=f"Subject: Birthday Wish!\n\n{modified_letter}"
                                )
