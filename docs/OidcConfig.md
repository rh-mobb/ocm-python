# OidcConfig

Contains the necessary attributes to support oidc configuration hosting under Red Hat or registering a Customer's byo oidc config.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | HREF for the oidc config, filled in response. | [optional] 
**id** | **str** | ID for the oidc config, filled in response. | [optional] 
**creation_timestamp** | **datetime** | Creation timestamp, filled in response. | [optional] 
**installer_role_arn** | **str** | ARN of the AWS role to assume when installing the cluster as to reveal the secret, supplied in request. It is only to be used in Unmanaged Oidc Config. | [optional] 
**issuer_url** | **str** | Issuer URL, filled in response when Managed and supplied in Unmanaged. | [optional] 
**last_update_timestamp** | **datetime** | Last update timestamp, filled when patching a valid attribute of this oidc config. | [optional] 
**last_used_timestamp** | **datetime** | Last used timestamp, filled by the latest cluster that used this oidc config. | [optional] 
**managed** | **bool** | Indicates whether it is Managed or Unmanaged (Customer hosted). | [optional] 
**organization_id** | **str** | Organization ID, filled in response respecting token provided. | [optional] 
**reusable** | **bool** | Indicates whether the Oidc Config can be reused. | [optional] 
**secret_arn** | **str** | Secrets Manager ARN for the OIDC private key, supplied in request. It is only to be used in Unmanaged Oidc Config. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


