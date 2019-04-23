
SHELL:=/bin/bash
ENV = ./gutecENV/bin/activate

.PHONY: all install clean

all: install

install:
	bash -c "python3 -m venv ./gutecENV; source $(ENV); pip3 install gutec;"
	chmod +x activate.sh

clean:
	rm -rf ./gutecENV