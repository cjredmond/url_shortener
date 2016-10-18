from django.db import models
import random

class Link(models.Model):
    url = models.URLField(max_length = 250)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150, null=True, blank=True)
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length = 40)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



    @property
    def count(self):
        return sum([hit_obj.count for hit_obj in self.hit_set.all()])


class Hit(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link)
    clicked = models.BooleanField()


    @property
    def count(self):
        if self.clicked:
            return 1
