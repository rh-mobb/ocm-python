# ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ImageMirror]**](ImageMirror.md) | Retrieved list of image mirrors. | [optional] 
**page** | **int** | Index of the requested page, where one corresponds to the first page. | [optional] 
**size** | **int** | Number of items contained in the returned page. | [optional] 
**total** | **int** | Total number of items of the collection. | [optional] 

## Example

```python
from ocm_client.models.api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response import ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response from a JSON string
api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response_instance = ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response.to_json())

# convert the object into a dict
api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response_dict = api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response_instance.to_dict()
# create an instance of ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response from a dict
api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response_from_dict = ApiClustersMgmtV1ClustersClusterIdImageMirrorsGet200Response.from_dict(api_clusters_mgmt_v1_clusters_cluster_id_image_mirrors_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


