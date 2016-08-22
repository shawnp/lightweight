import os
#import python systems
import sys


# import django configure settings
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '{{secret_key}}')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


#Django SETTING
# Set the django config debug to ture set static key"Never do" 

settings.configure(
	DEBUG = True,
	SECRET_KEY = 'thisisthesecretkey',
	ALLOWED_HOSTS=ALLOWED_HOSTS,
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = (
		'django.middleware.common.CommonMiddleware',
		'django.middleware.csrf.CsrfViewMiddleware',
		'django.middleware.clickjacking.XFrameOptionsMiddleware',
		),
)

# Django IMPORTS

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

# Django VIEWS Setting

def index (request):
	return HttpResponse ('Hello Wold')


# Django URLS Setting
urlpatterns = (
	url(r'^$', index),

)

# Django WSGI SETTING
application = get_wsgi_application()


if __name__ == "__main__":
	from django.core.management import execute_from_command_line


	execute_from_command_line(sys.argv)