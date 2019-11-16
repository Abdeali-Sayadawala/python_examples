# -*- coding: utf-8 -*-
import re

def valid_email(email):
    if len(email) > 7:
        if (re.search('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email)):
            return True
        else:
            return False

N = int(input())
emails = list()

for i in range(N):
    em = input()
    if valid_email(em):
        emails.append(em)

for i in range(len(emails)):
    print(emails[i])