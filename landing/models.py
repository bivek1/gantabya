from django.db import models
from django.db import IntegrityError, models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length= 200)
    slug = models.SlugField(unique=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1

            while True:
                try:
                    super(Category, self).save(*args, **kwargs)
                    break
                except IntegrityError:
                    self.slug = f"{original_slug}-{counter}"
                    counter += 1
        else:
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    

class Course(models.Model):
    category = models.ForeignKey(Category, related_name='course_category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    scholorship = models.BooleanField(default= False)
    scholorship_description = models.CharField(max_length = 300)
    slug = models.SlugField(unique= True, null = True, blank=True)
    description = RichTextUploadingField()
    short_description = models.TextField()
    video = models.FileField(upload_to='course_video/', null = True, blank= True)
    image = models.ImageField(upload_to='course_image/', null=True, blank=True)
  
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1

            while True:
                try:
                    super(Course, self).save(*args, **kwargs)
                    break
                except IntegrityError:
                    self.slug = f"{original_slug}-{counter}"
                    counter += 1
        else:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null = True, blank= True)
    email = models.EmailField(null = True, blank= True)
    remarks = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.name