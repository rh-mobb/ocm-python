# ComponentRoute

Representation of a Component Route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ComponentRoute&#39; if this is a complete object or &#39;ComponentRouteLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**hostname** | **str** | Hostname of the route. | [optional] 
**tls_secret_ref** | **str** | TLS Secret reference of the route. | [optional] 

## Example

```python
from ocm_client.models.component_route import ComponentRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentRoute from a JSON string
component_route_instance = ComponentRoute.from_json(json)
# print the JSON string representation of the object
print(ComponentRoute.to_json())

# convert the object into a dict
component_route_dict = component_route_instance.to_dict()
# create an instance of ComponentRoute from a dict
component_route_from_dict = ComponentRoute.from_dict(component_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


