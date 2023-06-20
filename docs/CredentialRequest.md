# CredentialRequest

Contains the necessary attributes to allow each operator to access the necessary AWS resources
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credentials secret used to access cloud resources | [optional] 
**namespace** | **str** | Namespace where the credentials secret lives in the cluster | [optional] 
**policy_permissions** | **list[str]** | List of policy permissions needed to access cloud resources | [optional] 
**service_account** | **str** | Service account name to use when authenticating | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


