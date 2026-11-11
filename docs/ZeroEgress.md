# ZeroEgress

Zero egress configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if zero egress is enabled for this cluster. | [optional] 
**no_proxy_default_domains** | **List[str]** | List of default no-proxy domains automatically added to the cluster&#39;s no-proxy configuration when zero egress is enabled. | [optional] 

## Example

```python
from ocm_client.models.zero_egress import ZeroEgress

# TODO update the JSON string below
json = "{}"
# create an instance of ZeroEgress from a JSON string
zero_egress_instance = ZeroEgress.from_json(json)
# print the JSON string representation of the object
print(ZeroEgress.to_json())

# convert the object into a dict
zero_egress_dict = zero_egress_instance.to_dict()
# create an instance of ZeroEgress from a dict
zero_egress_from_dict = ZeroEgress.from_dict(zero_egress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


