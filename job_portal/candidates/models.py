from django.db import models


GENDER_MALE = 'male'
GENDER_FEMALE = 'female'
GENDER_CHOICES = {
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
}
# Create your models here.

class Candidates(models.Model):
    '''
    - Name
    - Age
    - Gender
    - Mobile
    - City
    - Salary Expectations
    - Are they willing to relocate?
    '''
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_MALE)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    expected_salary = models.IntegerField()
    willing_relocate = models.BooleanField(default=False)

    def __str__(self):
        return self.name