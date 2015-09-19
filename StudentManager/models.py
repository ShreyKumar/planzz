from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_of = models.IntegerField()
    lectures = models.ManyToManyField('Lecture')

    def __unicode__(self):
        return self.name + ' from class of ' + class_of


class Lecture(models.Model):

    def __unicode__(self):
        pass

class Tutorial(models.Model):
    def __unicode__(self):
        pass
