# coding: utf-8
import boto3
session = boto3.Session(profile_name='shotty2')
instances = ec2.session.all()
s3 = session.resource('s3')

    
