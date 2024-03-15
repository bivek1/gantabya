from django.shortcuts import render
from landing.forms import PasswordChangeFormUpdate, UserForm
from landing.models import *
from manager.forms import *
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


def dashBoard(request):

    course = Course.objects.all().order_by('-id')[:10]

    dist ={
        'course':course,
        'total_student': Customer.objects.all().count(),
        'total_course':Course.objects.all().count(),
        'total_kyc': KYC.objects.all().count()
    }
    return render(request, "manager/dashboard.html", dist)

def news(request):
    latest = Course.objects.all().order_by('-id')[:5]
   
    category = Category.objects.all().order_by('-id')[:8]
    form = CourseForm()
    dist = {
        'category':category,
        'course':latest,
        'form':form,
    }
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            sav = form.save(commit= False)
            sav.added_by = request.user
            sav.save()
            messages.success(request, "Successfully added courses")
        else:
            messages.success(request, "Something went wrong")
    return render(request, "manager/news.html", dist)


def allNews(request):
    latest = Course.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    all_news = Course.objects.all().order_by('-id')

    dist = {
        'category':category,
        'latest':latest,
        'all_news':all_news
    }
    return render(request,'manager/allNews.html', dist)

def cnews(request, str):
    latest = Course.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    all_news = Course.objects.filter(status = str).order_by('-id')

    dist = {
        'category':category,
        'latest':latest,
        'all_news':all_news,
        'status':str
    }
    return render(request,'manager/c_news.html', dist)


def deleteNews(request, id):
    news = Course.objects.get(id = id)
    news.delete()

    messages.success(request, "Course has been deleted")
    return HttpResponseRedirect(reverse('manager:allNews'))


def updateNews(request, id):
    latest = Course.objects.all().order_by('-id')[:5]
    
    category = Category.objects.all().order_by('-id')[:8]
    news = Course.objects.get(id = id)
    form = CourseForm(instance=news)
    
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'real_news':news
    }
    if request.method == 'POST':
        
        form = CourseForm(request.POST, request.FILES, instance= news)
        if form.is_valid():
            sav = form.save(commit= False)
            sav.added_by = request.user
            sav.save()
            messages.success(request, "Update succesfull")
        else:
            messages.success(request, "Something went wrong")
        return HttpResponseRedirect(reverse('manager:allNews'))
    return render(request, "manager/editNews.html", dist)


def CategoryView(request):
    latest = Course.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    form = CategoryForm()
    all_category = Category.objects.all().order_by('-id')
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'all_category':all_category
    }
    if request.method == 'POST':
        edit_id = None
        try:
            edit_id = request.POST['edit']
            news_real = Category.objects.get(id = edit_id)
            print(news_real)
            form = CategoryForm(request.POST, request.FILES, instance=news_real)
            if form.is_valid():
                form.save()
                messages.success(request, "Update Successfully")
            else:
                messages.success(request, "Something went wrong")
        except:
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Category added successfully")
            else:
                messages.success(request, "Something went wrong")

    return render(request, "manager/category.html", dist)

def deleteCategory(request , id):
    cate = Category.objects.get(id = id)
    cate.delete()
    messages.success(request, "Successfully delete category")
    return HttpResponseRedirect(reverse('manager:category'))


def userList(request):
    latest = Course.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    form = UserForm()
    all_category = CustomUser.objects.filter(user_type = 'owner').order_by('-id')
    password_form = PasswordChangeFormUpdate(request.user)
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'all_category':all_category,
        'password_form':password_form
    }
    if request.method == 'POST':
        try:
            User.objects.create_superuser(username = request.POST['username'], email = request.POST['email'], password=request.POST['password'])
            messages.success(request, "User added successfully")
        except:
            messages.success(request, "Something went wrong")

    return render(request, "manager/user.html", dist)

def studentList(request):
    all_category = CustomUser.objects.filter(user_type = 'customer').order_by('-id')
   
    dist = {
        'all_category':all_category,
    }
   
    return render(request, "manager/student.html", dist)

def deleteStudent(request, id):
    stud = CustomUser.objects.get(id = id)
    stud.delete()
    messages.success(request, "Successfully deleted student")
    return HttpResponseRedirect(reverse('manager:student'))

