import click

@click.group()
def cli():
    """A CLI app to manage project tasks."""
    pass

@cli.command()
@click.argument('test_name')
def test(test_name):
    """Run tests for the project."""
    click.echo(f"Running test: {test_name}")
    # Here you would implement your test logic
    # For example, you could call a testing framework like unittest or pytest
    click.echo("Tests completed successfully.")

@cli.command()
def build():
    """Build the project."""
    click.echo("Building the project...")
    # Implement your build logic here
    click.echo("Project built successfully.")

@cli.command()
@click.argument('version')
def pkg(version):
    """Package the project for distribution."""
    click.echo(f"Packaging the project version: {version}...")
    # Implement your packaging logic here
    click.echo("Project packaged successfully.")

@cli.command()
@click.option('--action', type=click.Choice(['submit', 'review'], case_sensitive=False))
def admin(action):
    """Admin operations."""
    if action == 'submit':
        click.echo("Submitting the project...")
        # Implement your submission logic here
        click.echo("Project submitted successfully.")
    elif action == 'review':
        click.echo("Reviewing the project...")
        # Implement your review logic here
        click.echo("Project reviewed successfully.")

if __name__ == '__main__':
    cli()