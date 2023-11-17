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


class AMIOverride(object):
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
        'ami': 'str',
        'product': 'Product',
        'region': 'CloudRegion'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'ami': 'ami',
        'product': 'product',
        'region': 'region'
    }

    def __init__(self, kind=None, id=None, href=None, ami=None, product=None, region=None, local_vars_configuration=None):  # noqa: E501
        """AMIOverride - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._ami = None
        self._product = None
        self._region = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if ami is not None:
            self.ami = ami
        if product is not None:
            self.product = product
        if region is not None:
            self.region = region

    @property
    def kind(self):
        """Gets the kind of this AMIOverride.  # noqa: E501

        Indicates the type of this object. Will be 'AMIOverride' if this is a complete object or 'AMIOverrideLink' if it is just a link.  # noqa: E501

        :return: The kind of this AMIOverride.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this AMIOverride.

        Indicates the type of this object. Will be 'AMIOverride' if this is a complete object or 'AMIOverrideLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this AMIOverride.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this AMIOverride.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this AMIOverride.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AMIOverride.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this AMIOverride.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this AMIOverride.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this AMIOverride.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AMIOverride.

        Self link.  # noqa: E501

        :param href: The href of this AMIOverride.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def ami(self):
        """Gets the ami of this AMIOverride.  # noqa: E501

        AMI is the id of the Amazon Machine Image.  # noqa: E501

        :return: The ami of this AMIOverride.  # noqa: E501
        :rtype: str
        """
        return self._ami

    @ami.setter
    def ami(self, ami):
        """Sets the ami of this AMIOverride.

        AMI is the id of the Amazon Machine Image.  # noqa: E501

        :param ami: The ami of this AMIOverride.  # noqa: E501
        :type: str
        """

        self._ami = ami

    @property
    def product(self):
        """Gets the product of this AMIOverride.  # noqa: E501


        :return: The product of this AMIOverride.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AMIOverride.


        :param product: The product of this AMIOverride.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def region(self):
        """Gets the region of this AMIOverride.  # noqa: E501


        :return: The region of this AMIOverride.  # noqa: E501
        :rtype: CloudRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AMIOverride.


        :param region: The region of this AMIOverride.  # noqa: E501
        :type: CloudRegion
        """

        self._region = region

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
        if not isinstance(other, AMIOverride):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AMIOverride):
            return True

        return self.to_dict() != other.to_dict()