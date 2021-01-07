### This will send the email to "TO" and "CC" email id with attachment and email body in the form of table ######

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime

attachment='/location/of/the/attachment'

#######################Email Function #############################
def py_mail(SUBJECT, BODY, TO, CC, FROM):
    """With this function we send out our html email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    rcpt = CC.split(",")  + [TO]
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['Cc'] = CC
    MESSAGE['From'] = FROM


    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
    att1 = MIMEApplication(open(attachment,'rb').read())
    att1.add_header('Content-Disposition', 'attachment', filename="Linux_inventory.xlsx")	## Provide the attachment location
    MESSAGE.attach(att1)

    # The actual sending of the e-mail
    server = smtplib.SMTP('myrelay.email.com:25')						## provide the email relay address

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "mypassword"

    server.starttls()
   # server.login(FROM,password)
    server.sendmail(FROM, rcpt, MESSAGE.as_string())
    server.quit()


###################################################################

host = "myServer.com"
IP_ADDRESS = "10.10.10.10"


email_content = """
        <h2><u>Capacity calculation """ + str(application) + """</u></h2>
        <head>
          <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
          <title>html title</title>
          <style type="text/css" media="screen">
            table{
                background-color: white;
                empty-cells:hide;
                 border-collapse: collapse;
            }
            td.cell{
                background-color: white;
                border: 2px solid black;
            }
          </style>
        </head>
        <body>
          <table border=2 class="table"><tr ><td bgcolor="#96D6F0">&nbsp;&nbsp;&nbsp;&nbsp;Hostname &nbsp;&nbsp;&nbsp;&nbsp;</td><td bgcolor="#96D6F0">&nbsp;IP ADDRESS </td></tr>"""
email_content += """<tr><td>&nbsp;""" + str(host) + """&nbsp;</td><td>&nbsp;""" + str(IP_ADDRESS) """&nbsp;</td></tr>"""

email_content += """</table>
        </body>
        """



TO = "ID1@email.com,ID2@email.com"
CC = "manager1@email.com,manager2@email.com"
FROM ='myEmail@email.com'
SUBJECT = "HOST and IP Details for  " + str(datetime.datetime.now().strftime("%d-%m-%Y"))
py_mail(SUBJECT, email_content, TO, CC, FROM)
