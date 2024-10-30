from django.shortcuts import render
# ویو ثبت نام
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser  
from .forms import RegistrationForm  
import random 

def generate_otp():
    return random.randint(100000, 999999)

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            otp = generate_otp()
            # request.session['otp'] = otp  # ذخیره کد OTP در سشن برای استفاده در صورت نیاز
            return HttpResponse(f"کد OTP شما: {otp}")
            # print(f"کد OTP برای شماره {otp}")
            # request.session['otp'] = otp  
            # request.session['user_id'] = user.id 

            # return  HttpResponse(f"داده دریافت شده: {otp}")
        else:
            return HttpResponse("opssss")

    else:
        form = RegistrationForm()
    
        return render(request, 'signup_otp/signup.html', {'form': form})

