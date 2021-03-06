from django import forms
from django.contrib.auth.models import User
from .models import Submission
from django.utils.translation import ugettext_lazy as _


class SubmissionForm(forms.ModelForm):
	class Meta:
		model = Submission
		fields = ['state', 'bucket', 'bidsdir', 'jobdir', 'creds_file', 'datasetname', 'modality', 'slice_timing', 'data_file', 'upload_data_or_not']
		labels={
			'state':_('Analysis Level'),
			'bucket':_('S3 Bucket Name'),
			'bidsdir':_('BIDS Directory'),
			'jobdir':_('Unique Token'),
			'creds_file':_('AWS Credentials File'),
			'datasetname':_('Dataset Name'),
			'modality':_('Modality'),
			'slice_timing':_('Slice Timing Method'),
			'data_file':_('Local Data (Zipped)'),
			'upload_data_or_not':_('Upload Local Data?')
		}
		help_texts={
			'state':_('Level of analysis to perform'),
			'bucket':_('Name of S3 bucket where data lives'),
			'bidsdir':_('Path on S3 bucket where data lives'),
			'jobdir':_('Unique identifier for job submission to facilitate later queries'),
			'creds_file':_('File containing user credentials for AWS services'),
			'datasetname':_('Dataset name (group analysis)'),
			'modality':_('Modality of data'),
			'slice_timing':_('The method in which slices were acquired.'),
			'data_file':_('Local data to be uploaded to S3 bucket(stored in BIDS formatting and zipped).'),
			'upload_data_or_not':_('Whether or not the local data should be uploaded to S3.')
		}
