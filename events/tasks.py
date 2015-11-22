from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from rapidsms.models import Connection
from rapidsms.router import send

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="send messages to contacts that become eligible for general event.",
    ignore_result=True
)
def send_msg_general_events():
    """
    Send messages to contacts that become eligible for general events.
    """
    # Test
    conn_obj = Connection.objects.all()[0]
    send("Hello", conn_obj)
