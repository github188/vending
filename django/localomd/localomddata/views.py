from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    hrefDict = [{"name":"HOME", "href":"/"},
                {"name":"ADMIN", "href":"/admin_omd"},
                {"name":"API", "href":"/api/list/"}]
    context = {
        "hrefDict":hrefDict,
    }
    return render(request, "index.html", context)

def apiIndex(request):
    print('hello')
    hrefDict = [
        {"name": "HOME", "href": "/"},
        {"name":"MoneyCharge", "href":"/api/data/moneycharge/"},
    ]
    print(hrefDict.__len__())
    context = {
        "hrefDict":hrefDict
    }
    return render(request, "apiIndex.html", context)