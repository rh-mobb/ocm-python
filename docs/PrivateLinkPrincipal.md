# PrivateLinkPrincipal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;PrivateLinkPrincipal&#39; if this is a complete object or &#39;PrivateLinkPrincipalLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**principal** | **str** | ARN for a principal that is allowed for this Private Link. | [optional] 

## Example

```python
from ocm_client.models.private_link_principal import PrivateLinkPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLinkPrincipal from a JSON string
private_link_principal_instance = PrivateLinkPrincipal.from_json(json)
# print the JSON string representation of the object
print(PrivateLinkPrincipal.to_json())

# convert the object into a dict
private_link_principal_dict = private_link_principal_instance.to_dict()
# create an instance of PrivateLinkPrincipal from a dict
private_link_principal_from_dict = PrivateLinkPrincipal.from_dict(private_link_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


