import boto3
import click

s3 = boto3.resource('s3')

###### Click modules creating list bucket function and cli commands:

@click.group()
def cli() :
    "Webotronica deploys websites to Mars AWS Data Centers"
    pass

@cli.command('list-buckets')
def list_buckets() :
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects( bucket):
    "Lists the bucket objects"
    for obj in s3.Bucket('bucket').objects.all():
        print(obj)

##### Main functoin
if __name__ == "__main__" :
    cli()
