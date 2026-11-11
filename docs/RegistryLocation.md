# RegistryLocation

RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '*' or '??'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | domainName specifies a domain name for the registry In case the registry use non-standard (80 or 443) port, the port should be included in the domain name as well. | [optional] 
**insecure** | **bool** | insecure indicates whether the registry is secure (https) or insecure (http) By default (if not specified) the registry is assumed as secure. | [optional] 

## Example

```python
from ocm_client.models.registry_location import RegistryLocation

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryLocation from a JSON string
registry_location_instance = RegistryLocation.from_json(json)
# print the JSON string representation of the object
print(RegistryLocation.to_json())

# convert the object into a dict
registry_location_dict = registry_location_instance.to_dict()
# create an instance of RegistryLocation from a dict
registry_location_from_dict = RegistryLocation.from_dict(registry_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


