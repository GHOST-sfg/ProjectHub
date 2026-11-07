from django.http import HttpResponse


def home(request):
    return HttpResponse("Project Management Tool is running!")

# Create your views here.
