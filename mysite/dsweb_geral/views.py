from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'dsweb/templates/index.html',context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'dsweb/templates/detail.html',{'question':question})

def results(request, question_id):
    response = "Resultados da questão %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "Votação para a questão %s."
    return HttpResponse(response % question_id)