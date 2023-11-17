# InlineResponse2005

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account_id** | **str** | The AWS Account Id for the STS Account Roles | [optional] 
**items** | [**list[AWSSTSAccountRole]**](AWSSTSAccountRole.md) | Retrieved list of STS Account Roles | [optional] 
**page** | **int** | Index of the returned page, where one corresponds to the first page. As this collection doesn&#39;t support paging the result will always be &#x60;1&#x60;. | [optional] 
**size** | **int** | Number of items that will be contained in the returned page. As this collection doesn&#39;t support paging or searching the result will always be the total number of be the total number of STS account roles. | [optional] 
**total** | **int** | Total number of items of the collection that match the search criteria, regardless of the size of the page. As this collection doesn&#39;t support paging or searching the result will always be the total number of STS account roles | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


