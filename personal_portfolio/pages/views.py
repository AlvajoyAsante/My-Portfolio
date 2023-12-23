from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {
        'Firstname': 'Alvajoy',
        'Lastname': 'Asante',
        'Fullname': 'Alvajoy Asante',
        'Phonenumber': '(980) 288-4855',
        'Email': 'aasante@charlotte.edu',
        'Location': 'University of Charlotte, Charlotte, NC',
        'Sitename': 'mywebsite.com',
        'Occupation': 'Aspiring Software Engineer',
        'LinkedIn': 'https://www.linkedin.com/in/alvajoy-asante/',
        'Github': 'https://github.com/Overload02',
        'Sitename': 'Alvajoy Asante',
    }

    return HttpResponse(render(request, "pages/home.html", context))
    # return HttpResponse("Hello Viewers! We are testing how traffic is split")
