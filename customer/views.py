from django.shortcuts import get_object_or_404, render
from landing.models import *
from landing.forms import KYCForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import View
from landing.forms import PasswordChangeFormUpdate, CustomerForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def dashboard(request):

    course = Course.objects.all().order_by('-id')[:10]
    kyc = KYC.objects.filter(customer__id = request.user.id )

    dist ={
        'course':course,
        'kyc':kyc
    }
    return render(request, "customer/dashboard.html", dist)

def courseView(request):
    course = Course.objects.all().order_by('-id')

    dist ={
        'course':course
    }

    return render(request, "customer/studentc.html", dist)


def kycVerify(request):

    form = KYCForm()
    
    cm = KYC.objects.filter(customer__admin = request.user)
  
    for i in cm:
        cm=i
        break
    if cm:
        form = KYCForm(instance=cm)
    else:
        form = KYCForm()
   
    if request.user.customer.state:
        form.fields['state'].initial = request.user.customer.state
    else:
        try:
            pass
        except:
            pass
    
    if request.user.customer.city:
        form.fields['city'].initial = request.user.customer.city
    else:
        try:
           pass
        except:
            pass
    

    if request.user.customer.number:
        form.fields['number'].initial = request.user.customer.number

    if request.user.customer.address:
        form.fields['address'].initial = request.user.customer.address
    else:
        try:
            pass
        except:
            pass
       

    if request.user.customer.country:
        form.fields['country'].initial = request.user.customer.country 
   
    dist = {
        'form':form,
        'cm':cm
    }

    if request.method == 'POST':
        if cm:
            form = KYCForm(request.POST, request.FILES, instance=cm)
        else:
            form = KYCForm(request.POST, request.FILES)

       
        if form.is_valid():
            aa = form.save(commit=False)
            aa.customer = request.user.customer
            aa.save()
            uses = request.user.customer
            if not uses.state:uses.state= aa.state
            if not uses.city:uses.city= aa.city
            if not uses.country:uses.country= aa.country
            if not uses.number:uses.number= aa.number
          
            uses.save()
        
            return HttpResponseRedirect(reverse('customer:verify'))
        else:
            print(form.errors)
            dist.update({'form':form})
            messages.success(request, "Something went wrong! " )

    return render(request, "customer/kyc.html", dist)


def schoView(request):
    
    all_news = Course.objects.all().order_by('-id')

    dist = {
        'all_news':all_news
    }
    return render(request,'customer/schoCourse.html', dist)


def applyNow(request, id):
    course = get_object_or_404(Course, id=id)
    student = request.user.customer

    existing_scholarship = Scholorship.objects.filter(course=course, customer=student).exists()

    if existing_scholarship:
        messages.warning(request, "You have already applied for this course.")
        return HttpResponseRedirect(reverse('customer:scho'))
    else:
        Scholorship.objects.create(course=course, customer=student, remarks = request.POST['reason'])
        messages.success(request, "Successfully applied for scholarship.")
        return HttpResponseRedirect(reverse('customer:dashboard'))
    

class Profile(View):
    template_name = 'customer/profile.html'
    def get(self, request, *args, **kwargs):
        pcform = PasswordChangeFormUpdate(request.user)
        form = CustomerForm(instance=request.user.customer)
        cm = KYC.objects.filter(customer__admin = request.user)
        scho = Scholorship.objects.filter(customer = request.user.customer)
  
        for i in cm:
            cm=i
            break
        dist = {
            'pcform':pcform,
            'form':form,
            'cm':cm,
            'scho':scho,
            'real_customer':request.user.customer
        }

        return render(request, self.template_name, dist)

    def post(self, request, *args, **kwargs):
        real_customer = request.user.customer
        try:
            real_customer.admin.first_name = request.POST['first_name']
            real_customer.admin.last_name = request.POST['last_name']
            real_customer.admin.email = request.POST['email']
            real_customer.admin.username = request.POST['email']
            real_customer.admin.save()
        except:
            messages.error(request, "Email is added already..")
            return HttpResponseRedirect(reverse('customer:profile'))
        form = CustomerForm(request.POST)
        if form.is_valid():
            real_customer.number = request.POST['number']
          
            real_customer.state = request.POST['state']
            real_customer.city = request.POST['city']
            real_customer.country= request.POST['country']
            real_customer.address = request.POST['address']
            real_customer.save()
            messages.success(request, "Sucessfully Updated Profile")
            return HttpResponseRedirect(reverse('customer:profile'))
        else:
            err = form.errors
            print(err)
            dist = {
            'pcform':PasswordChangeFormUpdate(request.user),
            'form':form,
           
            'real_customer':request.user.customer            
            }
           
            messages.error(request, "Something went wrong")
            return render(request, self.template_name, dist)
    
def updatePic(request):
    file = request.FILES['profile']
    cust = request.user.customer
    cust.profil_pic = file
    cust.save()
    messages.success(request, "Successfully updated profile picture")
    return HttpResponseRedirect(reverse('customer:profile'))


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
       
        return HttpResponseRedirect(reverse('customer:homepage'))