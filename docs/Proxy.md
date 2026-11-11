# Proxy

Proxy configuration of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_proxy** | **str** | HTTPProxy is the URL of the proxy for HTTP requests. | [optional] 
**https_proxy** | **str** | HTTPSProxy is the URL of the proxy for HTTPS requests. | [optional] 
**no_proxy** | **str** | NoProxy is a comma-separated list of domains and CIDRs for which  the proxy should not be used | [optional] 

## Example

```python
from ocm_client.models.proxy import Proxy

# TODO update the JSON string below
json = "{}"
# create an instance of Proxy from a JSON string
proxy_instance = Proxy.from_json(json)
# print the JSON string representation of the object
print(Proxy.to_json())

# convert the object into a dict
proxy_dict = proxy_instance.to_dict()
# create an instance of Proxy from a dict
proxy_from_dict = Proxy.from_dict(proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


