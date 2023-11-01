import smtplib
from email import encoders  # later on

# ordinary text we will be using for the mail
from email.mime.text import MIMEText

from email.mime.base import MIMEBase    # this will be used to send attachments

from email.mime.multipart import MIMEMultipart  # for the whole thing?

# basically we need to log in through the script on an existing gmail account, and then by using the SMTP protocol send emails
# from that account

# this is the address of the gmail/google smtp server, and the 25 is the port
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()  # this is used to start the server
server.starttls()  # this is used because google requires a secure connection, so we need to enable TLS encryption after connecting
# to the server

# This is the command that needs to be used in order to login, but having here our email and password is not secure at all
# server.login('mail@mail.com', 'password123')

# The best thing we could do is to use encryption but for now we can just save our password in another file and do this:
with open('password.txt', 'r') as f:
    emailPass = f.read()

    # What this does is that it opens a file with the name "password.txt." and then opens it in read mode 'r', then we give a name to
    # the file (the name f), and then we store the password to the "password" variable by using the .read() method which reads
    # the whole file (but in this case there is ONLY the password inside that file so it should work)

# and we're logged in
server.login('crazyjackal3@gmail.com', emailPass)

msg = MIMEMultipart()
# here the message variable is basically used as a dictionary with the keys of it being the important fields of
# where the mail is coming from, where is it going, and what's the subject of it
msg['From'] = 'Greg'
msg['To'] = 'gregorytsak3@gmail.com'
msg['Subject'] = 'Testing my Python Mail Client'

# Then for the actual mail content we will use a .txt file
with open('message.txt', 'r') as f:
    message = f.read()

# adding a text to our msg object/dictionary
# remember to use the message variable and NOT the message.txt file
msg.attach(MIMEText(message, 'plain'))

# here is the part of getting an image, decoding it into bytes, then using a steam to process image data and THEN attach it to the msg
filename = 'coding.jpg'
attachment = open(filename, 'rb')  # we need to use it read byte mode

# the stream used to process the image data. this variable is called a "payload" and a payload can be of various types (text, voice message
# etc) and in general the payload refers to the main content or data being transmitted within a MIME (Multipurpose Internet Mail Extension)
# message
p = MIMEBase('application', 'octet-stream')

# we set the previously made payload to read the image variable
p.set_payload(attachment.read())

encoders.encode_base64(p)  # encoding the image data
# adding a header to the p image attachment/file
p.add_header('Content-Disposition', f'attachment: filename = {filename}')

# Finally attaching the payload (the image file) to the message (msg variable)
msg.attach(p)

text = msg.as_string()  # converting the whole msg object/dictionary into string

# sending through the server the email
server.sendmail('crazyjackal3@gmail.com', 'gregorytsak3@gmail.com', text)
# the arguments are: 'email from', 'email to', 'type of email'

attachment.close()
server.quit()
