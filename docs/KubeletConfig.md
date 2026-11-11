# KubeletConfig

OCM representation of KubeletConfig, exposing the fields of Kubernetes KubeletConfig that can be managed by users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;KubeletConfig&#39; if this is a complete object or &#39;KubeletConfigLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**name** | **str** | Allows the user to specify the name to be used to identify this KubeletConfig. Optional. A name will be generated if not provided. | [optional] 
**pod_pids_limit** | **int** | Allows the user to specify the podPidsLimit to be applied via KubeletConfig. Useful if workloads have greater PIDs limit requirements than the OCP default. | [optional] 

## Example

```python
from ocm_client.models.kubelet_config import KubeletConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KubeletConfig from a JSON string
kubelet_config_instance = KubeletConfig.from_json(json)
# print the JSON string representation of the object
print(KubeletConfig.to_json())

# convert the object into a dict
kubelet_config_dict = kubelet_config_instance.to_dict()
# create an instance of KubeletConfig from a dict
kubelet_config_from_dict = KubeletConfig.from_dict(kubelet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


