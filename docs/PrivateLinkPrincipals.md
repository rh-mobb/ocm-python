# PrivateLinkPrincipals

Contains a list of principals for the Private Link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;PrivateLinkPrincipals&#39; if this is a complete object or &#39;PrivateLinkPrincipalsLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**principals** | [**List[PrivateLinkPrincipal]**](PrivateLinkPrincipal.md) | List of additional principals for the Private Link | [optional] 

## Example

```python
from ocm_client.models.private_link_principals import PrivateLinkPrincipals

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLinkPrincipals from a JSON string
private_link_principals_instance = PrivateLinkPrincipals.from_json(json)
# print the JSON string representation of the object
print(PrivateLinkPrincipals.to_json())

# convert the object into a dict
private_link_principals_dict = private_link_principals_instance.to_dict()
# create an instance of PrivateLinkPrincipals from a dict
private_link_principals_from_dict = PrivateLinkPrincipals.from_dict(private_link_principals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


