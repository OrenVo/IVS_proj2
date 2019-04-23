# Makefile for Deus Vult calculator

.PHONY: all clean test ins pack
all: run

run: main.py
	python main.py

ins:
	pip install -r Requirements.txt

test: deus_math_lib.py test_deus_math_lib.py
	pytest
clean:
	rmdir /S /Q ..\doc ..\pack .\__pycache__ .\.pytest_cache
	rm *.pyc


pack:
	mkdir ..\pack
	mkdir ..\pack\repo
	mkdir ..\pack\install
	mkdir ..\pack\documentation
	copy /Y ..\* ..\pack\repo
	mkdir ..\pack\repo\src
	copy /Y .\* ..\pack\repo\src
profile:
	python -m cProfile ./deus_profiling.py <profiling.txt

doc:

	doxygen
help:
	echo To run this app, first install python (3.5 minimal version). Then run make ins - to install all dependencies. Then you can run the calculator by running main.py script.
