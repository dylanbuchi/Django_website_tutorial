from django.http import HttpResponse

# Create your views here.


def hello(request):

    response = HttpResponse()
    response.set_cookie('dj4e_cookie', 'fc1f073f', max_age=1000)

    return response
