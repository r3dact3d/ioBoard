#!/usr/bin/python

import bluetooth
import time
import smtplib

# These are commented out until I can make this script check for all
# using one function and not 4 different if loops
#fam = {"Dad" : "Dad BT Address",
#       "Mom" : "Mom BT Address",
#       "Son" : "Son BT Address",
#  "Daughter" : "Daughter BT Address"}
#for key, value in fam.iteritems():

def sendMail(name, subject):
# Change Sender_email to your email address
    sender = 'Sender_email@gmail.com'
# Change To_email to who you want to send email to
    email = 'To_email@gmail.com'
    payLoad = 'Subject: %s\n' % subject
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
# Change SECRET_PASSWORD to your gmail password or whatever email provider
    smtp.login(sender, 'SECRET_PASSWORD')
    smtp.sendmail(sender, email, payLoad)
    smtp.quit()

def ioBoard():
# Set status is blank until it is either set in or out, to deteremine when there is a change and
# email needs to be sent to notify when someone either comes in or goes out
    status = ''
    key = 'Mom'
    while True:
# Change 'MOMS BT ADDRESS' to a real Bluetooth Address
        result = bluetooth.lookup_name('MOMS BT ADDRESS', timeout=15)
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

ioBoard()
