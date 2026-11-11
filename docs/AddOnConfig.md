# AddOnConfig

Representation of an add-on config. The attributes under it are to be used by the addon once its installed in the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnConfig&#39; if this is a complete object or &#39;AddOnConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**add_on_environment_variables** | [**List[AddOnEnvironmentVariable]**](AddOnEnvironmentVariable.md) | List of environment variables for the addon | [optional] 
**secret_propagations** | [**List[AddOnSecretPropagation]**](AddOnSecretPropagation.md) | List of secret propagations for the addon | [optional] 

## Example

```python
from ocm_client.models.add_on_config import AddOnConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnConfig from a JSON string
add_on_config_instance = AddOnConfig.from_json(json)
# print the JSON string representation of the object
print(AddOnConfig.to_json())

# convert the object into a dict
add_on_config_dict = add_on_config_instance.to_dict()
# create an instance of AddOnConfig from a dict
add_on_config_from_dict = AddOnConfig.from_dict(add_on_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


