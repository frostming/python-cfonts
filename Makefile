docs:
	make -C docs html
	cd docs/_build/html && git add -A && git commit -m "update docs"
	cd docs/_build/html && git push origin gh-pages

fonts:
	git clone https://github.com/dominikwilkowski/cfonts.git tmp
	cp tmp/fonts/*.json cfonts/fonts/
	rm -fr tmp

.PHONY: docs fonts
