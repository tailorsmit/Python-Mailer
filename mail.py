import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys,time

curr=1
total=1
full_progbar=1
sender_address = 'yourmailid@gmail.com'
sender_pass = 'yourpassword'

def progbar(cur, tota, full_progba):
	curr=cur
	total=tota
	full_progbar=full_progba
	frac = curr/total
	filled_progbar = round(frac*full_progbar)
	print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')
	time.sleep(0.5)


if len(sys.argv) == 1:
	#str=input("dallo")
	mail_content = input("Enter Message : ")
	#The mail addresses and password
	
	receiver_address = input("Enter To: ")
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = input("Enter Subject : ")
	#The subject line
	#The body and the attachments for the mail
	progbar(250,1000, 25)

	message.attach(MIMEText(mail_content, 'plain'))
	attachement=input("you want to attach files : ")
	if attachement=="Yes"or attachement=="yes"or attachement=="y" or attachement=="Y":
		noofattachment=int(input("Enter no. of  attachment : "));
	
		for i in range(noofattachment):
			attach_file_name = input("Enter Name of File : ")
			attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
			payload = MIMEBase('application', 'octate-stream')
			payload.set_payload((attach_file).read())
			encoders.encode_base64(payload) #encode the attachment
			#add payload header with filename
            #payload.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
			payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
			message.attach(payload)
			progbar(500,1000, 25)
			#Create SMTP session for sending the mail
			"""socks.setdefaultproxy(socks.HTTP, '172.16.3.1', 3128)
			socks.wrapmodule(smtplib)
			AUTHREQUIRED=1"""
		progbar(750,1000, 25)
		try:
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(sender_address, sender_pass) #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, receiver_address, text)
			session.quit()
			progbar(1000,1000, 25)
			print('Mail Sent')
		except SMTPException:
				print ("Error: unable to send email")
	else:
		progbar(500,1000, 25)
		#Create SMTP session for sending the mail
		"""socks.setdefaultproxy(socks.HTTP, '172.16.3.1', 3128)
		socks.wrapmodule(smtplib)
		AUTHREQUIRED=1"""
		progbar(750,1000, 25)
		try:
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login('mharsh6896@gmail.com', 'unnati301') #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, receiver_address, text)
			session.quit()
			progbar(1000,1000, 25)
			print('Mail Sent')
		
		except SMTPException:
			print ("Error: unable to send email")
else:
    receiver_address = sys.argv[1]
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = sys.argv[3]
    progbar(250,1000, 25)
    attach_file_name = sys.argv[2]
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    #payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    progbar(500,1000, 25)
	#Create SMTP session for sending the mail
    progbar(750,1000, 25)
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        progbar(1000,1000, 25)
        print(' Mail Sent')
    except SMTPException:
        print ("Error: unable to send email")
