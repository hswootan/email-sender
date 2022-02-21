import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Hong'
email['to'] = 'email_to_send'
email['subject'] = 'claim your 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'John'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_email_account', 'your_password!')
    smtp.send_message(email)
    print("All good!")

# -----------------------
# -----------------------
# email = EmailMessage()
# email['from'] = 'Hong W'
# email['to'] = 'email_to_send'
# email['subject'] = 'claim your 1,000,000 dollars!'

# email.set_content("Testing email!")

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('your_email_account', 'your_password')
#     smtp.send_message(email)
#     print("All good!")
# -----------------------
