from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

import console
from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads

# Create your views here.

def show(request):
	joke_json = loads(urlopen('http://api.icndb.com/jokes/random').read())
	return HTMLParser().unescape(joke_json['value']['joke']).encode('utf-8')

