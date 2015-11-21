from rapidsms.apps.base import AppBase


class Unsubscribe(AppBase):

    def handle(self, msg):
        if msg.text == 'stop':
            if msg.connection.contact is None:
                msg.respond(
                    "You must JOIN or REGISTER yourself before you can " +
                    "stop echildcare service. To register, send REGISTER")
                return True

            msg.connection.contact.delete()
            msg.connection.delete()
            msg.respond("You have successfully unsubscribed from the echildcare service. \
                To register again send REGISTER")
            return True
        return False