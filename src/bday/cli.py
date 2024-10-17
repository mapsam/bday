import click
from bday.db import BdayDatabase

@click.group()
def main():
    """bday cli"""
    pass

@main.command()
@click.option("--name", required=True, help="birth person", type=str)
@click.option("--day", required=True, help="birth day", type=int)
@click.option("--month", required=True, help="birth month", type=int)
@click.option("--year", required=False, default=None, help="birth year", type=int)
def add(name, day, month, year):
    """Add a birthday."""
    db = BdayDatabase("dev")
    db.addItem(name=name, month=month, day=day, year=year)

@main.command()
@click.option("--id", required=True, help="bday id", type=str)
def get(id):
    """Get a birthday by id."""
    db = BdayDatabase("dev")
    db.getItem(id=id)

@main.command()
@click.option("--month", required=False, default=None, help="birth month", type=int)
@click.option("--day", required=False, default=None, help="birth day", type=int)
@click.option("--year", required=False, default=None, help="birth year", type=int)
def ls(year, month, day):
    """List birthdays."""
    click.echo(f"Listing {year}-{month}-{day}")
