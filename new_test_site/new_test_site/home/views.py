from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone 

from .models import display, data

# Create your views here.
 def IndexView(generic.ListView): 
 	template_name = 'home/index.html'  
 	cubedata = display.object.all() 
 	



