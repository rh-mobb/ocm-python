# Hypershift

Hypershift configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Boolean flag indicating if the cluster should be creating using _Hypershift_.  By default this is &#x60;false&#x60;.  To enable it the cluster needs to be ROSA cluster and the organization of the user needs to have the &#x60;hypershift&#x60; capability enabled. | [optional] 

## Example

```python
from ocm_client.models.hypershift import Hypershift

# TODO update the JSON string below
json = "{}"
# create an instance of Hypershift from a JSON string
hypershift_instance = Hypershift.from_json(json)
# print the JSON string representation of the object
print(Hypershift.to_json())

# convert the object into a dict
hypershift_dict = hypershift_instance.to_dict()
# create an instance of Hypershift from a dict
hypershift_from_dict = Hypershift.from_dict(hypershift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


