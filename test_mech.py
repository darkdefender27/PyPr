#!/usr/bin/env python
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)

f = open(r'C:\Users\Shubham Utwal\Desktop\tikonaCredentials.txt')
credentials = {}

for line in f.readlines():
    line = line.replace(" ", "")
    line = line.strip()
    parts = line.split(":")    
    credentials[parts[0]] = parts[1]

tikona_username = credentials['username']
tikona_password = credentials['password']

br.open("https://login.tikona.in/userportal/newlogin.do?phone=0")

br.select_form(name="form1")
br.form['username'] = tikona_username
br.form['password'] = tikona_password
br.form['type'].append('Internet')

br.submit()
print br.response().read()


