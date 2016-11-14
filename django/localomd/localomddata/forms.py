from django import forms

from pagedown.widgets import PagedownWidget

from .models import Product

class ProductTextForm(forms.ModelForm):
    productSumary = forms.CharField(widget=forms.Textarea)
    productDesc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Product
        fields = [
            "provider","productName", "category", "orderPrice","orderCount", "orderCountUnit", "orderTotalPrice", "productPrice",
            "imageRefUrl", "imageListUrl", "imageDetailUrl", "productSumary", "productDesc",
            "orderByUser", "isActive",
        ]

# class ProductForm(forms.ModelForm):
#     content = forms.CharField(widget=PagedownWidget(show_preview=False))
#     publish = forms.DateField(widget=forms.SelectDateWidget)
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "content",
#             "image",
#             "draft",
#             "publish",
#         ]