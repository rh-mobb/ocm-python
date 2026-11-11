# AddOnSecretPropagation

Representation of an addon secret propagation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the secret propagation | [optional] 
**destination_secret** | **str** | DestinationSecret is location of the secret to be added | [optional] 
**enabled** | **bool** | Indicates is this secret propagation is enabled for the addon | [optional] 
**source_secret** | **str** | SourceSecret is location of the source secret | [optional] 

## Example

```python
from ocm_client.models.add_on_secret_propagation import AddOnSecretPropagation

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnSecretPropagation from a JSON string
add_on_secret_propagation_instance = AddOnSecretPropagation.from_json(json)
# print the JSON string representation of the object
print(AddOnSecretPropagation.to_json())

# convert the object into a dict
add_on_secret_propagation_dict = add_on_secret_propagation_instance.to_dict()
# create an instance of AddOnSecretPropagation from a dict
add_on_secret_propagation_from_dict = AddOnSecretPropagation.from_dict(add_on_secret_propagation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


