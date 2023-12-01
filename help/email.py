from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.contrib.auth.models import User

def send(email,text):
    username = User.objects.get(email=email).username
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "Ganti Kata Sandi"
    html_content = text
    sender = {"name":"Kawoola","email":"admin@kawoola.com"}
    to = [{"email":email,"name":username}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


