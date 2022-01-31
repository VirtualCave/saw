import logging

import boto3
from botocore.client import ClientError


class AWSResponseDto:

    KO = "ko"
    OK = "ok"

    def __init__(self):
        self.error = None
        self.response = None

    def get_status(self):
        if self.error:
            return AWSResponseDto.KO
        elif self.response:
            return AWSResponseDto.OK
        else:
            raise RuntimeError(
                "Constructor needs response or error, but booth are None"
            )


class AwsEc2ResponseDto(AWSResponseDto):
    def __init__(self, aws_response: dict = None, error: Exception = None):
        super().__init__()
        if error:
            self.error = error
        elif aws_response:
            self.response = aws_response
        else:
            raise RuntimeError(
                "Constructor needs response or error, but booth are None"
            )

    def dict(self):
        if self.get_status() == AWSResponseDto.KO:
            return {
                "status": self.get_status(),
                "error": repr(self.error),
            }
        else:
            return {"status": self.get_status(), "response": self.response}


class AwsEc2Client:

    EC2 = "ec2"

    def __init__(
        self, aws_access_key_id: str, aws_secret_access_key: str, aws_region: str
    ):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region = aws_region

        self.client = boto3.client(
            AwsEc2Client.EC2,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=self.region,
        )

    def list_resources(self, tags=None):
        if tags:
            logging.info("TODO")
        try:
            ec2_instances_response = self.client.describe_instances()
            reservations = ec2_instances_response.get("Reservations")
            response = []
            for reservation in reservations:
                for instance in reservations:
                    instance = instance["Instances"][0]
                    response.append(
                        {
                            "id": instance["InstanceId"],
                            "reservation": reservation["ReservationId"],
                            "type": instance["InstanceType"],
                            "state": instance["State"]["Name"],
                            "tags": {
                                t["Key"]: t["Value"] for t in instance.get("Tags", {})
                            },
                            "launch_time": instance["LaunchTime"],
                            "owner": reservation["OwnerId"],
                        }
                    )
            return AwsEc2ResponseDto(aws_response=response)
        except ClientError as e:
            logging.error(f"AWS client error: {e}")
            return AwsEc2ResponseDto(error=e)
        except Exception as e:
            logging.error(f"Error processing aws client response: {e}")
