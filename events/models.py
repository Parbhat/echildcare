from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class GeneralEvent(models.Model):
    """
    General event covers things that a child have to undergo after a certain period of time. 
    For example, Measles vaccine after 15 months of birth. These events have to happen for 
    all after a particular period of time.
    """

    name_of_event = models.CharField(max_length=100, null=False, blank=False)
    days = models.IntegerField(help_text='Days after which you should go to \
        the event', null=False, blank=False)

    msg_to_send = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.name_of_event

    class Meta:
        verbose_name = 'General Event'

@python_2_unicode_compatible
class ScheduledEvent(models.Model):
    """
    Events are scheduled on a date and children that are under the event criteria
    are called to the event.
    """
    name_of_event = models.CharField(max_length=100, null=False, blank=False)
    days = models.IntegerField(help_text='Minimum child age in days to be eligible to go to \
        the event', null=False, blank=False)

    event_date = models.DateField(null=False, blank=False)
    msg_to_send = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name_of_event
        
    class Meta:
        verbose_name = 'Scheduled Event'