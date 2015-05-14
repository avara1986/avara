# encoding: utf-8
from django.conf import settings
from django.utils import timezone
from google.appengine.api import mail
from google.appengine.api import taskqueue

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class SendToQueue(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        taskqueue.add(
            queue_name='mailqueue', url='/api/queue-send-mail/', method='GET')
        taskqueue.add(
            queue_name='mailqueue', url='/api/queue-send-mail/', method='GET')
        taskqueue.add(
            queue_name='mailqueue', url='/api/queue-send-mail/', method='GET')
        taskqueue.add(
            queue_name='mailqueue', url='/api/queue-send-mail/', method='GET')
        return Response("Oks")


class QueueSendMail(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        mail.send_mail(subject='Envío desde la cola', body='Envío desde la cola a las ' + str(timezone.now()),
                       sender=settings.EMAIL_HOST_USER, to='a.vara@gobalo.es')
        return Response("Oks")
