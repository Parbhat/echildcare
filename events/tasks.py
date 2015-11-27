from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from datetime import date

from rapidsms.router import send
from rapidsms.models import Connection
from rapidsms.models import Contact

from events.models import GeneralEvent, ScheduledEvent

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute=0, hour=9)),
    name="delete scheduled tasks that are over",
    ignore_result=True
)
def delete_scheduled_events():
    """
    Delete scheduled events that are completed.
    """
    curr_date = date.today()

    scheduled_events_all = ScheduledEvent.objects.all()

    for event in scheduled_events_all:
        if (curr_date - event.event_date).days > 0:
            event.delete()


@periodic_task(
    run_every=(crontab(minute=0, hour=10)),
    name="send messages to contacts that become eligible for general events.",
    ignore_result=True
)
def send_msg_general_events():
    """
    Send messages to contacts that become eligible for general events.
    """
    
    contact_all = Contact.objects.all()
    gen_events_all = GeneralEvent.objects.all()

    connections_to_send = Connection.objects.none()

    curr_date = date.today()

    for event in gen_events_all:
        connections_to_send = Connection.objects.none()
        for contact in contact_all:
            if (curr_date - contact.date_of_birth).days == event.days:
                contact_conn = Connection.objects.filter(contact=contact)
                connections_to_send = connections_to_send | contact_conn

        for conn in connections_to_send:
            send(event.msg_to_send, conn)


@periodic_task(
    run_every=(crontab(minute=0, hour=10)),
    name="send messages to contacts that are eligible for scheduled events.",
    ignore_result=True
)
def send_msg_scheduled_events():
    """
    Send messages to contacts that are eligible for scheduled events.
    """
    
    contact_all = Contact.objects.all()
    scheduled_events_all = ScheduledEvent.objects.all()

    connections_to_send = Connection.objects.none()

    for event in scheduled_events_all:
        connections_to_send = Connection.objects.none()
        for contact in contact_all:
            if (event.event_date - contact.date_of_birth).days >= event.days:
                contact_conn = Connection.objects.filter(contact=contact)
                connections_to_send = connections_to_send | contact_conn

        for conn in connections_to_send:
            send(event.msg_to_send, conn)
