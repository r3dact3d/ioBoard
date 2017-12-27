#!/usr/bin/python

import bluetooth
import time
import smtplib

# These are commented out until I can make this script check for all
# using one function and not 4 different if loops
fam = {"mom" : "xx:xx:xx:xx:xx:xx",
"dad" : "xx:xx:xx:xx:xx:xx;",
"son" : "xx:xx:xx:xx:xx:xx",
"daughter" : "xx:xx:xx:xx:xx:xx"}

def sendMail(name, subject):
# Change Sender_email to your email address
    sender = 'sender@gmail.com'
# Change To_email to who you want to send email to
    email = 'email@gmail.com'
    payLoad = 'Subject: %s\n' % subject
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
# Change SECRET_PASSWORD to your gmail password or whatever email provider
    smtp.login(sender, 'PASSWORD')
    smtp.sendmail(sender, email, payLoad)
    smtp.quit()

def ioBoard(fam):
# Set status is blank until it is either set in or out, to deteremine when there is a change and
# email needs to be sent to notify when someone either comes in or goes out
    status = ''
    while True:
# Change 'MOMS BT ADDRESS' to a real Bluetooth Address
        for key, value in fam.iteritems():
            print(key, value)
            result = bluetooth.lookup_name(value, timeout=15)
            if(result != None):
                print('%s is in') % key
                if(status != 'in'):
                    print('Status has changed for %s') % key
                    status = 'in'
                    subIn = '%s is home!' % key
                    sendMail(key, subIn)
            else:
                print('%s is out') % key
                if(status != 'out'):
                    print('Status has changed for %s') % key
                    status = 'out'
                    subOut = '%s is NOT home!' % key
                    sendMail(key, subOut)
        time.sleep(60)

ioBoard(fam)

