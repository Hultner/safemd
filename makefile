# Make file for building safemd

.PHONY : install
install:
	python setup.py install

.PHONY : deploy
deploy:
	rm -rf dist
	python setup.py bdist_wheel sdist --formats gztar
	twine upload dist/*

.PHONY : build
build:
	python setup.py bdist_wheel sdist --formats gztar

.PHONY : test
test:
	pytest

.PHONY : clean
	rm -f MANIFEST
	rm -f *.pyc
	rm -f **/*.pyc
	rm -f **/*.swp
	rm -rf build
	rm -rf dist
	rm -rf tmp
