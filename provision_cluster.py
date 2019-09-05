import configparser
import boto3

config = configparser.ConfigParser()
config.read(['aws.cfg', 'dwh.cfg'])

KEY = config.get('AWS','KEY')
SECRET = config.get('AWS','SECRET')
 
redshift = boto3.client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       )

iam = boto3.client('iam',aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     region_name='us-west-2'
                  )

roleArn = iam.get_role(RoleName='dwhRole')['Role']['Arn']

print(config.get("CLUSTER","DB_NAME"))

try:
    response = redshift.create_cluster(        
        ClusterType=config.get("INFRA","DWH_CLUSTER_TYPE"),
        NodeType=config.get("INFRA","DWH_NODE_TYPE"),
        NumberOfNodes=int(config.get("INFRA","DWH_NUM_NODES")),
        ClusterIdentifier=config.get("INFRA","DWH_CLUSTER_IDENTIFIER"),
        DBName=config.get("CLUSTER","DB_NAME"),
        MasterUsername=config.get("CLUSTER","DB_USER"),
        MasterUserPassword=config.get("CLUSTER","DB_PASSWORD"),
        IamRoles=[roleArn]
    )
except Exception as e:
    print(e)