from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
import smtplib, uuid, datetime
from help.email import send
from django.contrib import messages
from help.decorators import is_login
from .models import Token
from django.urls import reverse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
@is_login
def get_token(request):
    if request.POST:
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user.exists():
            token = uuid.uuid4()
            now = datetime.datetime.now()
            hours = datetime.timedelta(hours = 6)
            
            time =  now + hours
            time = int(time.timestamp())

            html = """\
            <html>
                <head></head>
                <body>
                    <p>Halo!<br>
                    Kamu ingin mengubah kata sandi?<br>
                    <a href="{}">klik disini</a>
                    untuk melanjutkan. Jika kamu tidak merasa melakukan hal ini abaikan saja.
                    </p>
                </body>
            </html>
            """.format(request.build_absolute_uri(reverse('set_password', kwargs={'token':token})))
            send(email, html)
            data = {
                'email': email,
                'token': token,
                'expired': time
            }
            Token.objects.create(**data)
            messages.success(request, 'Kami telah mengirim informasi ke alamat email {}'.format(email))
            return redirect('login')
        else:
            messages.error(request, 'Email tidak terdaftar!')
            return redirect('login')
    else:
        return redirect('login')
        
        
@is_login
def change(request, token):
    o = Token.objects.filter(token=token)
    if o.exists():
        if request.POST:
            password = request.POST['password1']
            if len(password) < 6:
                messages.error(request, 'Password min. 5 karakter')
                return redirect('set_password',token=token)
            else:
                get = Token.objects.get(token=token)
                u = User.objects.get(email=get.email)
                u.set_password(password)
                u.save()
                o.delete()
                messages.success(request, 'Password berhasil diubah, silahkan masuk!')
                return redirect('login')
        else:
            konteks = {
                'token': token
            }
            return render(request, "set_password.html", konteks)
    else:
        messages.error(request, 'Token yang anda masukkan mungkin sudah kadaluwarsa!')
        return redirect('login')