from django.db import models
import datetime

# Create your models here.

class Poll(models.Model):
    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __unicode__(self):
        return self.Choice

    poll = models.ForeignKey(Poll)
    Choice = models.CharField(max_length=200)
    votes = models.IntegerField()


