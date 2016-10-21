#! /usr/bin/env python

from email_message import *

recipient = "paul.wolf@usu.edu"
subject = "testing module"
user = "paul.wolf11@gmail.com"
pwd = "spun65432"
body = date_today() + "just testing module on 13 inch"

send_email(user, pwd, recipient, subject, body)

#Get error message that send_email not defined. This is the function name in email_message