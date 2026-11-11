# Maintenance

Maintenance configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Boolean flag indicating if the cluster is set into maintenance mode. Clusters on maintenance mode are not allowed to perform any operation.  By default this is &#x60;false&#x60;.  To enable it a SREP needs to patch the value through OCM API | [optional] 

## Example

```python
from ocm_client.models.maintenance import Maintenance

# TODO update the JSON string below
json = "{}"
# create an instance of Maintenance from a JSON string
maintenance_instance = Maintenance.from_json(json)
# print the JSON string representation of the object
print(Maintenance.to_json())

# convert the object into a dict
maintenance_dict = maintenance_instance.to_dict()
# create an instance of Maintenance from a dict
maintenance_from_dict = Maintenance.from_dict(maintenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


