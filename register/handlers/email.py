#!/usr/bin/env python

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
import re

class EmailHandler(KeywordHandler):

    keyword = "email"

    def help(self):
        self.respond("To save the E-mail for email notifications, send email <E-mail id>")

    def handle(self, text):
        if self.msg.connection.contact is None:
            return self.respond_error(
                "You must JOIN or REGISTER yourself before you can " +
                "set your E-mail")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", text):
            return self.respond_error("Please enter E-mail in correct format.")

        self.msg.connection.contact.email = text
        self.msg.connection.contact.save()

        return self.respond(
            "Thanks for saving your E-mail for child %(name)s." % {
                'name': self.msg.connection.contact.name})