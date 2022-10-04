from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404, HttpResponseRedirect)
from django.urls import reverse
from user.models import User
from user.forms import UpdateProfileForm


def home(request):
    return render (request, '_layout.html')


def profile(request, *args, **kwargs):
    user_obj = get_object_or_404(User, id=request.user.id)
    user_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=user_obj)
    if request.method == "POST":
        if user_form.is_valid():    
                user_form.save()
                return HttpResponseRedirect(reverse('successfull'))


    return render(request, 'user/profile.html')


def successfullsave(request):
    return render(request,'successfull.html',{})