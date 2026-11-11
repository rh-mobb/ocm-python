# WifGcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**federated_project_id** | **str** | This represents the GCP project ID in which, when specified, the wif workload WorkloadIdentityPool resources will be configured. | [optional] 
**federated_project_number** | **str** | This represents the GCP project number in which, when specified, the wif workload WorkloadIdentityPool resources will be configured. | [optional] 
**impersonator_email** | **str** | This is the service account email that OCM will use to access other SAs.  | [optional] 
**project_id** | **str** | This represents the GCP project ID in which the wif resources will be configured. | [optional] 
**project_number** | **str** | This represents the GCP project number in which the wif resources will be configured. | [optional] 
**role_prefix** | **str** | Prefix for naming GCP custom roles configured. | [optional] 
**service_accounts** | [**List[WifServiceAccount]**](WifServiceAccount.md) | The list of service accounts and their associated roles that will need to be configured on the user&#39;s GCP project. | [optional] 
**support** | [**WifSupport**](WifSupport.md) |  | [optional] 
**workload_identity_pool** | [**WifPool**](WifPool.md) |  | [optional] 

## Example

```python
from ocm_client.models.wif_gcp import WifGcp

# TODO update the JSON string below
json = "{}"
# create an instance of WifGcp from a JSON string
wif_gcp_instance = WifGcp.from_json(json)
# print the JSON string representation of the object
print(WifGcp.to_json())

# convert the object into a dict
wif_gcp_dict = wif_gcp_instance.to_dict()
# create an instance of WifGcp from a dict
wif_gcp_from_dict = WifGcp.from_dict(wif_gcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


