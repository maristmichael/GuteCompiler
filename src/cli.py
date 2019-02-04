#!/usr/bin/env python
import click

@click.command()
@click.option('--file', '-f', 'file_path')
def cli(file_path):
    try:
        message = f'sucessfully compiled {file_path}'
        click.echo(message)
    except Exception as e:
        message = f'compile error: {e}'
        click.echo(message)