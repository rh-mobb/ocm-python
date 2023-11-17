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


class AutoscalerScaleDownConfig(object):
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
        'delay_after_add': 'str',
        'delay_after_delete': 'str',
        'delay_after_failure': 'str',
        'enabled': 'bool',
        'unneeded_time': 'str',
        'utilization_threshold': 'str'
    }

    attribute_map = {
        'delay_after_add': 'delay_after_add',
        'delay_after_delete': 'delay_after_delete',
        'delay_after_failure': 'delay_after_failure',
        'enabled': 'enabled',
        'unneeded_time': 'unneeded_time',
        'utilization_threshold': 'utilization_threshold'
    }

    def __init__(self, delay_after_add=None, delay_after_delete=None, delay_after_failure=None, enabled=None, unneeded_time=None, utilization_threshold=None, local_vars_configuration=None):  # noqa: E501
        """AutoscalerScaleDownConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delay_after_add = None
        self._delay_after_delete = None
        self._delay_after_failure = None
        self._enabled = None
        self._unneeded_time = None
        self._utilization_threshold = None
        self.discriminator = None

        if delay_after_add is not None:
            self.delay_after_add = delay_after_add
        if delay_after_delete is not None:
            self.delay_after_delete = delay_after_delete
        if delay_after_failure is not None:
            self.delay_after_failure = delay_after_failure
        if enabled is not None:
            self.enabled = enabled
        if unneeded_time is not None:
            self.unneeded_time = unneeded_time
        if utilization_threshold is not None:
            self.utilization_threshold = utilization_threshold

    @property
    def delay_after_add(self):
        """Gets the delay_after_add of this AutoscalerScaleDownConfig.  # noqa: E501

        How long after scale up that scale down evaluation resumes.  # noqa: E501

        :return: The delay_after_add of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: str
        """
        return self._delay_after_add

    @delay_after_add.setter
    def delay_after_add(self, delay_after_add):
        """Sets the delay_after_add of this AutoscalerScaleDownConfig.

        How long after scale up that scale down evaluation resumes.  # noqa: E501

        :param delay_after_add: The delay_after_add of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: str
        """

        self._delay_after_add = delay_after_add

    @property
    def delay_after_delete(self):
        """Gets the delay_after_delete of this AutoscalerScaleDownConfig.  # noqa: E501

        How long after node deletion that scale down evaluation resumes, defaults to scan-interval.  # noqa: E501

        :return: The delay_after_delete of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: str
        """
        return self._delay_after_delete

    @delay_after_delete.setter
    def delay_after_delete(self, delay_after_delete):
        """Sets the delay_after_delete of this AutoscalerScaleDownConfig.

        How long after node deletion that scale down evaluation resumes, defaults to scan-interval.  # noqa: E501

        :param delay_after_delete: The delay_after_delete of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: str
        """

        self._delay_after_delete = delay_after_delete

    @property
    def delay_after_failure(self):
        """Gets the delay_after_failure of this AutoscalerScaleDownConfig.  # noqa: E501

        How long after scale down failure that scale down evaluation resumes.  # noqa: E501

        :return: The delay_after_failure of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: str
        """
        return self._delay_after_failure

    @delay_after_failure.setter
    def delay_after_failure(self, delay_after_failure):
        """Sets the delay_after_failure of this AutoscalerScaleDownConfig.

        How long after scale down failure that scale down evaluation resumes.  # noqa: E501

        :param delay_after_failure: The delay_after_failure of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: str
        """

        self._delay_after_failure = delay_after_failure

    @property
    def enabled(self):
        """Gets the enabled of this AutoscalerScaleDownConfig.  # noqa: E501

        Should cluster-autoscaler scale down the cluster.  # noqa: E501

        :return: The enabled of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AutoscalerScaleDownConfig.

        Should cluster-autoscaler scale down the cluster.  # noqa: E501

        :param enabled: The enabled of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def unneeded_time(self):
        """Gets the unneeded_time of this AutoscalerScaleDownConfig.  # noqa: E501

        How long a node should be unneeded before it is eligible for scale down.  # noqa: E501

        :return: The unneeded_time of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: str
        """
        return self._unneeded_time

    @unneeded_time.setter
    def unneeded_time(self, unneeded_time):
        """Sets the unneeded_time of this AutoscalerScaleDownConfig.

        How long a node should be unneeded before it is eligible for scale down.  # noqa: E501

        :param unneeded_time: The unneeded_time of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: str
        """

        self._unneeded_time = unneeded_time

    @property
    def utilization_threshold(self):
        """Gets the utilization_threshold of this AutoscalerScaleDownConfig.  # noqa: E501

        Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.  # noqa: E501

        :return: The utilization_threshold of this AutoscalerScaleDownConfig.  # noqa: E501
        :rtype: str
        """
        return self._utilization_threshold

    @utilization_threshold.setter
    def utilization_threshold(self, utilization_threshold):
        """Sets the utilization_threshold of this AutoscalerScaleDownConfig.

        Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.  # noqa: E501

        :param utilization_threshold: The utilization_threshold of this AutoscalerScaleDownConfig.  # noqa: E501
        :type: str
        """

        self._utilization_threshold = utilization_threshold

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
        if not isinstance(other, AutoscalerScaleDownConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoscalerScaleDownConfig):
            return True

        return self.to_dict() != other.to_dict()