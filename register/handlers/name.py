#!/usr/bin/env python

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler


class NameHandler(KeywordHandler):

    keyword = "name"

    def help(self):
        self.respond("To save the child name, send name <child-name>")

    def handle(self, text):
        if self.msg.connection.contact is None:
            return self.respond_error(
                "You must JOIN or REGISTER yourself before you can " +
                "set your child name")

        self.msg.connection.contact.name = text
        self.msg.connection.contact.save()

        return self.respond(
            "Thanks for saving your child name. %(name)s is a cute name." % {
                'name': text})