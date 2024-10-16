import click
from bday.db import BdayDatabase

@click.group()
def main():
    """bday cli"""
    pass

@main.command()
@click.option("--name", required=True, help="birth person", type=str)
@click.option("--month", required=True, help="birth month", type=int)
@click.option("--day", required=True, help="birth day", type=int)
@click.option("--year", required=False, default=None, help="birth year", type=int)
def add(name, year, month, day):
    """Add a birthday."""
    db = BdayDatabase("dev")
    click.echo(f"Adding {name}, {year}-{month}-{day}")

@main.command()
@click.option("--month", required=False, default=None, help="birth month", type=int)
@click.option("--day", required=False, default=None, help="birth day", type=int)
@click.option("--year", required=False, default=None, help="birth year", type=int)
def ls(year, month, day):
    """List birthdays."""
    click.echo(f"Listing {year}-{month}-{day}")
