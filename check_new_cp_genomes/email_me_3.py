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

subject = date_today() + ": Fern plastid Genome List Update"

body = "insert requireed text here \n next line here"

recipient = "paul.wolf@usu.edu" # or add list of email addresses

send_email("paul.wolf11@gmail.com", "spun65432",recipient, subject, body)