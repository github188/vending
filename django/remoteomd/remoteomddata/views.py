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
        {"name": "首页", "href": "/"},
        {"name": "充值", "href":"/api/data/moneycharge/"},
        {"name": "订单", "href": "/api/data/ordermain/"},
        {"name": "商品", "href": "/api/data/product/"},
        {"name": "商品分类", "href": "/api/data/productcategory/"},
        {"name": "供应商", "href": "/api/data/productprovider/"},
        {"name": "货道", "href": "/api/data/slot/"},
        {"name": "货道状态", "href": "/api/data/slotstatus/"},
        {"name": "售货机", "href": "/api/data/vendingmachine/"},
        {"name": "售货机类型", "href": "/api/data/vendingmachinetype/"},
        {"name": "用户", "href": "/api/data/user/"},
        {"name": "会员", "href": "/api/data/member/"},
        {"name": "分组", "href": "/api/data/group/"},
        {"name": "配置", "href": "/api/data/config/"},
        {"name": "硬币变更", "href": "/api/data/coinchangelog/"},
    ]
    context = {
        "hrefDict":hrefDict
    }
    return render(request, "apiIndex.html", context)