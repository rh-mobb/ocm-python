# Ingress

Representation of an ingress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;Ingress&#39; if this is a complete object or &#39;IngressLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**dns_name** | **str** | DNS Name of the ingress. | [optional] 
**cluster_routes_hostname** | **str** | Cluster routes hostname. | [optional] 
**cluster_routes_tls_secret_ref** | **str** | Cluster routes TLS Secret reference. | [optional] 
**component_routes** | [**Dict[str, ComponentRoute]**](ComponentRoute.md) | Component Routes settings. | [optional] 
**default** | **bool** | Indicates if this is the default ingress. | [optional] 
**excluded_namespace_selectors** | [**List[NamespaceSelector]**](NamespaceSelector.md) | A set of excluded exclude namespaces via labels for ingress. | [optional] 
**excluded_namespaces** | **List[str]** | A set of excluded namespaces for the ingress. | [optional] 
**listening** | [**ListeningMethod**](ListeningMethod.md) |  | [optional] 
**load_balancer_type** | [**LoadBalancerFlavor**](LoadBalancerFlavor.md) |  | [optional] 
**route_namespace_ownership_policy** | [**NamespaceOwnershipPolicy**](NamespaceOwnershipPolicy.md) |  | [optional] 
**route_selectors** | **Dict[str, str]** | A set of labels for the ingress.  | [optional] 
**route_wildcard_policy** | [**WildcardPolicy**](WildcardPolicy.md) |  | [optional] 

## Example

```python
from ocm_client.models.ingress import Ingress

# TODO update the JSON string below
json = "{}"
# create an instance of Ingress from a JSON string
ingress_instance = Ingress.from_json(json)
# print the JSON string representation of the object
print(Ingress.to_json())

# convert the object into a dict
ingress_dict = ingress_instance.to_dict()
# create an instance of Ingress from a dict
ingress_from_dict = Ingress.from_dict(ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


