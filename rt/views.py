from django.shortcuts import render
from .forms import RT_Form
from .models import RT
from registration.models import RegistrationProfile  
from django.shortcuts import render,get_object_or_404,redirect,Http404 

# Create your views here.

def home(request):
	qs=RT.objects.all().order_by('-id').filter(public__exact=True)
	context={'qs':qs}
	return render(request,'home.html',context)


def submit(request):
	form = RT_Form(request.POST or None)
	context={'form':form}
	if form.is_valid():
		instance =form.save(commit=False)
		instance.user=request.user
		instance.save()

		
	return render(request,'submit.html',context)	


def userView(request,user__username):
	instance=get_object_or_404(RegistrationProfile,user__username=user__username)
	
	if str(request.user)==str(user__username):
		username=user__username
		qs=RT.objects.all().order_by('-id').filter(user__username=user__username)
		context={'instance':instance,'qs':qs,'username':user__username}
	else:
		username=user__username
		qs=	RT.objects.all().order_by('-id').filter(user__username=user__username,public__exact=True)
		context={'instance':instance,'qs':qs,'username':user__username}
	return render(request,'user.html',context)

def detailView(request,id):
	object = RT.objects.get(id=id)
	context={'object':object}
	return render(request,'detail.html',context)
