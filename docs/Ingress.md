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
**default** | **bool** | Indicates if this is the default ingress. | [optional] 
**excluded_namespaces** | **list[str]** | A set of excluded namespaces for the ingress. | [optional] 
**listening** | [**ListeningMethod**](ListeningMethod.md) |  | [optional] 
**load_balancer_type** | [**LoadBalancerFlavor**](LoadBalancerFlavor.md) |  | [optional] 
**route_namespace_ownership_policy** | [**NamespaceOwnershipPolicy**](NamespaceOwnershipPolicy.md) |  | [optional] 
**route_selectors** | **dict(str, str)** | A set of labels for the ingress.  | [optional] 
**route_wildcard_policy** | [**WildcardPolicy**](WildcardPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


