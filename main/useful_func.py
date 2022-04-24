from .const import first_level
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def get_needed_exp(level):
	if level < 1 or not isinstance(level, int):
		raise ValueError("Неверный формат уровня")
	if level == 1:
		return first_level
	return round(first_level * 1.15**(level - 1))


def email_is_valid(email: str):
	# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	return re.fullmatch(regex, email)


def send_mail(mail, text):
	addr_from = "programming.agent@yandex.ru"
	password = "ecovachexwuyiiij"

	msg = MIMEMultipart()
	msg['From'] = addr_from
	msg['To'] = mail
	msg['Subject'] = 'Game agent'

	msg.attach(MIMEText(text, 'plain'))
	try:
		server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
		server.login(addr_from, password)
		server.sendmail(addr_from, mail, msg.as_string())
		server.quit()
		return None
	except Exception as e:
		return f"error: {e}"
