# RegistrySources

RegistrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds and pods. For instance, whether or not to allow insecure access. It does not contain configuration for the internal cluster registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_registries** | **List[str]** | AllowedRegistries: registries for which image pull and push actions are allowed. To specify all subdomains, add the asterisk (*) wildcard character as a prefix to the domain name. For example, *.example.com. You can specify an individual repository within a registry. For example: reg1.io/myrepo/myapp:latest. All other registries are blocked. Mutually exclusive with &#x60;BlockedRegistries&#x60; | [optional] 
**blocked_registries** | **List[str]** | BlockedRegistries: registries for which image pull and push actions are denied. To specify all subdomains, add the asterisk (*) wildcard character as a prefix to the domain name. For example, *.example.com. You can specify an individual repository within a registry. For example: reg1.io/myrepo/myapp:latest. All other registries are allowed. Mutually exclusive with &#x60;AllowedRegistries&#x60; | [optional] 
**insecure_registries** | **List[str]** | InsecureRegistries are registries which do not have a valid TLS certificate or only support HTTP connections. To specify all subdomains, add the asterisk (*) wildcard character as a prefix to the domain name. For example, *.example.com. You can specify an individual repository within a registry. For example: reg1.io/myrepo/myapp:latest. | [optional] 

## Example

```python
from ocm_client.models.registry_sources import RegistrySources

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrySources from a JSON string
registry_sources_instance = RegistrySources.from_json(json)
# print the JSON string representation of the object
print(RegistrySources.to_json())

# convert the object into a dict
registry_sources_dict = registry_sources_instance.to_dict()
# create an instance of RegistrySources from a dict
registry_sources_from_dict = RegistrySources.from_dict(registry_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


