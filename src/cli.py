#!/usr/bin/env python
import click
import gutec
from utilities import STDERR

@click.command()
@click.option('--file', '-f', 'filepath')
def cli(filepath):
    gutec.main(filepath)
    
