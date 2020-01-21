import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import base64
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import shutil

message = Mail(
    from_email=os.environ.get('FROM_EMAIL'),
    to_emails=os.environ.get('TO_EMAILS'),
    subject=os.environ.get('SUBJECT'),
    html_content='<strong>Build is finished, check attached</strong>')


shutil.make_archive('app', 'tar', os.environ.get('ATTACHMENT'))
with open('app.tar', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('app.tar'),
    FileType('application/tar'),
    Disposition('attachment')
)
message.attachment = attachedFile

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
