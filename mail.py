import os
import sys
import time
import smtplib
import getpass

SMTP_YAHOO_SERVER_NAME = 'smtp.mail.yahoo.com' #port : 465
SMTP_GMAIL_SERVER_NAME = 'smtp.gmail.com' #port : 587
SMTP_OUTLOOK_SERVER_NAME = 'smtp.office365.com' #port : 587

menu_message_count = """
     [ID]     [ MESSAGE COUNT ]

      0   :         500
      1   :         400
      2   :         300
      3   :         200
      4   :         100
      5   :        Custom
      6   :        Cancel
"""
menu_server_port = """
    [ID]      [SERVER NAME]     [PORT]

     0          GMAIL            587
     1          OUTLOOK          587
     2          YAHOO            465
     3          Custom          Custom
     4          Cancel
"""
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class MailSend:
    count = 0
    def __init__(self):
        self.server_name = None
        self.port = None
        try:
            while True:
                self.fromAddress = str(input(colors.BOLD + colors.OKGREEN +"Please Enter Your Mail Address : "))
                if not self.fromAddress:
                    print(colors.BOLD + colors.WARNING + "Please Enter Your Mail Address ...")
                    time.sleep(1)
                    self.clear_terminal()
                    self.fromAddress = str(input(colors.BOLD + colors.OKGREEN +"Please Enter Your Mail Address : "))
                self.fromPassword = str(input(colors.BOLD + colors.OKGREEN +"Please Enter Your Mail Address Password : "))
                if not self.fromPassword:
                    print(colors.BOLD + colors.WARNING +"Please Enter Your Mail Addres Password ...")
                    time.sleep(1)
                    self.clear_terminal()
                    self.fromPassword = str(input(colors.BOLD + colors.OKGREEN +"Please Enter Your Mail Address Password : "))
                self.target = str(input(colors.BOLD + colors.OKGREEN +"Please Destination Mail Address : "))
                if not self.target:
                    print(colors.BOLD + colors.WARNING +"Please Enter Destination Mail Address ...")
                    time.sleep(1)
                    self.clear_terminal()
                    self.target = str(input(colors.BOLD + colors.OKGREEN +"Please Destination Mail Address : "))
                self.message = str(input(colors.BOLD + colors.OKGREEN +"Please Message : "))
                if not self.message:
                    self.message = "Hi i am incarter!!!"
                self.menu()
                break
        except KeyboardInterrupt:
            print(colors.FAIL + colors.BOLD + "[ CTRL + C ] Detected !!!")
            print("Quiting ....")
            time.sleep(3)
            self.clear_terminal()
        except Exception as e:
            print("An Error Occurred")
            print(colors.BOLD + colors.FAIL + f" Error Type  : {e}")
            colors.ENDC
            time.sleep(2)
            self.clear_terminal()
    def menu(self):
        try:
            print(menu_server_port)
            while True:
                self.select = int(input(colors.BOLD + colors.OKGREEN + "Choose a Mail Server : "))
                if self.select<0 or self.select>4:
                    print(colors.FAIL + colors.BOLD + "No Such Value Found")
                else:
                    break
        except ValueError:
            print(colors.BOLD + colors.WARNING +"Cannot Contain Textual Expressions and Spaces")
            time.sleep(2)
            self.clear_terminal()
            self.menu()
        except KeyboardInterrupt:
            print(colors.FAIL + colors.BOLD + "[ CTRL + C ] Detected !!!")
            print("Quiting ....")
            time.sleep(3)
            self.clear_terminal()
        except Exception as e:
            print("An Error Occurred")
            print(colors.BOLD + colors.FAIL + f" Error Type  : {e}")
            time.sleep(2)
            self.clear_terminal()
    def config_server_name(self):
        if self.select == 0:
            self.server_name = SMTP_GMAIL_SERVER_NAME
            self.port = 587
        elif self.select == 1:
            self.server_name = SMTP_OUTLOOK_SERVER_NAME
            self.port = 587
        elif self.select == 2:
            self.server_name = SMTP_YAHOO_SERVER_NAME
            self.port = 465
        elif self.select == 3:
            try:
                self.server_name = str(input(colors.OKGREEN + colors.BOLD + "Please Enter a Mail Server Name : "))
                self.port = int(input(colors.OKGREEN + colors.BOLD +"Please Enter the Port Number of the Server Name You Entered : "))
            except ValueError:
                print(colors.BOLD + colors.WARNING + "Cannot Contain Textual Expressions and Spaces")
                time.sleep(2)
                self.clear_terminal()
                self.config_server_name()
            except KeyboardInterrupt:
                print(colors.FAIL + colors.BOLD + "[ CTRL + C ] Detected !!!")
                print("Quiting ....")
                time.sleep(3)
                self.clear_terminal()
            except Exception as e:
                print("An Error Occurred")
                print(colors.BOLD + colors.FAIL + f" Error Type  : {e}")
                time.sleep(2)
                self.clear_terminal()
        else:
            print(colors.BOLD + colors.WARNING + "Quiting ....")
            time.sleep(3)
            self.clear_terminal()
            colors.ENDC
            sys.exit()
    def mail_send_count(self):
        try:
            print(menu_message_count)
            while True:
                while True:
                    self.amount_message = int(input(colors.OKGREEN + colors.BOLD + "Please Send Message Amount : "))
                    if self.amount_message < 0 or self.amount_message > 6:
                        print("Please choose between 0 and 6")
                    else:
                        break
                if self.amount_message == 0:
                    self.amount_message = 500
                elif self.amount_message == 1:
                    self.amount_message = 400
                elif self.amount_message == 2:
                    self.amount_message = 300
                elif self.amount_message == 3:
                    self.amount_message = 200
                elif self.amount_message == 4:
                    self.amount_message = 100
                elif self.amount_message == 5:
                    while True:
                        self.amount = int(input(colors.OKGREEN + colors.BOLD + "Please Send Message Amount (Max : 500 , Min : 1) : "))
                        if self.amount < 1 or self.amount > 500:
                            print(colors.BOLD + colors.WARNING + "The number of Messages to be sent is maximum 500, at least 1 piece.")
                            self.amount = int(input(colors.OKGREEN + colors.BOLD + "Please Send Message Amount (Max : 500 , Min : 1) : "))
                        else:
                            self.amount_message = self.amount
                            break
                else:
                    self.amount_message = 0
                break

            print(self.amount_message)
        except ValueError:
            print(colors.BOLD + colors.WARNING + "Cannot Contain Textual Expressions and Spaces")
            time.sleep(2)
            self.clear_terminal()
            self.send_config()
        except KeyboardInterrupt:
            print(colors.FAIL + colors.BOLD + "[ CTRL + C ] Detected !!!")
            print("Quiting ....")
            time.sleep(3)
            self.clear_terminal()
        except Exception as e:
            print("An Error Occurred")
            print(colors.BOLD + colors.FAIL + f" Error Type  : {e}")
            time.sleep(2)
            self.clear_terminal()
    def send_config(self):
        try:
            self.server = smtplib.SMTP(self.server_name, self.port)
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.fromAddress, self.fromPassword)
        except Exception as e:
            print("An Error Occurred")
            print(colors.BOLD + colors.FAIL + f" Error Type  : {e}")
            time.sleep(2)
            self.clear_terminal()
            print()
            print(self.server_name,self.port)
            print(self.fromAddress, self.fromPassword)
            sys.exit()
    def attack(self):
        for i in range(self.amount_message +1):
            self.server.sendmail(self.fromAddress,[self.target],self.message)
            MailSend.count +=1
            print(f"\rSending Mail Number : {MailSend.count}")
        self.server.close()
    def clear_terminal(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        else:
            pass
a = MailSend()
a.config_server_name()
a.mail_send_count()
a.send_config()
a.attack()