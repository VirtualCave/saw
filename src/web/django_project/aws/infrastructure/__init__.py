import logging

import boto3
from botocore.client import ClientError

from aws.infrastructure.dtos import AwsEc2Client

S3 = "s3"
EC2 = "ec2"


def scan_resources(
    access_key_id, secret_access_key, region, service=None, business=None
):
    result = dict()
    result["s3"] = s3_scan(access_key_id, secret_access_key)

    result["ec2"] = ec2_scan(access_key_id, secret_access_key, region)
    return result


def ec2_scan(access_key_id, secret_access_key, region):
    ec2 = AwsEc2Client(access_key_id, secret_access_key, region)
    ec2_response_dto = ec2.list_resources()
    return ec2_response_dto.dict()


def s3_scan(access_key_id, secret_access_key):
    s3_client = boto3.client(
        S3, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key
    )
    response = s3_client.list_buckets()
    owner = response["Owner"]["ID"]
    buckets = []
    for b in response["Buckets"]:
        buckets.append(
            {
                "name": b["Name"],
                "creation_date": b["CreationDate"],
                "tags": s3_get_bucket_tags(s3_client, b["Name"]),
            }
        )
    return {"owner": owner, "buckets": buckets}


def s3_get_bucket_tags(s3_client, bucket_name):
    try:
        tags_response = s3_client.get_bucket_tagging(Bucket=bucket_name)
    except ClientError as e:
        logging.error(f"Client error: {e}")
        return {}
    bucket_tags = tags_response.get("TagSet", [])
    return {bt["Key"]: bt["Value"] for bt in bucket_tags}
