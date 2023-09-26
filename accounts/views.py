from django.shortcuts import render, redirect
from .forms import RegisterationForms
from . models import Account 
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterationForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password )
            user.phone = phone
            user.save()
            
            # User ACTICATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html',{
                'user':user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(userr.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_mail = email
            send_email = EmailMessage(email_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Registration Successful')
            return redirect('register')
    else:
        form = RegisterationForms()
    
    context = {
        'form': form,
    }
    return render(request, 'category/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'category/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.sucess(request, 'You are logged out.')
    return redirect('login')
    
