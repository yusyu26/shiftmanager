from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import datetime

class Post(models.Model):    
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
    
    date = models.DateField(
        default=datetime.date.today,
        blank = False,
        null = False)
    
    starttime = models.TimeField(
        default='18:00',
        blank = False,
        null = False)

    endtime = models.TimeField(
        default='23:00',
        blank = False,
        null = False)

    author = models.CharField(
        max_length = 50,
        blank = False,
        null = False)
    
    substitute = models.CharField(
        default = '',
        verbose_name = "シフト交代者名",
        max_length = 50,
        blank = True,
        )
        

    def __str__(self):
        return f"Post created on {self.date} by {self.author}"
        
    def get_absolute_url(self):
        return reverse_lazy("shortage_shift_list")
