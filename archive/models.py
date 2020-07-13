# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class Tag(models.Model):
	class Meta:
		ordering = ['name']

	name = models.CharField(max_length=200, blank=False)

	def __unicode__(self):
		return self.name


class Conference(models.Model):
	year = models.IntegerField(blank=False,null=False)
	location = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	metadata = models.TextField(blank=True, null=True)
	attendees = models.IntegerField(blank=False,null=False)

	is_active  = models.BooleanField(default=True)

	link_url = models.CharField(max_length=200, blank=False)
	logo_url = models.CharField(max_length=200, blank=False)

	date_start = models.DateTimeField(auto_now_add=True,  blank=False)
	date_end = models.DateTimeField(auto_now_add=True,  blank=False)

	def __unicode__(self):
		return "Material %s"%self.year

class Presenter(models.Model):
	slug = models.CharField(max_length=200, blank=False,null=False)
	name = models.CharField(max_length=200, blank=False,null=False)
	bio = models.TextField(blank=True, null=True)

	thumbnail_url = models.URLField(blank=True, null=True)
	sex       = models.IntegerField(blank=True, null=True)
	country   = models.CharField(max_length=24, blank=False,null=False) # Unicode flag


	def __unicode__(self):
		return unicode(self.name)

class Link(models.Model):
	url 	  = models.URLField(blank=True, null=True)
	name 	  = models.CharField(max_length=200, blank=False,null=False)
	presenter = models.ForeignKey(Presenter, blank=False, null=False, related_name="links")


	def __unicode__(self):
		return unicode(self.name) + " ("+self.presenter.name+")"


class Slot(models.Model):
	conference = models.ForeignKey(Conference, blank=False, null=False)
	presenter = models.ManyToManyField(Presenter, blank=False, null=False)
	running_order = models.IntegerField(blank=False,null=False)
	slug = models.CharField(max_length=100, blank=False,null=False)

	title = models.TextField(blank=True, null=True)
	abstract = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	transcript = models.TextField(blank=True, null=True)
	synopsis = models.TextField(blank=True, null=True)
	length = models.IntegerField(blank=False,null=False)


	poster_img_url = models.TextField(blank=True, null=True)

	tags = models.ManyToManyField(Tag, blank=True)

	is_active  = models.BooleanField(default=True)

	# media
	youtube_link = models.TextField(blank=True, null=True)
	mp3_link     = models.TextField(blank=True, null=True)

	def get_presenters(self):
		return ' & '.join([unicode(i) for i in self.presenter.all().order_by('name')])

	def __unicode__(self):
		return "Material "+unicode(self.conference.year)+": "+self.title+" - "+self.get_presenters()
