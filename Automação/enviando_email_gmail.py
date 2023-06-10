import os
import smtplib
from email.message import EmailMessage

# configurar email e senha
Email_Endereço = ''
Email_Senha = ''


#  configurar emailstori
msg = EmailMessage()
msg['Subject'] = ''
msg['from'] = ''
msg['to'] = ''
msg.set_content('mensagem')

# enviar
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # 465 é a porta
    smtp.login(Email_Endereço, Email_Senha)
    smtp.send_message(msg)