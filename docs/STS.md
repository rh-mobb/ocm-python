# STS

Contains the necessary attributes to support role-based authentication on AWS.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc_endpoint_url** | **str** | URL of the location where OIDC configuration and keys are available | [optional] 
**auto_mode** | **bool** | Auto creation mode for cluster - OCM will create the operator roles and OIDC provider. false by default. | [optional] 
**enabled** | **bool** | If STS is enabled or disabled | [optional] 
**external_id** | **str** | Optional unique identifier when assuming role in another account | [optional] 
**instance_iam_roles** | [**InstanceIAMRoles**](InstanceIAMRoles.md) |  | [optional] 
**managed_policies** | **bool** | If true, cluster account and operator roles have managed policies attached. | [optional] 
**oidc_config** | [**OidcConfig**](OidcConfig.md) |  | [optional] 
**operator_iam_roles** | [**list[OperatorIAMRole]**](OperatorIAMRole.md) | List of roles necessary to access the AWS resources of the various operators used during installation | [optional] 
**operator_role_prefix** | **str** | Optional user provided prefix for operator roles. | [optional] 
**permission_boundary** | **str** | Optional user provided permission boundary. | [optional] 
**role_arn** | **str** | ARN of the AWS role to assume when installing the cluster | [optional] 
**support_role_arn** | **str** | ARN of the AWS role used by SREs to access the cluster AWS account in order to provide support | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


