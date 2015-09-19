from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_of = models.IntegerField()
    lectures = models.ManyToManyField('Lecture')

    def __unicode__(self):
        return self.name + ' from class of ' + self.class_of


class Lecture(models.Model):

    l_name = models.CharField(max_length = 100)
    l_code = models.CharField(max_length = 10)
    l_instructor = models.CharField(max_length = 100)
    l_cCapacity = models.IntegerField()
    l_mCapacity = models.IntegerField()
    l_pCapacity = (l_cCapacity / l_mCapacity) * 100
    


    def __unicode__(self):
        return self.l_name + ' has a lecture code of ' + self.l_code + ' with instructor ' + self.l_instructor + ' with a current capacity' + self.l_cCapacity + '/' + self.l_mCapacity + ' at ' + self.l_pCapacity

class Tutorial(models.Model):

    t_name = models.CharField(max_length=100)
    t_code = models.CharField(max_length=10)
    t_instructor = models.CharField(max_length=100)
    t_cCapacity = models.IntegerField()
    t_mCapacity = models.IntegerField()
    t_pCapacity = (t_cCapacity / t_mCapacity) * 100

    t_sTime = models.CharField(max_length=10)
    t_length = models.IntegerField()
    t_Day = models.CharField(max_length=15)

    def __unicode__(self):
        return self.t_name + ' has a tutorial code of ' + self.t_code + ' with instructor ' + self.t_instructor + ' with a start time ' + self.t_sTime + ' on ' + self.t_Day + ' for ' + self.t_length + ' and is currently filled at ' + self.t_cCapacity + '/' + self.t_mCapacity + ' with a % of ' + self.t_pCapacity + '%'
