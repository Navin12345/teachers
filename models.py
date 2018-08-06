from django.db import models

class teacher_info(models.Model):
    teachers_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=40, default=0)
    lastname = models.CharField(max_length=40,default=0, blank =True)
    subject = models.CharField(max_length=40,default=0)
    classes = models.CharField(max_length=40,default=0)
    photo = models.CharField(max_length=100,default=0, blank =True)
    coaching_name = models.CharField(max_length=40,default=0, blank =True)
    about = models.CharField(max_length=250,default=0, blank =True)
    qualification = models.CharField(max_length=250,default=0, blank =True)
    area = models.CharField(max_length=40,default=0)
    pincode = about = models.CharField(max_length=10,default=0)
    goal = models.CharField(max_length=50,default=0, blank =True)
    rating = models.IntegerField(default=0, blank =True)

    class Meta:
        db_table = 'classcast_teacher_info'

    def __str__(self):
        return u'%s-%s' % (str(self.firstname), str(self.area))