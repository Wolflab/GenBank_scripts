#! /usr/bin/env python
#
# This script sends an email from sender to recipient with update info
# Based on script found here: http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


def date_today(): 
    import datetime
    today = datetime.date.today()
    return str(today)

date = date_today()

recipient = "paul.wolf@usu.edu" # or add list of email addresses


if __name__ == '__main__':
    send_email("paul.wolf11@gmail.com", "spun65432", "paul.wolf@usu.edu", date + " - Fern plastid Genome List Update", "insert required text here \n next line here")