import click

from secret_injector.runner import run_secret_injector


@click.command()
def secret_injector_cli():
    click.echo('Hello World!')
    run_secret_injector()

