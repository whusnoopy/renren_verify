#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
import base64

def login():
  username = raw_input('username: ')
  password = raw_input('password: ')

  encode_pas = urllib.quote(base64.b64encode(password))

  login_para = {
    "username": username,
    "password": password,
    "url": "",
    "password_enc": encode_pas,
    "newpassword_enc": "",
    "retype_newpassword_enc": "",
    "login": "1",
    "login_type": "login",
    "uri": "aHR0cDovLzE5Mi4xNjguNjAuNjUv",
    "password_type": "normal",
    "password_orig": ""}

  login_url = "http://10.2.255.254"
  login_data = urllib.urlencode(login_para)

  try:
    f = urllib2.urlopen(url=login_url, data=login_data)
  except:
    print 'already online'
    return False

  req = f.read()
  if req.find('已成功登录') != -1:
    print 'we are online!'
    return True

  print req
  return False


def logout():
  logout_url = "http://10.2.255.254:81"
  logout_data = "logout=1"

  try:
    f = urllib2.urlopen(url=logout_url, data=logout_data)
  except:
    return False

  print 'we get off!'
  return True


if __name__ == "__main__":
  if len(sys.argv) <= 1 or sys.argv[1].lower() != "logout":
    if not login():
      print 'will logout and re login'
      logout()
      import time
      time.sleep(1)
      login()
  else:
    logout()

