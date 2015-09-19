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




class Course(models.Model):
    name = models.CharField('Lecture Name', max_length=300)
    code = models.CharField('Lecture Code', max_length=30)
    # make custom field for lecture sessions and times
    website = models.URLField('Lecture Website', blank=True)
    tutorial = models.OneToOneField('Tutorial')
    students = models.ManyToManyField(Student)
    max_enrolment = models.IntegerField(default=50)
    current_enrolment = models.IntegerField(blank=True)
    instructor = models.CharField(default='TBA')

    def __unicode__(self):
        return self.name

    def get_students(self):
        return self.students.all()

    def save(self, *args, **kwargs):
        self.current_enrolment = self.student_set.count()
        super(Lecture, self).__init__(*args, **kwargs)

class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField('Tutorial Session')
    # make custom field for lecture sessions and time
    students = models.ManyToManyField(Student)
    max_enrolment = models.IntegerField(default=30)
    TA = models.CharField(default='TBA')

    def save(self, *args, **kwargs):
        pass

    def __unicode__(self):
        return self.name
