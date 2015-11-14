#!/usr/bin/env python

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler


class PincodeHandler(KeywordHandler):

    keyword = "pincode"

    def help(self):
        self.respond("To save your area pincode, send pincode <pincode of your area>")

    def handle(self, text):
        if self.msg.connection.contact is None:
            return self.respond_error(
                "You must JOIN or REGISTER yourself before you can " +
                "set your area pincode")

        self.msg.connection.contact.place = text
        self.msg.connection.contact.save()

        return self.respond(
            "Thanks for saving your area pincode for child %(name)s." % {
                'name': self.msg.connection.contact.name})