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

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and configure S3 bucket"
    s3_bucket = s3.create_bucket(Bucket=bucket)

    policy = """
    {
        "Version":"2012-10-17",
        "Statement":[{
        "Sid":"PublicReadGetObject",
        "Effect":"Allow",
        "Principal": "*",
        "Action":["s3:GetObject"],
        "Resource":["arn:aws:s3:::%s/*"
                    ]   
                }
            ]
        }
    """% s3_bucket.name

    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)
    
    ws = new_bucket.Website()
    ws.put(WebsiteConfiguration={
        'ErrorDocument': {
        'Key': 'error.html'
            },
        'IndexDocument': {
        'Suffix': 'index.html'
    }})
    
    url = "http://%s.s3-website-us-east-1.amazonaws.com % s3_bucket.name"

    return


if __name__ == '__main__':
       cli() 
        
