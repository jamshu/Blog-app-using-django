from django.db import models
import datetime

class Newblogposts(models.Model):
    title = models.TextField()
    body = models.TextField()
    day = models.TextField()
    updated_time = models.DateTimeField(default=datetime.datetime.now())
    def __unicode__(self):
        return self.title
        
class Comments(models.Model):
    name = models.TextField()
    comment = models.TextField()
    title = models.TextField()

    def __unicode__(self):
        return self.name
