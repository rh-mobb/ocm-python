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


class Network(object):
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
        'host_prefix': 'int',
        'machine_cidr': 'str',
        'pod_cidr': 'str',
        'service_cidr': 'str',
        'type': 'str'
    }

    attribute_map = {
        'host_prefix': 'host_prefix',
        'machine_cidr': 'machine_cidr',
        'pod_cidr': 'pod_cidr',
        'service_cidr': 'service_cidr',
        'type': 'type'
    }

    def __init__(self, host_prefix=None, machine_cidr=None, pod_cidr=None, service_cidr=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Network - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host_prefix = None
        self._machine_cidr = None
        self._pod_cidr = None
        self._service_cidr = None
        self._type = None
        self.discriminator = None

        if host_prefix is not None:
            self.host_prefix = host_prefix
        if machine_cidr is not None:
            self.machine_cidr = machine_cidr
        if pod_cidr is not None:
            self.pod_cidr = pod_cidr
        if service_cidr is not None:
            self.service_cidr = service_cidr
        if type is not None:
            self.type = type

    @property
    def host_prefix(self):
        """Gets the host_prefix of this Network.  # noqa: E501

        Network host prefix which is defaulted to `23` if not specified.  # noqa: E501

        :return: The host_prefix of this Network.  # noqa: E501
        :rtype: int
        """
        return self._host_prefix

    @host_prefix.setter
    def host_prefix(self, host_prefix):
        """Sets the host_prefix of this Network.

        Network host prefix which is defaulted to `23` if not specified.  # noqa: E501

        :param host_prefix: The host_prefix of this Network.  # noqa: E501
        :type: int
        """

        self._host_prefix = host_prefix

    @property
    def machine_cidr(self):
        """Gets the machine_cidr of this Network.  # noqa: E501

        IP address block from which to assign machine IP addresses, for example `10.0.0.0/16`.  # noqa: E501

        :return: The machine_cidr of this Network.  # noqa: E501
        :rtype: str
        """
        return self._machine_cidr

    @machine_cidr.setter
    def machine_cidr(self, machine_cidr):
        """Sets the machine_cidr of this Network.

        IP address block from which to assign machine IP addresses, for example `10.0.0.0/16`.  # noqa: E501

        :param machine_cidr: The machine_cidr of this Network.  # noqa: E501
        :type: str
        """

        self._machine_cidr = machine_cidr

    @property
    def pod_cidr(self):
        """Gets the pod_cidr of this Network.  # noqa: E501

        IP address block from which to assign pod IP addresses, for example `10.128.0.0/14`.  # noqa: E501

        :return: The pod_cidr of this Network.  # noqa: E501
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr):
        """Sets the pod_cidr of this Network.

        IP address block from which to assign pod IP addresses, for example `10.128.0.0/14`.  # noqa: E501

        :param pod_cidr: The pod_cidr of this Network.  # noqa: E501
        :type: str
        """

        self._pod_cidr = pod_cidr

    @property
    def service_cidr(self):
        """Gets the service_cidr of this Network.  # noqa: E501

        IP address block from which to assign service IP addresses, for example `172.30.0.0/16`.  # noqa: E501

        :return: The service_cidr of this Network.  # noqa: E501
        :rtype: str
        """
        return self._service_cidr

    @service_cidr.setter
    def service_cidr(self, service_cidr):
        """Sets the service_cidr of this Network.

        IP address block from which to assign service IP addresses, for example `172.30.0.0/16`.  # noqa: E501

        :param service_cidr: The service_cidr of this Network.  # noqa: E501
        :type: str
        """

        self._service_cidr = service_cidr

    @property
    def type(self):
        """Gets the type of this Network.  # noqa: E501

        The main controller responsible for rendering the core networking components.  # noqa: E501

        :return: The type of this Network.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Network.

        The main controller responsible for rendering the core networking components.  # noqa: E501

        :param type: The type of this Network.  # noqa: E501
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
        if not isinstance(other, Network):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Network):
            return True

        return self.to_dict() != other.to_dict()
