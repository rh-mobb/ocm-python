# VersionGateAgreement

VersionGateAgreement represents a version gate that the user agreed to for a specific cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Indicates the type of this object. Will be &#39;VersionGateAgreement&#39; if this is a complete object or &#39;VersionGateAgreementLink&#39; if it is just a link. | [optional] 
**id** | **str** | Unique identifier of the object. | [optional] 
**href** | **str** | Self link. | [optional] 
**agreed_timestamp** | **datetime** | The time the user agreed to the version gate | [optional] 
**version_gate** | [**VersionGate**](VersionGate.md) |  | [optional] 

## Example

```python
from ocm_client.models.version_gate_agreement import VersionGateAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of VersionGateAgreement from a JSON string
version_gate_agreement_instance = VersionGateAgreement.from_json(json)
# print the JSON string representation of the object
print(VersionGateAgreement.to_json())

# convert the object into a dict
version_gate_agreement_dict = version_gate_agreement_instance.to_dict()
# create an instance of VersionGateAgreement from a dict
version_gate_agreement_from_dict = VersionGateAgreement.from_dict(version_gate_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


