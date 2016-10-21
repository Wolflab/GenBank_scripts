Not yet set up (Jan 31 2016)

But I did test this on 11" laptop
Once program is where you want it on HD
Then navigate to directory and type:

sudo python setup.py install


Need to ask this question:

module name is email_message.py
will not run as import email_message

Does work if imported thusly:
from email_message import send_email

but also need date_today()


or
from email_message import *  

Above works.

Can this be handled in setup.py?
Anything to do with the entry_points


here is the code so far:

from setuptools import setup
 
setup(
          name="email_message",
          version="0.1",
          author = "Paul G. Wolf",
          author_email = "paul.wolf11@gmail.com",
          entry_points = {'console_scripts': ['send_mail = email_message:main']},
          py_modules = ['email_message']
)