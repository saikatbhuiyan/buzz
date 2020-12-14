from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator



class Apply(models.Model):
  tsync_id = models.CharField(max_length=256, blank=True, null=True)
  name  = models.CharField(max_length=256,) 
  email  = models.EmailField(max_length=256,)
  phone  = models.CharField(max_length=14)
  full_address  = models.TextField(max_length=512, blank=True, null=True)
  name_of_university  = models.CharField(max_length=256)
  graduation_year  = models.PositiveIntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2020)])
  cgpa  = models.DecimalField(max_digits=4, 
                              decimal_places=2, 
                              default=2.0, 
                              validators=[MinValueValidator(2.0), MaxValueValidator(4.0)])
  experience_in_months  = models.PositiveIntegerField(blank=True, 
                                                      null=True, 
                                                      validators=[MinValueValidator(0), 
                                                      MaxValueValidator(100)])
  current_work_place_name  = models.CharField(max_length=256, blank=True, null=True)
  applying_in  = models.CharField(max_length=20,)
  expected_salary  = models.PositiveIntegerField(validators=[MinValueValidator(15000), MaxValueValidator(60000)])
  field_buzz_reference  = models.CharField(max_length=256, blank=True, null=True)
  github_project_url  = models.CharField(max_length=512, validators=[URLValidator])
  cv_file_token_id = models.PositiveIntegerField(blank=True, null=True)

  def __str__(self):
    return self.name

  
class Cv(models.Model):
  apply_id = models.CharField(max_length=256, blank=True, null=True)
  file = models.FileField(upload_to='uploads/%Y/%m/%d/')

  def __str__(self):
    return self.apply_id