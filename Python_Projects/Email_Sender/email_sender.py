import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()

html = Template(Path('index.html').read_text())
email['from'] = 'Chu Theko'
email['to'] = 'radioactivep2@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'
email.set_content(html.substitute({'name': "Chewy"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Kind of a greeting
    smtp.starttls()  # tls is an encryption mechanism

    # This is where you put in your credentials for the email account you are using
    smtp.login('ttheko101@gmail.com', 'ijrk njuz bsvk lllx')
    smtp.send_message(email)
    print("All good boss!")
