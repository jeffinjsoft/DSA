import boto3
from botocore.exceptions import ClientError

from common.models import Ami,InstanceProfile,Vpc,Sg,InstanceType,Keypair,Eip,Volume

def check_amis(a_id):
    """
    check for all amis and update models
    """


    try:
        ami_client = boto3.client('ec2')
        response = ami_client.describe_images(ExecutableUsers=[a_id])
    except ClientError as e:
        print e
    a_out = []
    for i in response['Images']:
        t = {}
        t[i['ImageId']]=i['Name']
        a_out.append(t)

    if len(a_out) == 0:
        print 'No amis found in %s'%a_id
        Ami.objects.all().delete()
        print 'Adding ubuntu 16 image'
        m = Ami(name='ubuntu',ami_id='ami-b35471dc')
        m.save()
    else:
        # delete all amis from DB
        Ami.objects.all().delete()
        #save new vales
        for a in a_out:
            for v in a:
                m = Ami(name=a[v],ami_id=v)
                m.save()
        print 'Successfully added amis'

def check_profiles():
    """
    check for all instance profiles and update models
    """

    # find instance profiles using boto3
    try:
        pro_client = boto3.client('iam')
        response = pro_client.list_instance_profiles()
    except ClientError as e:
        print e
    p_out = []

    for i in response['InstanceProfiles']:
        t = {}
        t[i['InstanceProfileName']]=i['Arn']
        p_out.append(t)

    if len(p_out) == 0:
        print 'No instance profiles found.'
    else:
        # delete all amis from DB
        InstanceProfile.objects.all().delete()
        #save new vales

        for a in p_out:
            for v in a:
                m = InstanceProfile(name=v,arn=a[v])
                m.save()
        print 'Successfully added pfofiles'



def check_types():
    """
    return all instance types and save to model
    """

    t_out = [ 't2.micro','t2.nano','t2.micro','t2.small','t2.medium','t2.large','t2.xlarge','t2.2xlarge','m1.small','m1.medium','m1.large','m1.xlarge','m3.medium','m3.large','m3.xlarge','m3.2xlarge','m4.large','m4.xlarge','m4.2xlarge','m4.4xlarge','m4.10xlarge','m4.16xlarge','m2.xlarge',
    'm2.2xlarge','m2.4xlarge','cr1.8xlarge','r3.large','r3.xlarge','r3.2xlarge','r3.4xlarge','r3.8xlarge','r4.large','r4.xlarge','r4.2xlarge','r4.4xlarge','r4.8xlarge','r4.16xlarge','x1.16xlarge','x1.32xlarge','x1e.xlarge','x1e.2xlarge','x1e.4xlarge','x1e.8xlarge','x1e.16xlarge','x1e.32xlarge','i2.xlarge','i2.2xlarge','i2.4xlarge',
    'i2.8xlarge','i3.large','i3.xlarge','i3.2xlarge','i3.4xlarge','i3.8xlarge','i3.16xlarge','hi1.4xlarge','hs1.8xlarge','c1.medium','c1.xlarge','c3.large','c3.xlarge','c3.2xlarge','c3.4xlarge','c3.8xlarge','c4.large','c4.xlarge','c4.2xlarge','c4.4xlarge','c4.8xlarge','c5.large','c5.xlarge','c5.2xlarge','c5.4xlarge',
    'c5.9xlarge','c5.18xlarge','cc1.4xlarge','cc2.8xlarge','g2.2xlarge','g2.8xlarge','g3.4xlarge','g3.8xlarge','g3.16xlarge','cg1.4xlarge','p2.xlarge','p2.8xlarge','p2.16xlarge','p3.2xlarge','p3.8xlarge','p3.16xlarge','d2.xlarge','d2.2xlarge','d2.4xlarge','d2.8xlarge','f1.2xlarge','f1.16xlarge','m5.large','m5.xlarge','m5.2xlarge',
    'm5.4xlarge','m5.12xlarge','m5.24xlarge','h1.2xlarge','h1.4xlarge','h1.8xlarge','h1.16xlarge']

    InstanceType.objects.all().delete()

    for a in t_out:
        m = InstanceType(name=a)
        m.save()
    print 'Successfully added instance types'

