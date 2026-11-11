# AWS

_Amazon Web Services_ specific settings of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | Customer Managed Key to encrypt EBS Volume | [optional] 
**sts** | [**STS**](STS.md) |  | [optional] 
**access_key_id** | **str** | AWS access key identifier. | [optional] 
**account_id** | **str** | AWS account identifier. | [optional] 
**additional_allowed_principals** | **List[str]** | Additional allowed principal ARNs to be added to the hosted control plane&#39;s VPC Endpoint Service. | [optional] 
**additional_compute_security_group_ids** | **List[str]** | Additional AWS Security Groups to be added to default worker (compute) machine pool. | [optional] 
**additional_control_plane_security_group_ids** | **List[str]** | Additional AWS Security Groups to be added to default control plane machine pool. | [optional] 
**additional_infra_security_group_ids** | **List[str]** | Additional AWS Security Groups to be added to default infra machine pool. | [optional] 
**audit_log** | [**AuditLog**](AuditLog.md) |  | [optional] 
**auto_node** | [**AwsAutoNode**](AwsAutoNode.md) |  | [optional] 
**billing_account_id** | **str** | BillingAccountID is the account used for billing subscriptions purchased via the marketplace | [optional] 
**ec2_metadata_http_tokens** | [**Ec2MetadataHttpTokens**](Ec2MetadataHttpTokens.md) |  | [optional] 
**etcd_encryption** | [**AwsEtcdEncryption**](AwsEtcdEncryption.md) |  | [optional] 
**hcp_internal_communication_hosted_zone_id** | **str** | ID of local private hosted zone for hypershift internal communication. | [optional] 
**private_hosted_zone_id** | **str** | ID of private hosted zone. | [optional] 
**private_hosted_zone_role_arn** | **str** | Role ARN for private hosted zone. | [optional] 
**private_link** | **bool** | Sets cluster to be inaccessible externally. | [optional] 
**private_link_configuration** | [**PrivateLinkClusterConfiguration**](PrivateLinkClusterConfiguration.md) |  | [optional] 
**secret_access_key** | **str** | AWS secret access key. | [optional] 
**subnet_ids** | **List[str]** | The subnet ids to be used when installing the cluster. | [optional] 
**tags** | **Dict[str, str]** | Optional keys and values that the installer will add as tags to all AWS resources it creates | [optional] 
**termination_handler_queue_url** | **str** | URL of the SQS queue used for graceful Spot instance interruption handling. When set, HyperShift deploys the AWS Node Termination Handler in the hosted control plane. Queue must be in the same region as the cluster. | [optional] 
**vpc_endpoint_role_arn** | **str** | Role ARN for VPC Endpoint Service cross account role. | [optional] 
**zero_egress** | [**ZeroEgress**](ZeroEgress.md) |  | [optional] 

## Example

```python
from ocm_client.models.aws import AWS

# TODO update the JSON string below
json = "{}"
# create an instance of AWS from a JSON string
aws_instance = AWS.from_json(json)
# print the JSON string representation of the object
print(AWS.to_json())

# convert the object into a dict
aws_dict = aws_instance.to_dict()
# create an instance of AWS from a dict
aws_from_dict = AWS.from_dict(aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


