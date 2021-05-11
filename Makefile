install:
	pip install --upgrade pdm wheel
	pdm sync -gp .

docs:
	pdm || $(MAKE) install
	$(MAKE) -C docs html

fonts:
	git clone https://github.com/dominikwilkowski/cfonts.git tmp
	cp tmp/fonts/*.json cfonts/fonts/
	rm -fr tmp

.PHONY: install docs fonts
