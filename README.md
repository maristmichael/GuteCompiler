# GuteCompiler
## Overview
This is a compiler built from scratch using Python3.
The language used is follows [this grammar specification](./grammar.pdf).


## Requirements
- Python3.7

## Setting up the Compiler
In a terminal or command line, navigate to the directory of the project

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

2. Clean the directory of the env

    ```make clean```