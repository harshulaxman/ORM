from django.db import models
from django.contrib import admin
class Author(models.Model):
	id=models.IntegerField(primary_key=True);
	name=models.CharField(max_length=20);
	publisher=models.CharField(max_length=25);
	bookname=models.CharField(max_length=30);
	bookid=models.IntegerField();
	pic=models.FileField(help_text="Upload photo in 50 kb");
	email=models.EmailField();
	dob=models.DateField();
class AuthorAdmin(admin.ModelAdmin):
	list_display=("id","name","publisher","bookname","bookid","pic","email","dob");
