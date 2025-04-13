## 💌 `app/mailer.py`python
from email.message import EmailMessage
import aiosmtplib
import os

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

async def send_mail(to, subject, content, attachment=None):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(content)
    if attachment:
        msg.add_attachment(attachment["data"], filename=attachment["filename"], maintype="application", subtype="pdf")
    await aiosmtplib.send(msg, hostname="smtp.gmail.com", port=587, start_tls=True,
                          username=SMTP_USER, password=SMTP_PASSWORD)
