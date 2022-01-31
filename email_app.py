import smtplib
from email.message import EmailMessage
import ssl


subject = 'Test'
sender = 'aforanupn@gmail.com'
receiver = 'aforanupn@gmail.com'
password = 'amazeme123'
content = 'This is a test message'

message = EmailMessage()
message['Subject'] = subject
message['To'] = receiver
message['From'] = sender
message.set_content(content)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message, message.as_string())
