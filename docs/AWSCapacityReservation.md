# AWSCapacityReservation

AWS Capacity Reservation specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specify the target Capacity Reservation in which the EC2 instances will be launched. | [optional] 
**market_type** | [**MarketType**](MarketType.md) |  | [optional] 
**preference** | [**CapacityReservationPreference**](CapacityReservationPreference.md) |  | [optional] 

## Example

```python
from ocm_client.models.aws_capacity_reservation import AWSCapacityReservation

# TODO update the JSON string below
json = "{}"
# create an instance of AWSCapacityReservation from a JSON string
aws_capacity_reservation_instance = AWSCapacityReservation.from_json(json)
# print the JSON string representation of the object
print(AWSCapacityReservation.to_json())

# convert the object into a dict
aws_capacity_reservation_dict = aws_capacity_reservation_instance.to_dict()
# create an instance of AWSCapacityReservation from a dict
aws_capacity_reservation_from_dict = AWSCapacityReservation.from_dict(aws_capacity_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


