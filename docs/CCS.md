# CCS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;CCS&#39; if this is a complete object or &#39;CCSLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**disable_scp_checks** | **bool** | Indicates if cloud permissions checks are disabled, when attempting installation of the cluster. | [optional] 
**enabled** | **bool** | Indicates if Customer Cloud Subscription is enabled on the cluster. | [optional] 

## Example

```python
from ocm_client.models.ccs import CCS

# TODO update the JSON string below
json = "{}"
# create an instance of CCS from a JSON string
ccs_instance = CCS.from_json(json)
# print the JSON string representation of the object
print(CCS.to_json())

# convert the object into a dict
ccs_dict = ccs_instance.to_dict()
# create an instance of CCS from a dict
ccs_from_dict = CCS.from_dict(ccs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


