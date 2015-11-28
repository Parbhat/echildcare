#!/usr/bin/env python

from django.db import models

from django import utils
from register.utils import format_number


class ContactExtended(models.Model):
    """ Abstract model to extend the RapidSMS Contact model """
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=False, null=True)
    place = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True

    @property
    def formatted_phone(self):
        return format_number(self.phone)
