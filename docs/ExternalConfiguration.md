# ExternalConfiguration

Representation of cluster external configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[Label]**](Label.md) | list of labels externally configured on the clusterdeployment. | [optional] 
**manifests** | [**List[Manifest]**](Manifest.md) | list of manifest externally configured for a hosted cluster. | [optional] 
**syncsets** | [**List[Syncset]**](Syncset.md) | list of syncsets externally configured on the cluster. | [optional] 

## Example

```python
from ocm_client.models.external_configuration import ExternalConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalConfiguration from a JSON string
external_configuration_instance = ExternalConfiguration.from_json(json)
# print the JSON string representation of the object
print(ExternalConfiguration.to_json())

# convert the object into a dict
external_configuration_dict = external_configuration_instance.to_dict()
# create an instance of ExternalConfiguration from a dict
external_configuration_from_dict = ExternalConfiguration.from_dict(external_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


