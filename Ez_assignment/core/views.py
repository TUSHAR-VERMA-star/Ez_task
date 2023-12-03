from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse,JsonResponse
import json
# Create your views here.


def Home(request):

    files = Database.objects.all()
    return render(request, "core/home.html", {'files':files, 'name':"tushar"})


def download_file(request, file_id):
    my_file = get_object_or_404(Database, pk=file_id)
    response = FileResponse(my_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{my_file.file.name}"'
    return response


def download_file_api(request, file_id):
    if(request.user.is_authenticated):
        print("yes")
        my_file = get_object_or_404(Database, pk=file_id)
        url = my_file.file.url
        data = {'download-link': url, 'message': 'success'}
        return JsonResponse(data)

    return HttpResponse("sorry login first")
