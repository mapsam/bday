import subprocess
import boto3
from botocore.config import Config
from bday.models import Bday

class BdayDatabase:
    def __init__(self, env):
        self.table = f"bday-{env}"
        self.client = boto3.resource("dynamodb", config=Config(region_name="us-west-2"))
        self.table = self.client.Table(self.table)

    def addItem(self, **kwargs):
        bday = Bday(
            Name=kwargs.get("name"),
            BirthMonth=kwargs.get("month"),
            BirthDay=kwargs.get("day"),
            BirthYear=kwargs.get("year")
        )
        self.table.put_item(
            Item=bday.dict()
        )

    def getItem(self, **kwargs):
        item = self.table.query(
            KeyConditionExpression=boto3.Key('Id').eq(kwargs.get('id'))
        )
        print(item)
        bday = Bday(**item["Item"])
        print(bday.model_dump())

    def removeItem():
        print("todo")

    def updateItem():
        print("todo")

    def listItems():
        print("todo")