# Makefile -- jpp-birthday2013

WEBAPP     = $(wildcard webapp.py)

run:
	. `pwd`/.env ; python $(WEBAPP)

install:
	virtualenv venv --no-site-packages --distribute --prompt=Birthday2013
	. `pwd`/.env ; pip install -r requirements.txt

# EOF
