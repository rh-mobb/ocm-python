# CloudVPC

Description of a cloud provider virtual private cloud.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_security_groups** | [**list[SecurityGroup]**](SecurityGroup.md) | List of AWS security groups with details. | [optional] 
**aws_subnets** | [**list[Subnetwork]**](Subnetwork.md) | List of AWS subnetworks with details. | [optional] 
**cidr_block** | **str** | CIDR block of the virtual private cloud. | [optional] 
**id** | **str** | ID of virtual private cloud. | [optional] 
**name** | **str** | Name of virtual private cloud according to its &#x60;Name&#x60; tag on AWS. | [optional] 
**red_hat_managed** | **bool** | If the resource is RH managed. | [optional] 
**subnets** | **list[str]** | List of subnets used by the virtual private cloud. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


