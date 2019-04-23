
SHELL:=/bin/bash

.PHONY: all install clean

all: install

install:
	bash -c "python3 -m venv ./gutecENV; source ./gutecENV/bin/activate; pip3 install gutec;"
	chmod +x activate.sh

clean:
	rm -rf ./gutecENV