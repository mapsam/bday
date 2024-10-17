import subprocess
import boto3
from boto3.dynamodb.conditions import Key
from botocore.config import Config
from bday.models import Bday
from bday.util import build_dt

class BdayDatabase:
    def __init__(self, env):
        self.table = f"bday-{env}"
        self.client = boto3.resource("dynamodb", config=Config(region_name="us-west-2"))
        self.table = self.client.Table(self.table)

    def add_bday(self, **kwargs):
        bday = Bday(
            Name=kwargs.get("name"),
            BirthMonth=kwargs.get("month"),
            BirthDay=kwargs.get("day"),
            BirthYear=kwargs.get("year")
        )
        self.table.put_item(Item=bday.dict())
        return bday

    def get_bday(self, id, day, month):
        dt = build_dt(day=day, month=month)
        res = self.table.get_item(
            Key={
                "BirthDt": dt,
                "Id": id
            }
        )

        if "Item" not in res:
            raise Exception(f"No bday found for {dt}, {id}")
        
        return Bday(**res["Item"])

    def remove_bday():
        print("todo")

    def update_bday():
        print("todo")

    def get_dt(self, day, month):
        dt = build_dt(day=day, month=month)
        res = self.table.query(
            KeyConditionExpression=Key('BirthDt').eq(dt)
        )

        if len(res["Items"]) < 1:
            raise Exception(f"No bdays found for {dt}")

        return list(map(lambda i: Bday(**i), res["Items"]))

    # def list_bdays_by(self, **kwargs):
    #     if kwargs.len > 1:
    #         raise Exception("only one list criteria can be provided")

        
    #     res = self.table.query(
    #         KeyConditions={
    #             "Id": {
    #                 "AttributeValueList": [id],
    #                 "ComparisonOperator": "EQ" 
    #             }
    #         }
    #     )