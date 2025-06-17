import rich_click as click

# 'main' is the click.Group object referenced in pyproject.toml
@click.group()
def hello_group():
    """
    A hello world extension for the ArmoniK CLI.
    The docstring of the group is used as its help text.
    """
    pass

@hello_group.command()
@click.option('--name', default='World', help='The name to greet.')
def say(name):
    """Prints a greeting."""
    click.echo(f"Hello, {name}!")
