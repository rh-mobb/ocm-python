# ApiClustersMgmtV1AwsInquiriesRegionsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CloudRegion]**](CloudRegion.md) | Retrieved list of regions. | [optional] 
**page** | **int** | Index of the returned page, where one corresponds to the first page. As this collection doesn&#39;t support paging the result will always be &#x60;1&#x60;. | [optional] 
**size** | **int** | Number of items that will be contained in the returned page. As this collection doesn&#39;t support paging or searching the result will always be the total number of regions of the provider. | [optional] 
**total** | **int** | Total number of items of the collection that match the search criteria, regardless of the size of the page. As this collection doesn&#39;t support paging or searching the result will always be the total number of available regions of the provider. | [optional] 

## Example

```python
from ocm_client.models.api_clusters_mgmt_v1_aws_inquiries_regions_post200_response import ApiClustersMgmtV1AwsInquiriesRegionsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClustersMgmtV1AwsInquiriesRegionsPost200Response from a JSON string
api_clusters_mgmt_v1_aws_inquiries_regions_post200_response_instance = ApiClustersMgmtV1AwsInquiriesRegionsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiClustersMgmtV1AwsInquiriesRegionsPost200Response.to_json())

# convert the object into a dict
api_clusters_mgmt_v1_aws_inquiries_regions_post200_response_dict = api_clusters_mgmt_v1_aws_inquiries_regions_post200_response_instance.to_dict()
# create an instance of ApiClustersMgmtV1AwsInquiriesRegionsPost200Response from a dict
api_clusters_mgmt_v1_aws_inquiries_regions_post200_response_from_dict = ApiClustersMgmtV1AwsInquiriesRegionsPost200Response.from_dict(api_clusters_mgmt_v1_aws_inquiries_regions_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


