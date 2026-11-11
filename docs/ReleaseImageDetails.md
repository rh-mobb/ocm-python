# ReleaseImageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_upgrades** | **List[str]** | AvailableUpgrades is the list of versions this version can be upgraded to. | [optional] 
**release_image** | **str** | ReleaseImage contains the URI of Openshift release image. | [optional] 

## Example

```python
from ocm_client.models.release_image_details import ReleaseImageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseImageDetails from a JSON string
release_image_details_instance = ReleaseImageDetails.from_json(json)
# print the JSON string representation of the object
print(ReleaseImageDetails.to_json())

# convert the object into a dict
release_image_details_dict = release_image_details_instance.to_dict()
# create an instance of ReleaseImageDetails from a dict
release_image_details_from_dict = ReleaseImageDetails.from_dict(release_image_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


