from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html', {'content':['value1', 'value2']})
