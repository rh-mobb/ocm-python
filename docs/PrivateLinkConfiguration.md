# PrivateLinkConfiguration

Manages the configuration for the Private Links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principals** | [**PrivateLinkPrincipals**](PrivateLinkPrincipals.md) |  | [optional] 

## Example

```python
from ocm_client.models.private_link_configuration import PrivateLinkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLinkConfiguration from a JSON string
private_link_configuration_instance = PrivateLinkConfiguration.from_json(json)
# print the JSON string representation of the object
print(PrivateLinkConfiguration.to_json())

# convert the object into a dict
private_link_configuration_dict = private_link_configuration_instance.to_dict()
# create an instance of PrivateLinkConfiguration from a dict
private_link_configuration_from_dict = PrivateLinkConfiguration.from_dict(private_link_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


