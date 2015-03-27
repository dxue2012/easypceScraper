# adopted from http://stackoverflow.com/questions/20039643/
# how-to-scrape-a-website-that-requires-login-first-with-python
#
# Author: Dyland Xue

##################################### Method 1
import mechanize
import cookielib
from bs4 import BeautifulSoup
import html2text
import getpass

username = raw_input("netid: ")
password = getpass.getpass()

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('http://easypce.com/')

# View available forms
for f in br.forms():
    print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)

# User credentials
br.form['username'] = username
br.form['password'] = password

# Login
br.submit()

easypce = br.open('http://easypce.com/').read()
course_510 = br.open('http://easypce.com/courses/COS510').read()
print(easypce)
print(course_510)
