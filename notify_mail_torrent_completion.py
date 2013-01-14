#!/usr/bin/python
import sys
import smtplib
import datetime

from email.mime.text import MIMEText

# Event 'torrent complete' Deluge. The script to be executed will be
# supplied with three Torrent variables
torrent_id = sys.argv[1]
torrent_name = sys.argv[2]
torrent_save_path = sys.argv[3]

# Setting mail
smtp_srv = "smtp.gmail.com"
smtp_port = 587
smtp_user = "xxxxx@gmail.com"
smtp_pass = "xxxxx"

# Setting Message
mail_from = "xxxxx@yyyyy.com"
mail_to = "xxxxx@yyyyy.com"
mail_subject = "Torrent complete: %s " % torrent_name

# Setting conexion SMTP
mailServer = smtplib.SMTP(smtp_srv, smtp_port)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(smtp_user, smtp_pass)

# Make message
message = MIMEText("TorrentId = %s \nTorrentName = %s \nTorrentPath = %s \nDate = %s"
    % (torrent_id, torrent_name, torrent_save_path, datetime.datetime.now()))

message['From'] = mail_from
message['To'] = mail_to
message['Subject'] = mail_subject

# Send email
mailServer.sendmail(mail_from, mail_to, message.as_string())
mailServer.quit()
