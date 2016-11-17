from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    hrefDict = [
                {"name":"ADMIN", "href":"/admin_omd"},
                {"name":"API", "href":"/api/list/"}]
    context = {
        "hrefDict":hrefDict,
    }
    return render(request, "index.html", context)

@login_required
def apiIndex(request):
    hrefDict = [
        {"name": "HOME", "href": "/"},
        {"name": "MoneyCharge", "href":"/api/data/moneycharge/"},
        {"name": "USERS", "href": "/api/data/users/"},
        {"name": "Groups", "href": "/api/data/groups/"},
    ]
    context = {
        "hrefDict":hrefDict
    }
    return render(request, "apiIndex.html", context)