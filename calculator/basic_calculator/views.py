from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from .forms import ContactForm

AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"

# Create your views here.
class AddView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01+num02)

class SubView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 - num02)

class DivView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)

class MultiView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 * num02)


def home(request):
    return render(request, 'home.html')


# def contact(request):
#     return HttpResponse('contact view')

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
        print(name, email)
    form = ContactForm()
    return render(request, 'form.html', {'form': form})



def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False
