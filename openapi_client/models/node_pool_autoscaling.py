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

from openapi_client.configuration import Configuration


class NodePoolAutoscaling(object):
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
        'kind': 'str',
        'id': 'str',
        'href': 'str',
        'max_replica': 'int',
        'min_replica': 'int'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'max_replica': 'max_replica',
        'min_replica': 'min_replica'
    }

    def __init__(self, kind=None, id=None, href=None, max_replica=None, min_replica=None, local_vars_configuration=None):  # noqa: E501
        """NodePoolAutoscaling - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._max_replica = None
        self._min_replica = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if max_replica is not None:
            self.max_replica = max_replica
        if min_replica is not None:
            self.min_replica = min_replica

    @property
    def kind(self):
        """Gets the kind of this NodePoolAutoscaling.  # noqa: E501

        Indicates the type of this object. Will be 'NodePoolAutoscaling' if this is a complete object or 'NodePoolAutoscalingLink' if it is just a link.  # noqa: E501

        :return: The kind of this NodePoolAutoscaling.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NodePoolAutoscaling.

        Indicates the type of this object. Will be 'NodePoolAutoscaling' if this is a complete object or 'NodePoolAutoscalingLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this NodePoolAutoscaling.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this NodePoolAutoscaling.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this NodePoolAutoscaling.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePoolAutoscaling.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this NodePoolAutoscaling.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this NodePoolAutoscaling.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this NodePoolAutoscaling.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this NodePoolAutoscaling.

        Self link.  # noqa: E501

        :param href: The href of this NodePoolAutoscaling.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def max_replica(self):
        """Gets the max_replica of this NodePoolAutoscaling.  # noqa: E501

        The maximum number of replicas for the node pool.  # noqa: E501

        :return: The max_replica of this NodePoolAutoscaling.  # noqa: E501
        :rtype: int
        """
        return self._max_replica

    @max_replica.setter
    def max_replica(self, max_replica):
        """Sets the max_replica of this NodePoolAutoscaling.

        The maximum number of replicas for the node pool.  # noqa: E501

        :param max_replica: The max_replica of this NodePoolAutoscaling.  # noqa: E501
        :type: int
        """

        self._max_replica = max_replica

    @property
    def min_replica(self):
        """Gets the min_replica of this NodePoolAutoscaling.  # noqa: E501

        The minimum number of replicas for the node pool.  # noqa: E501

        :return: The min_replica of this NodePoolAutoscaling.  # noqa: E501
        :rtype: int
        """
        return self._min_replica

    @min_replica.setter
    def min_replica(self, min_replica):
        """Sets the min_replica of this NodePoolAutoscaling.

        The minimum number of replicas for the node pool.  # noqa: E501

        :param min_replica: The min_replica of this NodePoolAutoscaling.  # noqa: E501
        :type: int
        """

        self._min_replica = min_replica

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
        if not isinstance(other, NodePoolAutoscaling):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodePoolAutoscaling):
            return True

        return self.to_dict() != other.to_dict()
