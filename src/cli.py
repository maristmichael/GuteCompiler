#!/usr/bin/env python
import click
import gutec
import subprocess

@click.command()
@click.option('--file', '-f', 'filepath')
def cli(filepath):
    try:
        gutec.main(filepath)
    except Exception as e:
        message = f'compile error: {e}'
        click.echo(message)


# @click.command()
# @click.option('--quit', '-q')
# def cli():
#     try:
#         subprocess.Popen("deactivate")
#     except Exception as e:
#         message = f'some error, idk...'
#         click.echo(message)
