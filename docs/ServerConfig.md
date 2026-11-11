# ServerConfig

Representation of a server config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;ServerConfig&#39; if this is a complete object or &#39;ServerConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**aws_shard** | [**AWSShard**](AWSShard.md) |  | [optional] 
**kubeconfig** | **str** | The kubeconfig of the server. | [optional] 
**server** | **str** | The URL of the server. | [optional] 
**topology** | [**ProvisionShardTopology**](ProvisionShardTopology.md) |  | [optional] 

## Example

```python
from ocm_client.models.server_config import ServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfig from a JSON string
server_config_instance = ServerConfig.from_json(json)
# print the JSON string representation of the object
print(ServerConfig.to_json())

# convert the object into a dict
server_config_dict = server_config_instance.to_dict()
# create an instance of ServerConfig from a dict
server_config_from_dict = ServerConfig.from_dict(server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


