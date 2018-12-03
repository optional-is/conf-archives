# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from models import *
from django.db.models import Sum

# Create your views here.
def index(request):
	c = {}
	conferences = Conference.objects.all().order_by('-year')
	c.update({'latest_conf': conferences[0]})

	c.update(add_footer_context())

	return render(request, 'index.html', c)	

def year(request, year_name):
	c = {}
	conf = get_object_or_404(Conference, year=int(year_name))
	c.update({'conference': conf})

	c.update(add_footer_context())

	c.update({'slots':Slot.objects.filter(conference=conf).order_by('running_order')})
	return render(request, 'conference_detail.html', c)	

def slot(request, year_name, slot_slug):
	c = {}
	slot = get_object_or_404(Slot, slug=slot_slug)
	c.update({'slot':slot})

	c.update(add_footer_context())

	return render(request, 'slot_detail.html', c)	

def tags(request, tag_name):
	c = {}
	tag = get_object_or_404(Tag, name=tag_name)

	c.update(add_footer_context())
	c.update({'tag': tag})
	c.update({'slots':Slot.objects.filter(tags__in=[tag]).order_by('title')})
	return render(request, 'tag_results.html', c)	


def add_footer_context():
	c = {}
	c.update({'conferences':Conference.objects.all().order_by('-year') })
	c.update({'total_time': Slot.objects.all().values('length').aggregate(total_time=Sum('length'))['total_time']})
	c.update({'tags':Tag.objects.all().order_by('name')})
	return c
