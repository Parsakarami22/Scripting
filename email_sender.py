import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Python Developer"
email["to"] = "youremail@gmail.com"
email["subject"] = "You won a dollar!"

email.set_content(html.substitute({"name":"Python"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login("myemail@gmail.com", "mypassword")
  smtp.send_message(email)
  print("all done!")
  
