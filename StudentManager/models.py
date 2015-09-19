from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_of = models.IntegerField()
    lectures = models.ManyToManyField('Lecture')

    def __unicode__(self):
        return self.name + ' from class of ' + class_of


class Lecture(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=30)
    times = models.CharField(max_length=100)
    website = models.URLField()
    tutorial = models.ForeignKey('Tutorial')


    def __unicode__(self):
        return self.name

    def get_students(self):
        return self.student_set.all()

class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
