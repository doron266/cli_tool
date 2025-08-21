from email.policy import default

import click
import random
import boto3

s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

@click.command()
@click.argument('obj')
@click.option('-t','--instance_type', help='Takes t2.small or t3.micro')
@click.option('-n', '--name', default='', help="Name of object")
def create(obj, instance_type, name):
    match obj:
        case 's3':
            s3.create_bucket(Bucket=name)
            click.echo(f"obj: {obj} name: {name} created successfully")
    pass

@click.command()
@click.argument('obj')
def list_objects(obj):
    # for item in ns:
    #     if item.keys()[0] == obj:
    #         match item.keys()[0]:
    #             case 'ec2':
    #                 click.echo(f"{item['created_by']} {item['owner']} {item['type']}")
    pass

@click.command()
@click.argument('obj')
def delete(obj):
    pass

@click.command()
@click.argument('obj')
def stop(obj):
    pass

@click.command()
@click.argument('obj')
def start(obj):
    pass


@click.command()
def number():
    click.echo(random.randint(1, 10))

    pass

