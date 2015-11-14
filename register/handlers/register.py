#!/usr/bin/env python

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.dateformat import DateFormat
from rapidsms.models import Contact


class RegisterHandler(KeywordHandler):

    keyword = "register|reg|join"

    def help(self):
        self.respond("Thanks for showing interest in echildcare. To register, \
            send JOIN <DATE OF BIRTH OF CHILD like YYYY-MM-DD> <MOBILE NUMBER FOR RECEIVING INFORMATION>")

    def handle(self, text):
        text_list = text.split()
        if len(text_list) != 2:
            return self.respond_error("You are registering in wrong format. \
            To register, send JOIN <DATE OF BIRTH OF CHILD like YYYY-MM-DD> \
            <MOBILE NUMBER FOR RECEIVING INFORMATION>")

        birth_date = text_list[0]
        mobile_num = text_list[1]

        try:
            contact = Contact.objects.create(date_of_birth=birth_date, phone=mobile_num)
        except:
            return self.respond_error("Please register in correct format. Ex: join 1994-04-24 9896098960")
            

        self.msg.connection.contact = contact

        # Now we change the connection identity to mobile number registered.
        self.msg.connection.identity = mobile_num
        self.msg.connection.save()

        self.respond(
            "Thank you for registering your child with echildcare born on  %s. Now you will receive \
            notifications on %s" % (birth_date, mobile_num))
