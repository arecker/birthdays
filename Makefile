.PHONY: all
all: venv/bin/python

venv/bin/python:
	python -m venv --copies ./venv

.PHONY: save
save:
	@echo "saving people.conf to pass://birthdays"
	cat people.conf | pass insert -f -m "birthdays"

.PHONY: load
load:
	@echo "loading people.conf from pass://birthdays"
	pass birthdays > people.conf
