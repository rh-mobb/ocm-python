# ClusterRegistryConfig

ClusterRegistryConfig describes the configuration of registries for the cluster. Its format reflects the OpenShift Image Configuration, for which docs are available on [docs.openshift.com](https://docs.openshift.com/container-platform/4.16/openshift_images/image-configuration.html) ```json {    \"registry_config\": {      \"registry_sources\": {        \"blocked_registries\": [          \"badregistry.io\",          \"badregistry8.io\"        ]      }    } } ``` 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_trusted_ca** | **Dict[str, str]** | A map containing the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust. | [optional] 
**allowed_registries_for_import** | [**List[RegistryLocation]**](RegistryLocation.md) | AllowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions. | [optional] 
**platform_allowlist** | [**RegistryAllowlist**](RegistryAllowlist.md) |  | [optional] 
**registry_sources** | [**RegistrySources**](RegistrySources.md) |  | [optional] 

## Example

```python
from ocm_client.models.cluster_registry_config import ClusterRegistryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegistryConfig from a JSON string
cluster_registry_config_instance = ClusterRegistryConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterRegistryConfig.to_json())

# convert the object into a dict
cluster_registry_config_dict = cluster_registry_config_instance.to_dict()
# create an instance of ClusterRegistryConfig from a dict
cluster_registry_config_from_dict = ClusterRegistryConfig.from_dict(cluster_registry_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


