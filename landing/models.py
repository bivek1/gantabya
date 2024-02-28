from django.db import models
from django.db import IntegrityError, models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = (("owner", "owner"), ("customer", 'customer'))
    user_type = models.CharField(default = "owner", choices = user_type_data, max_length = 20)
    email = models.EmailField(unique = True)

class Owner(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, related_name ="owner", on_delete=models.CASCADE, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return self.admin.first_name
    

class Customer(models.Model):
 
    admin = models.OneToOneField(CustomUser, related_name ="customer", on_delete=models.CASCADE, null = True, blank = True)
    number = models.BigIntegerField(null = True)
    country = models.CharField(max_length=100, null = True, blank = True)
    state = models.CharField(max_length=100, null = True, blank = True)
    city = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    profil_pic = models.ImageField(upload_to ="profile_pic/customer/", null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    added_by = models.ForeignKey(CustomUser, null=True, blank = True, related_name = 'student_adder', on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    kyc_verified = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    
    objects = models.Manager()
    

    def __str__(self):
        try:
            return self.admin.first_name
        except:
            return str(self.id)



class KYC(models.Model):
    image = models.ImageField(upload_to='kyc_image', null = True, blank=True)
    customer = models.ForeignKey(Customer, related_name='kyc_customer', on_delete=models.CASCADE, null = True, blank=True)
    country = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=200, null = True, blank= True)
    city = models.CharField(max_length=200)
    number = models.BigIntegerField()
    postal_address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=200, choices=(
        ('Male','Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ), null=True, blank = True)
    document_type = models.CharField(max_length=200, choices=(
        ('National ID', 'National ID'),
        ('Driver licence', 'Driver licence'),
        ('Passport', 'Passport'),
        
    ))
    


    # Licence
    licence_number = models.IntegerField(null = True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    document_front_image = models.ImageField(upload_to="document/", null =True, blank = True)
    document_back_image = models.ImageField(upload_to="document/", null =True, blank = True)
    

    # Passport
    passport_number = models.IntegerField(null = True, blank=True)
    passport_issue_date = models.DateField(null=True, blank=True)
    passport_expiry_date = models.DateField(null=True, blank=True)
    passport_image = models.ImageField(upload_to="document/", null =True, blank = True)
    passport_issued_country = models.CharField(max_length=200, null =True, blank = True)
    address_verification = models.ImageField(upload_to='bills', null=True, blank=True)
    # passport_image = models.ImageField(upload_to="document/", null =True, blank = True)

    # Business Registration 
    business_image = models.ImageField(upload_to='document/', null =True, blank = True)
    business_registration_date = models.DateField(null = True, blank=True)
    registraion_number = models.IntegerField(null = True, blank=True)
    
    #photo-id
    photo_image = models.ImageField(upload_to='photoid/', null =True, blank = True)
    photo_issue_date = models.DateField(null = True, blank=True)
    photo_number = models.IntegerField(null = True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.address


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
    description = models.TextField()
    short_description = models.TextField()
    video = models.FileField(upload_to='course_video/', null = True, blank= True)
    image = models.ImageField(upload_to='course_image/', null=True, blank=True)
    course_duration = models.CharField(max_length=200, null = True, blank=True)
    credit_hour = models.CharField(max_length=200, null = True, blank=True)
    entry_requirement = models.CharField(max_length=200, null = True, blank=True)
    intake = models.CharField(max_length=200, null = True, blank=True)
    accrediation = models.CharField(max_length=200, null = True, blank=True)
    time = models.CharField(max_length=200, null = True, blank=True)
  
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
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "owner":
            Owner.objects.create(admin = instance)
       
        if instance.user_type == "customer":
            Customer.objects.create(admin = instance)
       

@receiver(post_save, sender=CustomUser)
def post_save_receiver(sender, instance, **kwargs):
    if instance.user_type == "owner":
        instance.owner.save()
   
    if instance.user_type == "customer":
        instance.customer.save()
 