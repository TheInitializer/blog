"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

application = get_wsgi_application()
"""

#!/usr/bin/env python
import os
import sys
import imp

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if 'OPENSHIFT_REPO_DIR' in os.environ:
	sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'openshift'))
	virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/venv'
	os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
	virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
	exec(compile(open(virtualenv).read(), virtualenv, 'exec'),dict(file = virtualenv))
except IOError:
	pass

imp.find_module('openshiftstaticfiles')
import openshiftstaticfiles

from django.core.wsgi import get_wsgi_application

application = openshiftstaticfiles.Cling(get_wsgi_application())