def studentProfile(request, id):

    profile = CustomUser.objects.get(id = id)
    dist = {
        'profile':profile
    }
    return render(request,"manager/customerProfile.html", dist)



def deleteUser(request , id):
    cate = User.objects.get(id = id)
    cate.delete()
    messages.success(request, "User has been deleted")
    return HttpResponseRedirect(reverse('manager:userList'))

def nowLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage:homepage'))

def checkPassword(request):
   if request.method == 'POST':
        form = PasswordChangeFormUpdate(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Update Successfully')
            
        else:
            error = form.errors.as_data()
        
            messages.success(request, error)
       
        return HttpResponseRedirect(reverse('manager:userList'))
   
def kycView(request):
    kyc = KYC.objects.all()
    verified = kyc.filter(customer__kyc_verified = True).order_by('-id')
    not_verified = kyc.filter(customer__kyc_verified = False).order_by('-id')
    dist = {
        'kyc': verified,
        'kyc_not':not_verified,
        'pending':not_verified.count(),
        'verified_ss':verified.count()
    }
    # noti = notification(request)
    # dist.update(noti)
    return render(request, "manager/kyc.html", dist)


def kycVerification(request, id):
    kyc = KYC.objects.get(id = id)
    user = Customer.objects.get(id = kyc.customer.id)
    print(user)
   
    dist  ={
        'cm':kyc,
        'real_customer':user
    }
   
   
    return render(request, "manager/kycDetails.html", dist)

def verifyView(request, id):
    kyc  = KYC.objects.get(id = id)
    user = Customer.objects.get(id = kyc.customer.id)
    kyc.seen = True
    kyc.save()
    user.kyc_verified = True
    user.save()
    

    # sub = 'Your KYC is verified'
    # messa = "We congraulate you for verifying your kyc. And you can add Bank, recipient and send money."
   
   
    
   
    # dist_info = {
    #     'sub': sub, 'message':messa
    # }
    # dist_info.update(other_info)
    # content = settings.EMAIL_HOST_USER
    # html_message = render_to_string('component/email.html', dist_info)
    # pain_html_msg = strip_tags(html_message)
    # try: 
    #     msg = EmailMultiAlternatives(sub, pain_html_msg, content, recipient_list)
    #     msg.attach_alternative(html_message, "text/html")
    #     msg.send()
    # except:
    #     messages.error(request,"KYC verified. However failed to sent email. Please ask to verify customer email")
  
    # CustomerNotification.objects.create(customer = cust, name ="Congratulation Your KYC Has Been Verified.", types ="kyc", ids=cust.id)
    messages.success(request, "Successfully Verified Account")
    
    return HttpResponseRedirect(reverse('manager:kyc'))

def rejectView(request, id):
    kyc  = KYC.objects.get(id = id)
    user = Customer.objects.get(id = kyc.customer.id)
    kyc.seen = True
    kyc.save()
    user.rejected = True
    user.save()

    # sub = 'Your KYC is rejected'
    # messa = "We are sorry to inform you that your kyc is rejected, please update your details and try again."
    # other_info = siteInfo()
    
    # recipient_list = [user.admin.email]
    # dist_info = {
    #     'sub': sub, 'message':messa
    # }
    # dist_info.update(other_info)
    # content = settings.EMAIL_HOST_USER
    # html_message = render_to_string('component/email.html', dist_info)
    # pain_html_msg = strip_tags(html_message)
    # try: 
    #     msg = EmailMultiAlternatives(sub, pain_html_msg, content, recipient_list)
    #     msg.attach_alternative(html_message, "text/html")
    #     msg.send()
    # except:
    #     messages.error(request,"KYC rejected. However failed to sent email. Please ask to verify customer email")
   
    messages.success(request, "Successfully Rejected KYC")
    
    return HttpResponseRedirect(reverse('manager:kyc'))


def appliedScholor(request):
    scho = Scholorship.objects.all().order_by('-id')
    dist = {
        'scho':scho
    }
    return render(request, "manager/scho.html", dist)

