# FlavourNodes

Counts of different classes of nodes inside a flavour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master** | **int** | Number of master nodes of the cluster. | [optional] 

## Example

```python
from ocm_client.models.flavour_nodes import FlavourNodes

# TODO update the JSON string below
json = "{}"
# create an instance of FlavourNodes from a JSON string
flavour_nodes_instance = FlavourNodes.from_json(json)
# print the JSON string representation of the object
print(FlavourNodes.to_json())

# convert the object into a dict
flavour_nodes_dict = flavour_nodes_instance.to_dict()
# create an instance of FlavourNodes from a dict
flavour_nodes_from_dict = FlavourNodes.from_dict(flavour_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