def check_keys():
    """
    return all key pairs and save to model
    """
    try:
        k_client = boto3.client('ec2')
        response = k_client.describe_key_pairs()
    except ClientError as e:
        print e
    k_out = []
    for i in response['KeyPairs']:
        k_out.append(i['KeyName'])

    if len(k_out) == 0:

        print 'No keys found.'
    else:

        Keypair.objects.all().delete()
        for a in k_out:
            m = Keypair(name=a)
            m.save()
        print 'Successfully added keypairs'



def check_sgs():
    """
    return all sgs and save to model
    """
    try:
        s_client = boto3.client('ec2')
        response = s_client.describe_security_groups()
    except ClientError as e:
        print e
    s_out = []
    for i in response['SecurityGroups']:
        t = {}
        t['GroupId']=i['GroupId']
        t['VpcId'] = i['VpcId']
        t['GroupName'] = i['GroupName']

        s_out.append(t)

    if len(s_out) == 0:
        print 'No security groups found'
    else:
        Sg.objects.all().delete()

        for a in s_out:
            # print a
            # print a
            v = Vpc.objects.get(vpc_id=a['VpcId'])

            m = Sg(name=a['GroupName'],sg_id=a['GroupId'],vpc=v)
            m.save()

        print 'Successfully added security groups'


def get_tag_name(t_l):
    out = ''
    # print t_l
    for x in t_l:
        if x['Key']=='Name':
            out = x['Value']
    return out
def check_vpcs():
    """
    return all vpcs and save to model
    """
    try:
        v_client = boto3.client('ec2')
        response = v_client.describe_vpcs()
    except ClientError as e:
        print e
    v_out = []

    for i in response['Vpcs']:
        t = {}
        n = get_tag_name(i['Tags'])
        t[i['VpcId']] = n
        v_out.append(t)

    if len(v_out) == 0:
        print 'No Vpcs found'
    else:
        Vpc.objects.all().delete()

        for a in v_out:
            for v in a:
                m = Vpc(vpc_id=v,name=a[v])
                m.save()
        print 'Successfully added VPCS'


def check_eips():
    """
    check for all elastic ips and update models
    """

    # find instance profiles using boto3
    try:
        eip_client = boto3.client('ec2')
        response = eip_client.describe_addresses()
    except ClientError as e:
        print e
    e_out = []

    for i in response['Addresses']:
        t = {}
        if 'AllocationId' in i.keys():
            t[i['PublicIp']]=i['AllocationId']
        if len(t)>0:
            e_out.append(t)


    if len(e_out) == 0:
        print 'No elastic ips found.'
    else:
        # delete all amis from DB
        Eip.objects.all().delete()
        #save new vales

        for a in e_out:
            for v in a:
                m = Eip(eip=v,allow_id=a[v])
                m.save()
        print 'Successfully added eips'


def check_volumes():
    """
    check for all volumes and update models
    """

    # find instance profiles using boto3
    try:
        v_client = boto3.client('ec2')
        response = v_client.describe_volumes()
    except ClientError as e:
        print e
    # v_out = []

    # for i in response['Volumes']:
    #     t = {}
    #     print i
    #     e_out.append(t)


    if len(response['Volumes']) == 0:
        print 'No elastic ips found.'
    else:
        # delete all amis from DB
        Volume.objects.all().delete()
        #save new vales

        for a in response['Volumes']:
            if len(a['Attachments'])>0:
                m = Volume(vid=a['VolumeId'],instance_id=a['Attachments'][0]['InstanceId'],a_zone=a['AvailabilityZone'],snap_id=a['SnapshotId'],state=a['State'])
            else:
                m = Volume(vid=a['VolumeId'],a_zone=a['AvailabilityZone'],snap_id=a['SnapshotId'],state=a['State'])
            m.save()

        print 'Successfully added volumes'
        # pass
