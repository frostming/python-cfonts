docs:
	make -C docs html
	cd docs/_build/html && git add -A && git commit -m "update docs"
	cd docs/_build/html && git push origin gh-pages

.PHONY: docs
