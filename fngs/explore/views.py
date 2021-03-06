from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import QuerySubmission
from .forms import QuerySubmissionForm
from ndmg.scripts.ndmg_func_pipeline import ndmg_func_pipeline as fngs_pipeline
from ndmg.scripts.ndmg_dwi_pipeline import ndmg_dwi_pipeline as ndmg_pipeline
from django.conf import settings
import time
import importlib
import imp
from ndmg.utils import utils as mgu
from threading import Thread
from multiprocessing import Process
import os
import re

def index(request):
	return render(request, 'explore/index.html')

def submit_job(request):
	form = QuerySubmissionForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		submission = form.save(commit=False)
		submission.creds_file = request.FILES['creds_file']
		submission.save()
		logfile = submission.jobdir + "log.txt"
		p = Process(target=submitstuff, args=(submission, logfile))
		p.daemon=True
		p.start()
		p.join()
		messages = open(logfile, 'r').readlines()
		os.system("rm " + logfile)
		context = {
			"messages": messages,
			"form": form,
		}
		return render(request, 'explore/create_submission.html', context)
	context = {
		"form": form,
	}
	return render(request, 'explore/create_submission.html', context)

def submitstuff(submission, logfile):
	if submission.state == 'status':
		cmd = "ndmg_cloud status --jobdir " + submission.jobdir + " --credentials " + submission.creds_file.url
	if submission.state == 'kill':
		cmd = "ndmg_cloud kill --jobdir " + submission.jobdir + " --credentials " + submission.creds_file.url
	cmd = cmd + " > " + logfile
	os.system(cmd)
