import smtplib
import imghdr
from email.message import EmailMessage
password = "swpjkufxvuybupmv"
SENDER = "manitarious@gmail.com"
RECEIVER = "manitarious@gmail.com"
def send_email(image_path):
	email_message = EmailMessage()
	email_message["Subject"] = "Movement Report"
	email_message.set_content("We discovered a movement in your area")

	with open(image_path, "rb") as f:
		content = f.read()
	email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None , content))

	gmail = smtplib.SMTP("smtp.gmail.com", 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(SENDER, password)
	gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
	gmail.quit()


