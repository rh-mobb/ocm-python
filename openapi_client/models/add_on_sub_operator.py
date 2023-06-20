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


class AddOnSubOperator(object):
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
        'enabled': 'bool',
        'operator_name': 'str',
        'operator_namespace': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'operator_name': 'operator_name',
        'operator_namespace': 'operator_namespace'
    }

    def __init__(self, enabled=None, operator_name=None, operator_namespace=None, local_vars_configuration=None):  # noqa: E501
        """AddOnSubOperator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._operator_name = None
        self._operator_namespace = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if operator_name is not None:
            self.operator_name = operator_name
        if operator_namespace is not None:
            self.operator_namespace = operator_namespace

    @property
    def enabled(self):
        """Gets the enabled of this AddOnSubOperator.  # noqa: E501

        Indicates if the sub operator is enabled for the add-on  # noqa: E501

        :return: The enabled of this AddOnSubOperator.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AddOnSubOperator.

        Indicates if the sub operator is enabled for the add-on  # noqa: E501

        :param enabled: The enabled of this AddOnSubOperator.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def operator_name(self):
        """Gets the operator_name of this AddOnSubOperator.  # noqa: E501

        Name of the add-on sub operator  # noqa: E501

        :return: The operator_name of this AddOnSubOperator.  # noqa: E501
        :rtype: str
        """
        return self._operator_name

    @operator_name.setter
    def operator_name(self, operator_name):
        """Sets the operator_name of this AddOnSubOperator.

        Name of the add-on sub operator  # noqa: E501

        :param operator_name: The operator_name of this AddOnSubOperator.  # noqa: E501
        :type: str
        """

        self._operator_name = operator_name

    @property
    def operator_namespace(self):
        """Gets the operator_namespace of this AddOnSubOperator.  # noqa: E501

        Namespace of the add-on sub operator  # noqa: E501

        :return: The operator_namespace of this AddOnSubOperator.  # noqa: E501
        :rtype: str
        """
        return self._operator_namespace

    @operator_namespace.setter
    def operator_namespace(self, operator_namespace):
        """Sets the operator_namespace of this AddOnSubOperator.

        Namespace of the add-on sub operator  # noqa: E501

        :param operator_namespace: The operator_namespace of this AddOnSubOperator.  # noqa: E501
        :type: str
        """

        self._operator_namespace = operator_namespace

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
        if not isinstance(other, AddOnSubOperator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddOnSubOperator):
            return True

        return self.to_dict() != other.to_dict()
