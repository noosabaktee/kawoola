import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(to,text):
    me = 'Katimus'
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = to
    
    msg.attach(MIMEText(text, 'html'))
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    
    mail.ehlo()
    
    mail.starttls()
    
    mail.login('katimus.web@gmail.com', 'JUVENTUS')
    mail.sendmail(me, to, msg.as_string())
    mail.quit()