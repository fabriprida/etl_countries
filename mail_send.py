import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

def send_email(sender_email, password, receiver_email):
    subject = "Informe diario - Metricas de paises"
    body = "Adjunto se encuentra el archivo excel correspondiente al informe diario de los paises."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEBase("application", "octet-stream"))

    filename = "paises_con_metricas.xlsx"  
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part)

    text = msg.as_string()

    try:
        print("Connecting to the SMTP server...")
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        print("Connected to the SMTP server.")
    except Exception as e:
        print("An error occurred:", str(e))

    server.starttls()
    server.login(sender_email, password)  

    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully.")
    server.quit()
    return

def start_scheduling():
    schedule.every().day.at("08:00").do(send_email)
    while True:
        schedule.run_pending()
        time.sleep(1)