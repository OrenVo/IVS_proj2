# Makefile for Deus Vult calculator

.PHONY: all clean test ins pack
all: ins run

run: main.py
	python main.py

ins:
	pip install -r Requirements.txt

test: deus_math_lib.py test_deus_math_lib.py
	pytest
clean:
	rmdir /Q /S ".pytest_cache" "__pycache__" 

pack:

doc:
	cd .. && rm -rf /doc
	doxygen
