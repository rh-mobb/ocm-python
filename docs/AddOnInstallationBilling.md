# AddOnInstallationBilling

Representation of an add-on installation billing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;AddOnInstallationBilling&#39; if this is a complete object or &#39;AddOnInstallationBillingLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**billing_marketplace_account** | **str** | Account ID for billing market place | [optional] 
**billing_model** | [**BillingModel**](BillingModel.md) |  | [optional] 

## Example

```python
from ocm_client.models.add_on_installation_billing import AddOnInstallationBilling

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnInstallationBilling from a JSON string
add_on_installation_billing_instance = AddOnInstallationBilling.from_json(json)
# print the JSON string representation of the object
print(AddOnInstallationBilling.to_json())

# convert the object into a dict
add_on_installation_billing_dict = add_on_installation_billing_instance.to_dict()
# create an instance of AddOnInstallationBilling from a dict
add_on_installation_billing_from_dict = AddOnInstallationBilling.from_dict(add_on_installation_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


