from django.db import models

class Mailer(models.Model):
    to_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField() 
    delay = models.PositiveSmallIntegerField()
    sended = models.BooleanField(default=False)  

    @classmethod
    def create(cls, to_email, message, delay):
        mail = cls(to_email=to_email, subject=subject, message = message, delay = delay)
        return mail

    def __str__(self):
        return self.subject

