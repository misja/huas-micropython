all: collect build

build: collect
	python3 -m build

collect:
	python3 util.py --dest src

publish: build
	python3 -m twine upload dist/*

clean:
	rm -rf src/* dist