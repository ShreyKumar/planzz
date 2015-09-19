from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_of = models.IntegerField()
    lectures = models.ManyToManyField('Lecture')

    def __unicode__(self):
        return self.name + ' from class of ' + self.class_of


class Lecture(models.Model):

    def __unicode__(self):
        pass

class Tutorial(models.Model):

    t_name = models.CharField(max_length=100)
    t_code = models.CharField(max_length=10)
    t_instructor = models.CharField(max_length=100)
    t_capacity = models.IntegerField()
    t_sTime = models.CharField(max_length=10)
    t_Day = models.CharField(max_length=15)

    def __unicode__(self):
        return self.t_name + ' has a tutorial code of ' + self.t_code + ' with instructor ' + self.t_instructor + ' with a start time ' + self.t_sTime + ' on ' + self.t_Day
