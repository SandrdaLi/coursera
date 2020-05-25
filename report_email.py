#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib
import reports
import sys

def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    # Making attachment_path optional, if the attachment variable is empty string, no email will be sent.
    if not attachment_path == "":
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)
    return message

def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def main(argv):
    path = "/home/student-04-73a4303be165/supplier-data/descriptions/"
    dirs = os.listdir( path )

    table_data=[]
    for item in dirs:
        i = 0
        name = ['name', 'weight']
        fruits = []
        with open(path+item) as f :
            lines = f.readlines()
        for i in range(len(name)):
            fruits.append(name[i] + ": " + lines[i])
        table_data.append(fruits)
    print(table_data)

    attachment="/tmp/processed.pdf"
    title="Processed Updated on March 11, 2020"
    reports.generate(attachment, title, table_data)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    send(message)

if __name__ == "__main__":
    main(sys.argv)
