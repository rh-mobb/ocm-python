# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ocm_client.configuration import Configuration


class AutoscalerResourceLimitsGPULimit(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'range': 'ResourceRange',
        'type': 'str'
    }

    attribute_map = {
        'range': 'range',
        'type': 'type'
    }

    def __init__(self, range=None, type=None, local_vars_configuration=None):  # noqa: E501
        """AutoscalerResourceLimitsGPULimit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._range = None
        self._type = None
        self.discriminator = None

        if range is not None:
            self.range = range
        if type is not None:
            self.type = type

    @property
    def range(self):
        """Gets the range of this AutoscalerResourceLimitsGPULimit.  # noqa: E501


        :return: The range of this AutoscalerResourceLimitsGPULimit.  # noqa: E501
        :rtype: ResourceRange
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this AutoscalerResourceLimitsGPULimit.


        :param range: The range of this AutoscalerResourceLimitsGPULimit.  # noqa: E501
        :type: ResourceRange
        """

        self._range = range

    @property
    def type(self):
        """Gets the type of this AutoscalerResourceLimitsGPULimit.  # noqa: E501

        The type of GPU to associate with the minimum and maximum limits. This value is used by the Cluster Autoscaler to identify Nodes that will have GPU capacity by searching for it as a label value on the Node objects. For example, Nodes that carry the label key `cluster-api/accelerator` with the label value being the same as the Type field will be counted towards the resource limits by the Cluster Autoscaler.  # noqa: E501

        :return: The type of this AutoscalerResourceLimitsGPULimit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoscalerResourceLimitsGPULimit.

        The type of GPU to associate with the minimum and maximum limits. This value is used by the Cluster Autoscaler to identify Nodes that will have GPU capacity by searching for it as a label value on the Node objects. For example, Nodes that carry the label key `cluster-api/accelerator` with the label value being the same as the Type field will be counted towards the resource limits by the Cluster Autoscaler.  # noqa: E501

        :param type: The type of this AutoscalerResourceLimitsGPULimit.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoscalerResourceLimitsGPULimit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoscalerResourceLimitsGPULimit):
            return True

        return self.to_dict() != other.to_dict()
