from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from corpers.models import Corper
from registration.forms import *


def corper_registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('corpers_profile')
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['state_code'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_date['password'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
            corper = Corper(corper=user, sex=form.cleaned_data['sex'],
                            state_of_origin=form.cleaned_data['state_of_origin'],
                            date_of_birth=form.cleaned_data['date_of_birth'],
                            about=form.cleaned_data['about'],
                            phone_number=form.cleaned_data['phone_number'],
                            logo=form.cleaned_data['logo'])
            corper.save()
            return HttpResponseRedirect('corpers_profile')
        else:
            context = {'form': form}
            return render_to_response('account/corper_reg.html', context, context_instance=RequestContext(request))
    """user is not submitting the form , show them a blank account form"""
    form = RegistrationForm()
    context = {'form': form}
    return render_to_response('account/corper_reg.html', context, context_instance=RequestContext(request))


def corper_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('corpers_profile')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            state_code = form.cleaned_data['state_code']
            password = form.cleaned_data['password']
            corper = authenticate(state_code=state_code, password=password)
            if corper is not None:
                login(request, corper)
                return HttpResponseRedirect('corper_profile')
            context = {'form': form}
            return render_to_response('account/login.html', context, context_instance=RequestContext(request))
        context = {'form': form}
        return render_to_response('account/login.html', context, context_instance=RequestContext(request))
    """User is not submitting the form, show the login form """
    form = LoginForm()
    context = {'form': form}
    return render_to_response('account/login.html', context, context_instance=RequestContext(request))
