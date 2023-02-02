import smtplib
from email.message import EmailMessage
import sys
import time
import os
import datetime

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg ['subject'] = subject
    msg ['to'] = to

    user = input("\nYour Email => ")




    msg['from'] = user

    password = input("\nPassword => ") #App password generator

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    

    server.send_message(msg)

    print("Done")

    server.quit




if __name__ == '__main__':

    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)
    slowprint("")
    time.sleep(0)
    os.system('clear')


    print("""

    Team
    ██████╗  █████╗ ██████╗ ██╗   ██╗██╗      ██████╗ ███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗████╗  ██║
    ██████╔╝███████║██████╔╝ ╚████╔╝ ██║     ██║   ██║██╔██╗ ██║
    ██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  ██║     ██║   ██║██║╚██╗██║
    ██████╔╝██║  ██║██████╔╝   ██║   ███████╗╚██████╔╝██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                            
                    Author : Jason
                    Date   : 2023.2.1
                    
    
                    Telegram: @J4son0
    
    
    """)
    email_alert(input("\nMsg => "), input("\nBody of the Msg => ") , input("\nEnter the Target's Email => "))

