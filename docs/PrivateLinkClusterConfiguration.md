# PrivateLinkClusterConfiguration

Manages the configuration for the Private Links.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principals** | [**List[PrivateLinkPrincipal]**](PrivateLinkPrincipal.md) | List of additional principals for the Private Link | [optional] 

## Example

```python
from ocm_client.models.private_link_cluster_configuration import PrivateLinkClusterConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateLinkClusterConfiguration from a JSON string
private_link_cluster_configuration_instance = PrivateLinkClusterConfiguration.from_json(json)
# print the JSON string representation of the object
print(PrivateLinkClusterConfiguration.to_json())

# convert the object into a dict
private_link_cluster_configuration_dict = private_link_cluster_configuration_instance.to_dict()
# create an instance of PrivateLinkClusterConfiguration from a dict
private_link_cluster_configuration_from_dict = PrivateLinkClusterConfiguration.from_dict(private_link_cluster_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


