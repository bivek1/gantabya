# Generated by Django 5.0.2 on 2024-02-26 10:54

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('remarks', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('owner', 'owner'), ('customer', 'customer')], default='owner', max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('scholorship', models.BooleanField(default=False)),
                ('scholorship_description', models.CharField(max_length=300)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='course_video/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_image/')),
                ('course_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('credit_hour', models.CharField(blank=True, max_length=200, null=True)),
                ('entry_requirement', models.CharField(blank=True, max_length=200, null=True)),
                ('intake', models.CharField(blank=True, max_length=200, null=True)),
                ('accrediation', models.CharField(blank=True, max_length=200, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='landing.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('profil_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/customer/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kyc_verified', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_adder', to=settings.AUTH_USER_MODEL)),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='kyc_image')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('number', models.BigIntegerField()),
                ('postal_address', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200, null=True)),
                ('document_type', models.CharField(choices=[('National ID', 'National ID'), ('Driver licence', 'Driver licence'), ('Passport', 'Passport')], max_length=200)),
                ('licence_number', models.IntegerField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('document_front_image', models.ImageField(blank=True, null=True, upload_to='document/')),
                ('document_back_image', models.ImageField(blank=True, null=True, upload_to='document/')),
                ('passport_number', models.IntegerField(blank=True, null=True)),
                ('passport_issue_date', models.DateField(blank=True, null=True)),
                ('passport_expiry_date', models.DateField(blank=True, null=True)),
                ('passport_image', models.ImageField(blank=True, null=True, upload_to='document/')),
                ('passport_issued_country', models.CharField(blank=True, max_length=200, null=True)),
                ('address_verification', models.ImageField(blank=True, null=True, upload_to='bills')),
                ('business_image', models.ImageField(blank=True, null=True, upload_to='document/')),
                ('business_registration_date', models.DateField(blank=True, null=True)),
                ('registraion_number', models.IntegerField(blank=True, null=True)),
                ('photo_image', models.ImageField(blank=True, null=True, upload_to='photoid/')),
                ('photo_issue_date', models.DateField(blank=True, null=True)),
                ('photo_number', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kyc_customer', to='landing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
