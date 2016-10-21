from setuptools import setup
 
setup(
          name="email_message",
          version="0.1",
          author = "Paul G. Wolf",
          author_email = "paul.wolf11@gmail.com",
          entry_points = {'console_scripts': ['send_mail = email_message:main']},
          py_modules = ['email_message']
)