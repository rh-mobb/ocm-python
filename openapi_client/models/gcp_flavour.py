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


class GCPFlavour(object):
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
        'compute_instance_type': 'str',
        'infra_instance_type': 'str',
        'infra_volume': 'GCPVolume',
        'master_instance_type': 'str',
        'master_volume': 'GCPVolume',
        'worker_volume': 'GCPVolume'
    }

    attribute_map = {
        'compute_instance_type': 'compute_instance_type',
        'infra_instance_type': 'infra_instance_type',
        'infra_volume': 'infra_volume',
        'master_instance_type': 'master_instance_type',
        'master_volume': 'master_volume',
        'worker_volume': 'worker_volume'
    }

    def __init__(self, compute_instance_type=None, infra_instance_type=None, infra_volume=None, master_instance_type=None, master_volume=None, worker_volume=None, local_vars_configuration=None):  # noqa: E501
        """GCPFlavour - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._compute_instance_type = None
        self._infra_instance_type = None
        self._infra_volume = None
        self._master_instance_type = None
        self._master_volume = None
        self._worker_volume = None
        self.discriminator = None

        if compute_instance_type is not None:
            self.compute_instance_type = compute_instance_type
        if infra_instance_type is not None:
            self.infra_instance_type = infra_instance_type
        if infra_volume is not None:
            self.infra_volume = infra_volume
        if master_instance_type is not None:
            self.master_instance_type = master_instance_type
        if master_volume is not None:
            self.master_volume = master_volume
        if worker_volume is not None:
            self.worker_volume = worker_volume

    @property
    def compute_instance_type(self):
        """Gets the compute_instance_type of this GCPFlavour.  # noqa: E501

        GCP default instance type for the worker volume.  User can be overridden specifying in the cluster itself a type for compute node.  # noqa: E501

        :return: The compute_instance_type of this GCPFlavour.  # noqa: E501
        :rtype: str
        """
        return self._compute_instance_type

    @compute_instance_type.setter
    def compute_instance_type(self, compute_instance_type):
        """Sets the compute_instance_type of this GCPFlavour.

        GCP default instance type for the worker volume.  User can be overridden specifying in the cluster itself a type for compute node.  # noqa: E501

        :param compute_instance_type: The compute_instance_type of this GCPFlavour.  # noqa: E501
        :type: str
        """

        self._compute_instance_type = compute_instance_type

    @property
    def infra_instance_type(self):
        """Gets the infra_instance_type of this GCPFlavour.  # noqa: E501

        GCP default instance type for the infra volume.  # noqa: E501

        :return: The infra_instance_type of this GCPFlavour.  # noqa: E501
        :rtype: str
        """
        return self._infra_instance_type

    @infra_instance_type.setter
    def infra_instance_type(self, infra_instance_type):
        """Sets the infra_instance_type of this GCPFlavour.

        GCP default instance type for the infra volume.  # noqa: E501

        :param infra_instance_type: The infra_instance_type of this GCPFlavour.  # noqa: E501
        :type: str
        """

        self._infra_instance_type = infra_instance_type

    @property
    def infra_volume(self):
        """Gets the infra_volume of this GCPFlavour.  # noqa: E501


        :return: The infra_volume of this GCPFlavour.  # noqa: E501
        :rtype: GCPVolume
        """
        return self._infra_volume

    @infra_volume.setter
    def infra_volume(self, infra_volume):
        """Sets the infra_volume of this GCPFlavour.


        :param infra_volume: The infra_volume of this GCPFlavour.  # noqa: E501
        :type: GCPVolume
        """

        self._infra_volume = infra_volume

    @property
    def master_instance_type(self):
        """Gets the master_instance_type of this GCPFlavour.  # noqa: E501

        GCP default instance type for the master volume.  # noqa: E501

        :return: The master_instance_type of this GCPFlavour.  # noqa: E501
        :rtype: str
        """
        return self._master_instance_type

    @master_instance_type.setter
    def master_instance_type(self, master_instance_type):
        """Sets the master_instance_type of this GCPFlavour.

        GCP default instance type for the master volume.  # noqa: E501

        :param master_instance_type: The master_instance_type of this GCPFlavour.  # noqa: E501
        :type: str
        """

        self._master_instance_type = master_instance_type

    @property
    def master_volume(self):
        """Gets the master_volume of this GCPFlavour.  # noqa: E501


        :return: The master_volume of this GCPFlavour.  # noqa: E501
        :rtype: GCPVolume
        """
        return self._master_volume

    @master_volume.setter
    def master_volume(self, master_volume):
        """Sets the master_volume of this GCPFlavour.


        :param master_volume: The master_volume of this GCPFlavour.  # noqa: E501
        :type: GCPVolume
        """

        self._master_volume = master_volume

    @property
    def worker_volume(self):
        """Gets the worker_volume of this GCPFlavour.  # noqa: E501


        :return: The worker_volume of this GCPFlavour.  # noqa: E501
        :rtype: GCPVolume
        """
        return self._worker_volume

    @worker_volume.setter
    def worker_volume(self, worker_volume):
        """Sets the worker_volume of this GCPFlavour.


        :param worker_volume: The worker_volume of this GCPFlavour.  # noqa: E501
        :type: GCPVolume
        """

        self._worker_volume = worker_volume

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
        if not isinstance(other, GCPFlavour):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GCPFlavour):
            return True

        return self.to_dict() != other.to_dict()
