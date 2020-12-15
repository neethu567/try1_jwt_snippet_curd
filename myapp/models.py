from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    title=models.CharField(max_length=256,null=False,blank=False)


class Snippet(models.Model):
    snippet=models.CharField(max_length=256,null=False,blank=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    created_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.id)