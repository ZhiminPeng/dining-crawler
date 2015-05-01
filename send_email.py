
import json

data = []
with open('items.jl') as f:
    for line in f:
        data.append(json.loads(line))


def send_mail(title, message):
    print "Sending mail.........."
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    # my send email address
    fromaddr = 'zhiminp@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com:587')
    # receivers
    # toaddrs = 'linjian5477@gmail.com' #'zhimin.peng@math.ucla.edu'
    # toaddrs = ['zhimin.peng@math.ucla.edu']

    toaddrs = ['zhimin.peng@math.ucla.edu',
               'linjian5477@gmail.com', 'kyuan.ustc@gmail.com',
               'wuty07@gmail.com',
               'basca.yan@gmail.com']

    username = 'zhiminp@gmail.com'
    password = 'freebird.1'
    server.ehlo()
    server.starttls()
    server.login(username, password)

    # message for email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ' ,'.join(toaddrs)
    msg['Subject'] = title

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddrs, text)
    server.quit()
    print "Mail sent"

title = 'Dining Hall summary for today.'
message = ""
for item in data:
    if len(item['favor']) > 0:
        message = message + item['hall_name'] + \
            " has " + ", ".join(item['favor']) + \
            ". Here is the link for the full menu \n" + item['link'] + "\n"


if len(message) > 0:
    send_mail(title, message)
else:
    message = "Nothing is good for today.\n"
    message = message + "Please checkout the following websites \
to see if there are sth you like.\n"
    for item in data:
        message = message + item['hall_name'] + "\n" + item['link'] + "\n"
    message = message + "Email me your favorite\
 dishes so that I can add them to the list."
    send_mail(title, message)
