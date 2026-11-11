# ClientComponent

The reference of a component that will consume the client configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the component. | [optional] 
**namespace** | **str** | The namespace of the component. | [optional] 

## Example

```python
from ocm_client.models.client_component import ClientComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ClientComponent from a JSON string
client_component_instance = ClientComponent.from_json(json)
# print the JSON string representation of the object
print(ClientComponent.to_json())

# convert the object into a dict
client_component_dict = client_component_instance.to_dict()
# create an instance of ClientComponent from a dict
client_component_from_dict = ClientComponent.from_dict(client_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


