# ReleaseImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arm64** | [**ReleaseImageDetails**](ReleaseImageDetails.md) |  | [optional] 
**multi** | [**ReleaseImageDetails**](ReleaseImageDetails.md) |  | [optional] 

## Example

```python
from ocm_client.models.release_images import ReleaseImages

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseImages from a JSON string
release_images_instance = ReleaseImages.from_json(json)
# print the JSON string representation of the object
print(ReleaseImages.to_json())

# convert the object into a dict
release_images_dict = release_images_instance.to_dict()
# create an instance of ReleaseImages from a dict
release_images_from_dict = ReleaseImages.from_dict(release_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


