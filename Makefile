all: collect build

collect:
	python3 collect.py --dest src

build: collect
	python3 -m build

test: build
	twine upload --repository testpypi dist/*

publish: build
	twine upload dist/*

clean:
	rm -rf src build dist
