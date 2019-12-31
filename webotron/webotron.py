import boto3
import click

session = boto3.Session(profile_name='shotty2')
s3 = session.resource('s3')


@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "Lists all s3 buckets"
    print("----------  List of all s3 buckets  ----------")
    for i in s3.buckets.all():
        print(i.name)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "Lists contents of bucket"
    contents = s3.Bucket(bucket).objects.all()
    for i in contents:
        print(i)

if __name__ == '__main__':
       cli() 
        
