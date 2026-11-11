# AddOnInstallation

Representation of an add-on installation in a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnInstallation&#39; if this is a complete object or &#39;AddOnInstallationLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**addon** | [**AddOn**](AddOn.md) |  | [optional] 
**addon_version** | [**AddOnVersion**](AddOnVersion.md) |  | [optional] 
**billing** | [**AddOnInstallationBilling**](AddOnInstallationBilling.md) |  | [optional] 
**creation_timestamp** | **datetime** | Date and time when the add-on was initially installed in the cluster. | [optional] 
**operator_version** | **str** | Version of the operator installed by the add-on. | [optional] 
**parameters** | [**List[AddOnInstallationParameter]**](AddOnInstallationParameter.md) | List of add-on parameters for this add-on installation. | [optional] 
**state** | [**AddOnInstallationState**](AddOnInstallationState.md) |  | [optional] 
**state_description** | **str** | Reason for the current State. | [optional] 
**updated_timestamp** | **datetime** | Date and time when the add-on installation information was last updated. | [optional] 

## Example

```python
from ocm_client.models.add_on_installation import AddOnInstallation

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnInstallation from a JSON string
add_on_installation_instance = AddOnInstallation.from_json(json)
# print the JSON string representation of the object
print(AddOnInstallation.to_json())

# convert the object into a dict
add_on_installation_dict = add_on_installation_instance.to_dict()
# create an instance of AddOnInstallation from a dict
add_on_installation_from_dict = AddOnInstallation.from_dict(add_on_installation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


