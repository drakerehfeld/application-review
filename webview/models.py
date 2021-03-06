from django.db import models

class application(models.Model):
	fullName		 		= models.CharField(max_length=400,null=True)
	email			 		= models.CharField(max_length=400,null=True)
	uscId					= models.IntegerField(default=0,null=True)
	major			 		= models.CharField(max_length=400,null=True)
	minor			 		= models.CharField(max_length=400,null=True)
	gradYear				= models.CharField(max_length=400,null=True,default=0)
	available				= models.BooleanField(default=False)
	developer				= models.BooleanField(default=False)
	designer				= models.BooleanField(default=False)
	product					= models.BooleanField(default=False)
	other					= models.BooleanField(default=False)
	otherRole				= models.TextField(null=True)
	desiredOutcome			= models.TextField(null=True)
	contribution			= models.TextField(null=True)
	recentProj				= models.TextField(null=True)
	dailyProb				= models.TextField(null=True)
	excitingTech			= models.TextField(null=True)
	devToolsSoft			= models.TextField(null=True)
	devToolsHard			= models.TextField(null=True)
	designTools				= models.TextField(null=True)
	otherTools				= models.TextField(null=True)
	resume					= models.URLField(null=True)
	portfolio				= models.URLField(null=True)
	whatWork				= models.TextField(null=True)
	otherOrg				= models.TextField(null=True)
	referral				= models.TextField(null=True)
	joke					= models.TextField(null=True)
	annotated				= models.BooleanField(default=False)
	dedicationRating		= models.IntegerField(null=True)
	resourcefulRating		= models.IntegerField(null=True)
	experienceRating		= models.IntegerField(null=True)
	imaginationRating		= models.IntegerField(null=True)
	naughtyRating			= models.IntegerField(null=True)
	notes					= models.TextField(null=True)
	annotator				= models.CharField(max_length=100, null=True)
	final					= models.CharField(max_length=200, null=True)
