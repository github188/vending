from django.db import models
# docs.djangoproject.com/en/1.10/ref/models/fields/
# docs.djangoproject.com/en/1.10/ref/contrib/admin/#modeladmin-options
# github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
