# AWS

_Amazon Web Services_ specific settings of a cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | Customer Managed Key to encrypt EBS Volume | [optional] 
**sts** | [**STS**](STS.md) |  | [optional] 
**access_key_id** | **str** | AWS access key identifier. | [optional] 
**account_id** | **str** | AWS account identifier. | [optional] 
**audit_log** | [**AuditLog**](AuditLog.md) |  | [optional] 
**billing_account_id** | **str** | BillingAccountID is the account used for billing subscriptions purchased via the marketplace | [optional] 
**ec2_metadata_http_tokens** | [**Ec2MetadataHttpTokens**](Ec2MetadataHttpTokens.md) |  | [optional] 
**etcd_encryption** | [**AwsEtcdEncryption**](AwsEtcdEncryption.md) |  | [optional] 
**private_link** | **bool** | Sets cluster to be inaccessible externally. | [optional] 
**private_link_configuration** | [**PrivateLinkClusterConfiguration**](PrivateLinkClusterConfiguration.md) |  | [optional] 
**secret_access_key** | **str** | AWS secret access key. | [optional] 
**subnet_ids** | **list[str]** | The subnet ids to be used when installing the cluster. | [optional] 
**tags** | **dict(str, str)** | Optional keys and values that the installer will add as tags to all AWS resources it creates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


