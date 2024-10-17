import click
import json
from pydantic.json import pydantic_encoder
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
    """Add a birthday"""
    db = BdayDatabase("dev")
    bday = db.add_bday(name=name, month=month, day=day, year=year)
    click.echo(bday.model_dump_json())

@main.command()
@click.option("--id", required=True, help="bday id", type=str)
@click.option("--day", required=True, help="birth day", type=int)
@click.option("--month", required=True, help="birth month", type=int)
def get(id, day, month):
    """Get a birthday"""
    db = BdayDatabase("dev")
    bday = db.get_bday(id, day, month)
    click.echo(bday.model_dump_json())

@main.command()
@click.option("--day", required=False, default=None, help="birth day", type=int)
@click.option("--month", required=False, default=None, help="birth month", type=int)
def ls(day, month):
    """List birthdays"""
    db = BdayDatabase("dev")
    bdays = db.get_dt(day, month)
    click.echo(json.dumps(bdays, default=pydantic_encoder))
