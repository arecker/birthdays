.PHONY: all
all:
	@echo "no default rule.  Run make load or make save"

.PHONY: save
save:
	@echo "saving people.conf to pass://birthdays"
	cat people.conf | pass insert -f -m "birthdays"

.PHONY: load
load:
	@echo "loading people.conf from pass://birthdays"
	pass birthdays > people.conf
