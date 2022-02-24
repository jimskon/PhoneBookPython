#MakeFile to build and deploy the Sample US CENSUS Name Data using ajax
# For CSC3004 Software Development

# Put your user name below:
USER= skon

all: PutCGI PutHTML

PutCGI:
	chmod 757 phoneApp.py
	cp phoneApp.py /usr/lib/cgi-bin/$(USER)_phoneApp.py

	echo "Current contents of your cgi-bin directory: "
	ls -l /usr/lib/cgi-bin/

PutHTML:
	cp phoneApp.html /var/www/html/class/ssd/$(USER)/PhoneAppPython/
	cp phoneApp.css /var/www/html/class/ssd/$(USER)/PhoneAppPython/
	cp phoneApp.js /var/www/html/class/ssd/$(USER)/PhoneAppPython/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/class/ssd/$(USER)/PhoneAppPython/
