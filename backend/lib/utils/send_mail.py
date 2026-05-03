#   Python Libraries
from os import getenv

#   Internal Libraries
from .custom_functions import SendMail

RECIEVER: str = getenv('RECIEVER', '')
SMPTMASTER: str = getenv('SMPTMASTER', '') 
SMTPPASSWORD: str = getenv('SMTPPASSWORD', '')

if __name__ == '__main__':
        mail = SendMail()
        mail.send_mail_gmail(SMPTMASTER, SMTPPASSWORD, RECIEVER)
        mail.send_mail_yahoo(SMPTMASTER, SMTPPASSWORD, RECIEVER)
        mail.send_mail_server(SMPTMASTER, SMTPPASSWORD, RECIEVER)
        mail.send_mail_outlook(SMPTMASTER, SMTPPASSWORD, RECIEVER)
