# encoding: utf-8
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse
from google.appengine.api import mail
from google.appengine.api import taskqueue

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


""" EJEMPLO: SendEmail

URL que mandaba tareas a colas

class SendToQueue(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        taskqueue.add(
            queue_name='mailqueue', url=reverse('queue-send-mail'), method='GET')
        taskqueue.add(
            queue_name='mailqueue', url=reverse('queue-send-mail'), method='GET')
        taskqueue.add(
            queue_name='mailqueue', url=reverse('queue-send-mail'), method='GET')
        taskqueue.add(
            queue_name='mailqueue', url=reverse('queue-send-mail'), method='GET')
        return Response("Oks")
"""
""""GoL: Game of Life

Recibe un JSON de un tablero de GoL y devuelve la siguiente generación
"""


class GoL(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        pass

""" EJEMPLO: SendEmail

URL que la clase "SendToQueue" mandaba a una cola de GAE.

class SendEmail(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        mail.send_mail(subject='Envío desde la cola', body='Envío desde la cola a las ' + str(timezone.now()),
                       sender=settings.EMAIL_HOST_USER, to='a.vara@gobalo.es')
        mail.send_mail(subject='Envío desde la cola', body='Envío desde la cola a las ' + str(timezone.now()),
                       sender=settings.EMAIL_HOST_USER, to='a.vara@gobalo.es')
        mail.send_mail(subject='Envío desde la cola', body='Envío desde la cola a las ' + str(timezone.now()),
                       sender=settings.EMAIL_HOST_USER, to='a.vara@gobalo.es')
        mail.send_mail(subject='Envío desde la cola', body='Envío desde la cola a las ' + str(timezone.now()),
                       sender=settings.EMAIL_HOST_USER, to='a.vara@gobalo.es')
        return Response("Oks")

"""
