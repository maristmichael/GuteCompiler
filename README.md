# GuteCompiler
## Overview
This is a compiler built from scratch using Python3.
The language used is follows [this grammar specification](./grammar.pdf).


## Requirements
- Python3.7

## Setting up the Compiler

If you don't feel like dowloading the project itself, you can simple run:

``` python3 -m venv ./gutecENV; source ./gutecENV/bin/activate; pip3 install gutec; ```

And skip to 'Running the Compiler' otherwise, you can follow the commands below.

1. Setup the project requirements and create the environment:

    ```make``` 

2. Workon the python virtual environment

    ``` `./activate.sh` ```  (includes accents)


## Running up the Compiler

After all that magic, you're ready to use my compiler.

Compile a file:

```gutec path_to_a_file```

## Cleanup

1. Exit the virtual environment

    ```deactivate```

2. Delete the guteENV virtual environment directory