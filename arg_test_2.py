import sys
import os
import json
import random
import requests
import smtplib
import base64

PACKAGES = '/Volumes/Shared/Brud/west/repos/pipe_utils/packages.yml'

class Release:
    def __init__(self):
        print('Package Release Protocol')

    def email_notifications(self, pkg_name, release_name, release_description, e_usrname, e_psword):
        
        receivers = ['sheena.boone@gmail.com', 'sheena.boone@dapperlabs.com']
        
        print('Sending email notifications')
        # mail server settings
        server_address = 'smtp.gmail.com'
        server_port = 465
        server = smtplib.SMTP_SSL(server_address, server_port)
        # user credentials
        username = e_usrname
        password = e_psword
        #username = (base64.b64encode(e_usrname.encode("utf-8"))).decode("utf-8")
        #password = (base64.b64encode(e_psword.encode("utf-8"))).decode("uff-8")
        try:
            #server login
            server.login(username,password)
            # email subject and text
            msg = 'Subject: {}-{}\n\n{}'.format(pkg_name, release_name, release_despcription)
            # send email
            server.sendmail(username, receivers, msg)
            server.quit()
            print("Email Sent!")
            # comma-separated string, send email to
        except SMTPResponseException as e:
            error_code = e.smtp_code
            error_message= e.smtp_error
            print (f'Error: {error_code}: {error message}')
        
        
#     def slack_notifications(self, pkg_name, release_name, release_description):
#         print('Sending slack notifications')
#         url = "https://hooks.slack.com/services/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"
#         message = (release_description)
#         title = (f'{pkg_name}-{release_name} :zap:')
#         slack_data = {
#             "username": "NotificationBot",
#             "icon_emoji": ":satellite:",
#             #"channel" : "#somerandomcahnnel",
#             "attachments": [
#                 {
#                     "color": "#9733EE",
#                     "fields": [
#                         {
#                         "title": title,
#                         "value": message,
#                         "short": "false",
#                         }
#                     ]
#                 }
#             ]
#         }
#         byte_length = str(sys.getsizeof(slack_data))
#         headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
#         response = requests.post(url, data=json.dumps(slack_data), headers=headers)
#         if response.status_code != 200:
#             raise Exception(response.status_code, response.text)

    def pull_to_disk(self):
        print('Pulling to disk')


def run(pkg_name, release_name, release_description, e_usrname, e_psword):
    print('Release: add package release')
    pkg_rel = Release()

    # Send email notifications
    pkg_rel.email_notifications(pkg_name, release_name, release_description, e_usrname, e_psword)

    # Send slack notifications
    # pkg_rel.slack_notifications(pkg_name, release_name, release_description)

    # Pull to disk
    pkg_rel.pull_to_disk()

    
if __name__=="__main__":
    print('INCOMING FROM GITHUB: %s %s' % (sys.argv[1], sys.argv[2]))
    string_arg = ''.join(sys.argv[2])
    rsl_notes = string_arg.replace('\\r',"").replace('\\n','\n')    
    
    e_usrname = os.environ['EMAIL_USER']
    e_psword = os.environ['EMAIL_PSWORD']
    pkg_name = os.environ['PACKAGE_NAME']
    #print (pkg_name)
    #print (type(e_usrname))
    #print (e_usrname)
    run(pkg_name, sys.argv[1], rsl_notes, e_usrname, e_psword)
