from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from apps.common.models import *


class UserManager(BaseUserManager):

    '''
    methods added to base user manager for easy managing
    '''
    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the address by lowercasing the email and domain of the email
        address.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name.lower(), domain_part.lower()])
        return email

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = _tz.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_active=True, last_login=now, date_joined=now,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStamped):

    '''
    replacemnt for default auth.User model
    inheriting for AbstractBaseUser for default methods
    inherited fields are 'password', 'last_login'
    inhertited methods are 'is_authenticated', 'is_anonymous', 
    'set_password', 'check_password'
    '''

    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    email = models.EmailField(
        max_length=128, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    # Dates
    date_joined = CreationDateTimeField()

    # methods
    objects = UserManager()

    # properties
    is_advertiser = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    # requirements for django.auth
    USERNAME_FIELD = 'email'

    def __unicode__(self):
        name = self.email
        if self.first_name or self.last_name:
            name = u'%s %s' % (self.first_name, self.last_name)
        return name

    @property
    def name(self):
        if self.first_name or self.last_name:
            return u'%s %s' % (self.first_name, self.last_name)
        return None

    def get_username(self):
        if self.name:
            return self.name
        return self.email