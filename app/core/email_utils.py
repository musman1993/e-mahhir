# app/core/email_utils.py

import aiosmtplib
from email.message import EmailMessage
from app.core.config import settings



async def send_email(
    subject: str,
    recipient_email: str,
    body: str,
    sender_email: str = settings.SMTP_USER,
):
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.set_content(body)

    try:
        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASSWORD,
            use_tls=True,
        )
    except Exception as e:
        print("Error sending email:", e)
        raise
