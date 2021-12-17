from . import views
from django.urls import path

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

logger.error('Something went wrong! 2 urls')

urlpatterns = [
    path('', views.index, name='index'),
]