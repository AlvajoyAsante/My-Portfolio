from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'Firstname': 'Alvajoy',
        'Lastname': 'Asante',
        'Fullname': 'Alvajoy Asante',
        'Phonenumber': '704-733-7352',
        'Email': 'aasante@charlotte.edu',
        'Location': 'University of Charlotte, Charlotte, NC',
        'Sitename': 'mywebsite.com',
        'Occupation': 'Software Engineer',
        'LinkedIn': '',
        'Github': '',
        # 'Github': '',
    }

    return render(request, "pages/home.html", context)
