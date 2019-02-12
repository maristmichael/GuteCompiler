#!/usr/bin/env python
import click
import gutec

@click.command()
@click.option('--file', '-f', 'filepath')
def cli(filepath):
    try:
        gutec.main(filepath)
    except Exception as e:
        message = f'compile error: {e}'
        click.echo(message)