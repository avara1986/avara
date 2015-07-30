# encoding: utf-8
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse
from google.appengine.api import mail
from google.appengine.api import taskqueue

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
