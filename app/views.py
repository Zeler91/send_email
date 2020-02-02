from django.shortcuts import render
from app.models import Mailer
from app.forms import MailerForm
from django.views.generic import CreateView, ListView
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.template import loader
from django.urls import reverse_lazy  
from django.core.mail import BadHeaderError, send_mail
import threading
import time

class MailView(CreateView):
    model = Mailer
    form_class = MailerForm
    template_name = "index.html"
    success_url = '/mails_list/'  


    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     # threads = []
    #     # for mail in Mailer.objects.all():
    #     #     if not mail.sended:
    #     #         t = threading.Thread(target=form.send_email, args=(self.request,))
    #     #         threads.append(t)
    #     #         t.start()
    #     # for t in threads:
    #     #     t.join()
    #     # form.send_email(self.request)
    #     return super().form_valid(form)

def send_email(mail):
    subject =  mail.subject
    message = mail.message
    to_email = mail.to_email
    delay = mail.delay
    if subject and message and to_email and delay:
        try:
            print("Email {} will send after {} seconds".format(subject, delay))
            time.sleep(delay)
            mail.sended = True
            mail.save()
            if Mailer.objects.all().count() > 15:
                print('You reach the limit of mails')
            else:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])
                print("Email {} sended".format(subject))
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')



def mails_list(request):
    template = loader.get_template('mails_list.html')
    mails = Mailer.objects.all()
    mails.order_by('delay')
    mails_count = mails.count()
    threads = []
    max_mails = mails.count() - 10
    if max_mails < 0:
        max_mails = 0
    if mails_count > 10:
        mails_count = 10
    for mail in mails:
        if not mail.sended:
            t = threading.Thread(target=send_email, args=(mail,))
            threads.append(t)
            t.start()
    
    mails_data = {
        "title": "Last {} mails".format(mails_count),
        "mails": mails[max_mails:],
    }
    return HttpResponse(template.render(mails_data, request))    

    for t in threads:
        t.join()
