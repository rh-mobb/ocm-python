# ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[KeyRing]**](KeyRing.md) | Retrieved list of key rings. | [optional] 
**page** | **int** | Index of the returned page, where one corresponds to the first page. As this collection doesn&#39;t support paging the result will always be &#x60;1&#x60;. | [optional] 
**size** | **int** | Number of items that will be contained in the returned page. As this collection doesn&#39;t support paging or searching the result will always be the total number of key rings of the provider. | [optional] 
**total** | **int** | Total number of items of the collection that match the search criteria, regardless of the size of the page. As this collection doesn&#39;t support paging or searching the result will always be the total number of available key rings of the provider. | [optional] 

## Example

```python
from ocm_client.models.api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response import ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response from a JSON string
api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response_instance = ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response.to_json())

# convert the object into a dict
api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response_dict = api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response_instance.to_dict()
# create an instance of ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response from a dict
api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response_from_dict = ApiClustersMgmtV1GcpInquiriesKeyRingsPost200Response.from_dict(api_clusters_mgmt_v1_gcp_inquiries_key_rings_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


