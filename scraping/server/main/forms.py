# -*- coding: utf-8 -*-
from django import forms

class PageForm(forms.Form):
	page = forms.CharField()
