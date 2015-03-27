# adopted from http://stackoverflow.com/questions/20039643/
# how-to-scrape-a-website-that-requires-login-first-with-python
#
# Author: Dyland Xue

##################################### Method 1
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

br = mechanize.Browser()
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
br.open('https://github.com/login')

for f in br.forms():
    print f

br.select_form(nr=0)

# User credentials
br.form['login'] = 'myusername'
br.form['password'] = 'mypwd'

# Login
br.submit()

br.open('github.com/settings/emails').read()
