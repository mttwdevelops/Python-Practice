# Created 7/19/2022

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Xav Yav'
email['to'] = 'mttwhwang.works@gmail.com' 
email['subject'] = "This is a test"

email.set_content("This emails contents can be read.")

try:
    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('5RyLFLlVjk@gmail.com', 'v|.@m7nzC^,w)2Mfs9ST&9[;^')
        smtp.send_message(email)
        print('Email has sent.')
except:
    print("It tried but failed..")

# seems this does not work due to google authentication errors. Too bad!