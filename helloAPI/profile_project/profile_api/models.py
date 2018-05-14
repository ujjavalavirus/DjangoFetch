from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
	"""Helps Django work with our custom user model."""


	def create_user(self, email, name, password=None):
		"""Creates a new user profile object. """

		if not email:
			raise valueError('Users must have an email address.')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		"""set_password function encrypt the password"""
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, email, name, password):
		"""Creates & saves a new superuser with given details."""

		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""Respents a "User Profile" inside our system."""

	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)


	objects = UserProfileManager()
	"""Login with email on place of name"""
	USERNAME_FIELD = 'email' 
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		"""Used to get a users full name."""

		return self.name

	def get_short_name(self):
		"""Used to get a short name"""

		return self.name

	def __str__(self):
		"""Django uses this when it needs to convert the object to strings"""

		return self.email




class NewsRssFeed(models.Model):
	"""News fetch from rss & save the data"""

	title = models.TextField()
	description = models.TextField()
	newslink = models.CharField(max_length=255)
	imagelink = models.CharField(max_length=255)
	newsCategory = models.CharField(max_length=255)
	newsDate = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(Self):
		"""Return News ID"""

		return self.id


















