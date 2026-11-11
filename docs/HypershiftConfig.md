# HypershiftConfig

Hypershift configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hcp_namespace** | **str** | Contains the name of the hcp namespace for this Hypershift cluster. Empty for non Hypershift clusters. | [optional] 
**enabled** | **bool** | Boolean flag indicating if the cluster should be creating using _Hypershift_.  By default this is &#x60;false&#x60;.  To enable it the cluster needs to be ROSA cluster and the organization of the user needs to have the &#x60;hypershift&#x60; capability enabled. | [optional] 
**management_cluster** | **str** | Contains the name of the current management cluster for this Hypershift cluster. Empty for non Hypershift clusters. | [optional] 

## Example

```python
from ocm_client.models.hypershift_config import HypershiftConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HypershiftConfig from a JSON string
hypershift_config_instance = HypershiftConfig.from_json(json)
# print the JSON string representation of the object
print(HypershiftConfig.to_json())

# convert the object into a dict
hypershift_config_dict = hypershift_config_instance.to_dict()
# create an instance of HypershiftConfig from a dict
hypershift_config_from_dict = HypershiftConfig.from_dict(hypershift_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


