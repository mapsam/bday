terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_dynamodb_table" "bday" {
  name = "bday-${terraform.workspace}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "BirthDt"
  range_key = "Id"

  attribute {
    name = "BirthDt"
    type = "S" # MM:DD
  }
  attribute {
    name = "Id"
    type = "S"
  }
}