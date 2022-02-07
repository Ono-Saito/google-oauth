from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomUserManager(BaseUserManager):
	
	use_in_migrations = True

	def _create_user(self, request_data, **extra_fields):
		if not request_data['email']:
			raise ValueError('emailを入力してください')
<<<<<<< HEAD
		email = self.normalize_email(request_data['email'])
		user = self.model(username=request_data['username'], email=email, **extra_fields)
		user.set_password(request_data['password'])
		user.save(using=self.db)
		return user

	def create_user(self, request_data, **extra_fields):
=======
		if not username:
			raise ValueError('usernameを入力してください')
		email = self.normalize_email(email)
		user = self.model(
			username=username,
			email=email,
			**extra_fields
		)
		user.save(using=self.db)
		return user

	def create_user(self, username, email,**extra_fields):
>>>>>>> 6886aec2f16134270d759ae893f138181ded6537
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(request_data, **extra_fields)
	
	def create_superuser(self, request_data, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('staff=Falseになっています')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('is_superuser=Falseになっています')
		return self._create_user(request_data, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField('email', null=True)
	username = models.CharField('username', unique=True, max_length=150)
<<<<<<< HEAD
=======
	image_url = models.URLField('imageUrl', blank=True, max_length=200)
>>>>>>> 6886aec2f16134270d759ae893f138181ded6537
	is_staff = models.BooleanField('is_staff', default=False)
	is_active = models.BooleanField('is_active', default=True)
	date_joined = models.DateTimeField('date_joined', default=timezone.now)

	objects=CustomUserManager()

	USERNAME_FIELD = 'username'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['email']

	class Meta:
		verbose_name = "user"
		verbose_name_plural = "users"