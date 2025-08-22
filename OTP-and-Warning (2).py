import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime  import date, time, datetime
import time
import sys
timeexcep = int(300)
t = datetime.now()
p = t.strftime("%X")
onlyminute = t.minute
name = "GENERATION-X"
class Email_Notificaiton:

    def __init__(self):
        self.otp = random.randint(1000,9999)
        self.subj = "Message from Generation X ["+p+"]"
        self.message_body = "Hello User!!!\n" + name + "\nTo authenticate, please use the following One Time password(OTP)\n" + str(self.otp) + "\nIf you require any assistance, please contact" \
                                                                                                          " our 24 hr Customer Service"
    def OTP_MESSAGE(self):
        self.fromaddr = "checkotp04@gmail.com"
        self.password = "generationxpass"
        self.toaddr = "samsungadg123@gmail.com"
        p = t.strftime("%X")
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = self.subj
        self.body = self.message_body
        msg.attach(MIMEText(self.body, 'plain'))
        self.filename = "test.png"
        attachment = open(self.filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % self.filename)
        msg.attach(p)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr,self.password)
        text = msg.as_string()
        server.send_message(msg)
        server.quit()

    def funct(self):
        timew = 1
        while(True):
            if timew > 3:
                print("Maximum limit reached!\nThis action will be reported to the email owner!!!!")
                complain_notification()
                break
            inital = time.time()
            inp = str(input(f"{timew}). Enter the OTP: "))
            orginaltime = time.time() - inital
            timew = timew + 1
            if orginaltime > float(timeexcep):
                print("Time Exceed!!!!!!!!!!\nOTP Can't be verified!")
                sys.exit()
            elif orginaltime < float(timeexcep):
                if inp == str(self.otp):
                    print("OTP Verified!!!!")
                    return True
                elif inp != str(self.otp):
                    print("Wrong OTP!!!")
                    continue
if __name__ == '__main__':
    def complain_notification():
        obj_complain = Email_Notificaiton()
        subj_complain = "SECURITY WARNING FROM Generation X!!!!!!!!!!!!!!!!!!!!!! ["+p+"]"
        message_complain =  "Hello User!!!\n" +name+ "\nAn unusual activity has been found\nSome one is trying to use your account!\nKindly change your password!!!!!"
        obj_complain.subj=subj_complain
        obj_complain.message_body=message_complain
        obj_complain.OTP_MESSAGE()

    objnotify = Email_Notificaiton()
    objnotify.OTP_MESSAGE()
    objnotify.funct()
