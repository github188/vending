from django import forms

from localomddata.models.product import Product


class ProductTextForm(forms.ModelForm):
    productSummary = forms.CharField(widget=forms.Textarea)
    productDesc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Product
        fields = [
            "provider","productName", "productNo", "category", "orderUnitPrice","orderCount", "orderCountUnit", "saleUnitPrice",
            "imageRefUrl", "imageListUrl", "imageDetailUrl", "productSummary", "productDesc",
            "orderByUser", "orderTime", "isActive",
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