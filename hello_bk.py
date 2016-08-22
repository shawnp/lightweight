import os
#import python systems
import sys


# import django configure settings
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'


SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Set the django config debug to ture set static key"Never do" 
#
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



from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse



def index (request):
	return HttpResponse ('Hello Wold')

urlpatterns = (
	url(r'^$', index),

)


application = get_wsgi_application()


if __name__ == "__main__":
	from django.core.management import execute_from_command_line


	execute_from_command_line(sys.argv)