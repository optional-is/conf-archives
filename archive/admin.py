# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

admin.autodiscover()


# Register your models here.
admin.site.register(Slot)
admin.site.register(Presenter)
admin.site.register(Tag)
admin.site.register(Conference)
