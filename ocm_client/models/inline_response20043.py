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


class InlineResponse20043(object):
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
        'items': 'list[LimitedSupportReasonTemplate]',
        'page': 'int',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'items': 'items',
        'page': 'page',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, items=None, page=None, size=None, total=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20043 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items = None
        self._page = None
        self._size = None
        self._total = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def items(self):
        """Gets the items of this InlineResponse20043.  # noqa: E501

        Retrieved list of template.  # noqa: E501

        :return: The items of this InlineResponse20043.  # noqa: E501
        :rtype: list[LimitedSupportReasonTemplate]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InlineResponse20043.

        Retrieved list of template.  # noqa: E501

        :param items: The items of this InlineResponse20043.  # noqa: E501
        :type: list[LimitedSupportReasonTemplate]
        """

        self._items = items

    @property
    def page(self):
        """Gets the page of this InlineResponse20043.  # noqa: E501

        Index of the requested page, where one corresponds to the first page.  # noqa: E501

        :return: The page of this InlineResponse20043.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InlineResponse20043.

        Index of the requested page, where one corresponds to the first page.  # noqa: E501

        :param page: The page of this InlineResponse20043.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def size(self):
        """Gets the size of this InlineResponse20043.  # noqa: E501

        Number of items contained in the returned page.  # noqa: E501

        :return: The size of this InlineResponse20043.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InlineResponse20043.

        Number of items contained in the returned page.  # noqa: E501

        :param size: The size of this InlineResponse20043.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def total(self):
        """Gets the total of this InlineResponse20043.  # noqa: E501

        Total number of items of the collection.  # noqa: E501

        :return: The total of this InlineResponse20043.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse20043.

        Total number of items of the collection.  # noqa: E501

        :param total: The total of this InlineResponse20043.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, InlineResponse20043):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20043):
            return True

        return self.to_dict() != other.to_dict()
