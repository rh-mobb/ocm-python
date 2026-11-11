# Log

Log of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Log&#39; if this is a complete object or &#39;LogLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**content** | **str** | Content of the log. | [optional] 

## Example

```python
from ocm_client.models.log import Log

# TODO update the JSON string below
json = "{}"
# create an instance of Log from a JSON string
log_instance = Log.from_json(json)
# print the JSON string representation of the object
print(Log.to_json())

# convert the object into a dict
log_dict = log_instance.to_dict()
# create an instance of Log from a dict
log_from_dict = Log.from_dict(log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


