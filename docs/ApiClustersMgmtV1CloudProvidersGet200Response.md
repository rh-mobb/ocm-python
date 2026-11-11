# ApiClustersMgmtV1CloudProvidersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CloudProvider]**](CloudProvider.md) | Retrieved list of cloud providers. | [optional] 
**page** | **int** | Index of the requested page, where one corresponds to the first page. | [optional] 
**size** | **int** | Maximum number of items that will be contained in the returned page. | [optional] 
**total** | **int** | Total number of items of the collection that match the search criteria, regardless of the size of the page. | [optional] 

## Example

```python
from ocm_client.models.api_clusters_mgmt_v1_cloud_providers_get200_response import ApiClustersMgmtV1CloudProvidersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClustersMgmtV1CloudProvidersGet200Response from a JSON string
api_clusters_mgmt_v1_cloud_providers_get200_response_instance = ApiClustersMgmtV1CloudProvidersGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiClustersMgmtV1CloudProvidersGet200Response.to_json())

# convert the object into a dict
api_clusters_mgmt_v1_cloud_providers_get200_response_dict = api_clusters_mgmt_v1_cloud_providers_get200_response_instance.to_dict()
# create an instance of ApiClustersMgmtV1CloudProvidersGet200Response from a dict
api_clusters_mgmt_v1_cloud_providers_get200_response_from_dict = ApiClustersMgmtV1CloudProvidersGet200Response.from_dict(api_clusters_mgmt_v1_cloud_providers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


