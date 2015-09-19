from django.db import models

class Student(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    class_of = models.IntegerField()
    lectures = models.ManyToManyField('Lecture')
    friends = models.ManyToManyField('Friend')

    def __unicode__(self):
        return self.name + ' from class of ' + self.class_of
    def enroll(self, lecture):
        lecture.enrolled.push(self)
    def unenroll(self, lecture):
        for i in range(len(lecture.enrolled)):
            student = lecture.enrolled[i].id;
            if student == self.id:
                lecture.enrolled.pop(i)
    

class Lecture(models.Model):

    id = models.IntegerField() #id of the lecture
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 10)
    instructor = models.CharField(max_length = 100)
    cCapacity = models.IntegerField() #current capacity
    mCapacity = models.IntegerField() #max capacity
    pCapacity = (l_cCapacity / l_mCapacity) * 100
    enrolled = []
    

    def __unicode__(self):
        return self.l_name + ' has a lecture code of ' + self.l_code + ' with instructor ' + self.l_instructor + ' with a current capacity' + self.l_cCapacity + '/' + self.l_mCapacity + ' at ' + self.l_pCapacity

class Tutorial(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    instructor = models.CharField(max_length=100)
    cCapacity = models.IntegerField()
    mCapacity = models.IntegerField()
    pCapacity = (t_cCapacity / t_mCapacity) * 100

    sTime = models.CharField(max_length=10)
    length = models.IntegerField()
    Day = models.CharField(max_length=15)

    def __unicode__(self):
        return self.t_name + ' has a tutorial code of ' + self.t_code + ' with instructor ' + self.t_instructor + ' with a start time ' + self.t_sTime + ' on ' + self.t_Day + ' for ' + self.t_length + ' and is currently filled at ' + self.t_cCapacity + '/' + self.t_mCapacity + ' with a % of ' + self.t_pCapacity + '%'
