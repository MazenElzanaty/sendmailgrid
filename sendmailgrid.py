import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='no-reply@code95.info',
    to_emails='mazen.elzanaty@rootgate.com',
    subject='Testing mail from api',
    html_content='<strong>and ea sdajasndjsa sy to do anywhere, even with Python</strong>')
try:
     SENDGRID_API_KEY=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
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)