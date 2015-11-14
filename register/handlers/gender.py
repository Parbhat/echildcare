#!/usr/bin/env python

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler


class GenderHandler(KeywordHandler):

    keyword = "gender"

    def help(self):
        self.respond("To save the child gender, send gender <M/F/O> where M for male, \
             F for female and O for other")

    def handle(self, text):
        if self.msg.connection.contact is None:
            return self.respond_error(
                "You must JOIN or REGISTER yourself before you can " +
                "set your child gender")

        try:
            self.msg.connection.contact.gender = text.upper()
            self.msg.connection.contact.save()
        except:
            return self.respond_error("Please send in correct format. Ex: gender F")

        return self.respond(
            "Thanks for saving  %(name)s gender." % {
                'name': self.msg.connection.contact.name})