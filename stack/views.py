from django.shortcuts import render

from django.http import HttpResponse

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    logger.debug("dasgsdgds")
    # try:
    #     print("Sdgsdg")
    #     raise ValueError("Custome value error.")
    # except Exception as e:
    #     logger.exception(e)
    logger.debug("sdgsdgds")
    return HttpResponse("Hello, world. You're at the ELK stack index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def my_view(request, arg1, arg):
    ...
    if bad_mojo:
        # Log an error message
        logger.error('Something went wrong!')