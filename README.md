# Automated-birthday-wishes
This repository contains a Python script that automatically sends a personalized birthday email to friends listed in a CSV file. The script checks if today’s date matches any birthday in the CSV file. If it does, the script selects a random letter template, personalizes it with the friend’s name, and sends the email.

Tools Used:

Python: The script is written in Python.
pandas: Used to read the CSV file containing the birthdays.
datetime: Used to get the current date.
smtplib: Used to send the email via Gmail’s SMTP server.
email: Used to create the email message.
random: Used to select a random letter template.