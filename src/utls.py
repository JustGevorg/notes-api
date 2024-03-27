from email.message import EmailMessage
from config import SMTP_USER


def create_email(data: str):
    email = EmailMessage()
    email['Subject'] = f'Fastapi app'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(data)

    return email
