# =========================
# 7. app/utils/emailer.py (Email professionnel)
# =========================

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, job_id, cv_link, cover):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = "recruiter@example.com"
    msg['Subject'] = "Candidature – Poste en cybersécurité"
    
    body = f"""
    Bonjour,

    Veuillez trouver ci-joint ma candidature pour le poste mentionné.

    {cover}

    CV: {cv_link}
    """
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email", "your_password")
    text = msg.as_string()
    server.sendmail(sender_email, "recruiter@example.com", text)
    server.quit()
    
