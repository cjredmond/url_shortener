from django.db import models
import random

class Link(models.Model):
    url = models.URLField(max_length = 250)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length = 40)

    def __str__(self):
        return self.title


    def new_link(self):
        letter = ["a", "b", "c"]
        randomindex = random.randint(0,len(letter)-1)
        rand_letter = letter[randomindex]
        random_num = random.randint(1,5)
        stuff = str(rand_letter * random_num)
        #new_url = str("http://localhost:8000/pass/" + stuff)
        return stuff
