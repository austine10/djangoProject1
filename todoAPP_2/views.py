from django.http import HttpResponse, HttpResponseRedirect
from django.middleware import csrf
from django.shortcuts import render
from django.template.defaulttags import csrf_token

from todoAPP_2.models import my_notes


def home(request):
    print("home loaded....")
    notes = my_notes.objects.all().order_by('subject')
    print(notes)
    return render(request, 'page_2.html', {'notes': notes})


def page_2(request):
    print("page 2")
    subjects = request.GET['subject']
    insert = my_notes.objects.create(subject=subjects,description="desc")
    print(insert.id)

    return HttpResponseRedirect('/')


def base(request):

    subject = request.GET['subject']
    print(subject)
    notes = my_notes.objects.all().order_by('subject')
    print(notes)
    return render(request, 'base.html', {'notes':notes})


def delete(request,my_note_id):
    note_delete = my_notes.objects.get(id=my_note_id).delete()
    return HttpResponseRedirect("/")
