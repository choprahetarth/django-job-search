from django.db import models
from django.contrib.auth.models import User # this is the user model which is used to link 
# the creator to the jobs

# Create your models here.


class Job(models.Model):
    '''
    - Position Name 
    - Text Description
    - Age Criteria
    - Salary
    - No. of Openings
    '''
    position_name = models.CharField(max_length=100)
    text_description = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary = models.IntegerField()
    n_openings = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE) # model.CASCADE allows us to delete all the jobs a user has created once the user is deleted.

    def __str__(self):
        '''
        Change job_object (2) to self.position_name http://127.0.0.1:8000/admin/jobs/job/2/change/
        '''
        return self.position_name

