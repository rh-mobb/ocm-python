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


class NodePool(object):
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
        'aws_node_pool': 'AWSNodePool',
        'auto_repair': 'bool',
        'autoscaling': 'NodePoolAutoscaling',
        'availability_zone': 'str',
        'labels': 'dict(str, str)',
        'replicas': 'int',
        'status': 'NodePoolStatus',
        'subnet': 'str',
        'taints': 'list[Taint]',
        'tuning_configs': 'list[str]',
        'version': 'Version'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'aws_node_pool': 'aws_node_pool',
        'auto_repair': 'auto_repair',
        'autoscaling': 'autoscaling',
        'availability_zone': 'availability_zone',
        'labels': 'labels',
        'replicas': 'replicas',
        'status': 'status',
        'subnet': 'subnet',
        'taints': 'taints',
        'tuning_configs': 'tuning_configs',
        'version': 'version'
    }

    def __init__(self, kind=None, id=None, href=None, aws_node_pool=None, auto_repair=None, autoscaling=None, availability_zone=None, labels=None, replicas=None, status=None, subnet=None, taints=None, tuning_configs=None, version=None, local_vars_configuration=None):  # noqa: E501
        """NodePool - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._aws_node_pool = None
        self._auto_repair = None
        self._autoscaling = None
        self._availability_zone = None
        self._labels = None
        self._replicas = None
        self._status = None
        self._subnet = None
        self._taints = None
        self._tuning_configs = None
        self._version = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if aws_node_pool is not None:
            self.aws_node_pool = aws_node_pool
        if auto_repair is not None:
            self.auto_repair = auto_repair
        if autoscaling is not None:
            self.autoscaling = autoscaling
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if labels is not None:
            self.labels = labels
        if replicas is not None:
            self.replicas = replicas
        if status is not None:
            self.status = status
        if subnet is not None:
            self.subnet = subnet
        if taints is not None:
            self.taints = taints
        if tuning_configs is not None:
            self.tuning_configs = tuning_configs
        if version is not None:
            self.version = version

    @property
    def kind(self):
        """Gets the kind of this NodePool.  # noqa: E501

        Indicates the type of this object. Will be 'NodePool' if this is a complete object or 'NodePoolLink' if it is just a link.  # noqa: E501

        :return: The kind of this NodePool.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NodePool.

        Indicates the type of this object. Will be 'NodePool' if this is a complete object or 'NodePoolLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this NodePool.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this NodePool.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this NodePool.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePool.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this NodePool.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this NodePool.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this NodePool.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this NodePool.

        Self link.  # noqa: E501

        :param href: The href of this NodePool.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def aws_node_pool(self):
        """Gets the aws_node_pool of this NodePool.  # noqa: E501


        :return: The aws_node_pool of this NodePool.  # noqa: E501
        :rtype: AWSNodePool
        """
        return self._aws_node_pool

    @aws_node_pool.setter
    def aws_node_pool(self, aws_node_pool):
        """Sets the aws_node_pool of this NodePool.


        :param aws_node_pool: The aws_node_pool of this NodePool.  # noqa: E501
        :type: AWSNodePool
        """

        self._aws_node_pool = aws_node_pool

    @property
    def auto_repair(self):
        """Gets the auto_repair of this NodePool.  # noqa: E501

        Specifies whether health checks should be enabled for machines in the NodePool.  # noqa: E501

        :return: The auto_repair of this NodePool.  # noqa: E501
        :rtype: bool
        """
        return self._auto_repair

    @auto_repair.setter
    def auto_repair(self, auto_repair):
        """Sets the auto_repair of this NodePool.

        Specifies whether health checks should be enabled for machines in the NodePool.  # noqa: E501

        :param auto_repair: The auto_repair of this NodePool.  # noqa: E501
        :type: bool
        """

        self._auto_repair = auto_repair

    @property
    def autoscaling(self):
        """Gets the autoscaling of this NodePool.  # noqa: E501


        :return: The autoscaling of this NodePool.  # noqa: E501
        :rtype: NodePoolAutoscaling
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this NodePool.


        :param autoscaling: The autoscaling of this NodePool.  # noqa: E501
        :type: NodePoolAutoscaling
        """

        self._autoscaling = autoscaling

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NodePool.  # noqa: E501

        The availability zone upon which the node is created.  # noqa: E501

        :return: The availability_zone of this NodePool.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NodePool.

        The availability zone upon which the node is created.  # noqa: E501

        :param availability_zone: The availability_zone of this NodePool.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def labels(self):
        """Gets the labels of this NodePool.  # noqa: E501

        The labels set on the Nodes created.  # noqa: E501

        :return: The labels of this NodePool.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NodePool.

        The labels set on the Nodes created.  # noqa: E501

        :param labels: The labels of this NodePool.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def replicas(self):
        """Gets the replicas of this NodePool.  # noqa: E501

        The number of Machines (and Nodes) to create. Replicas and autoscaling cannot be used together.  # noqa: E501

        :return: The replicas of this NodePool.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this NodePool.

        The number of Machines (and Nodes) to create. Replicas and autoscaling cannot be used together.  # noqa: E501

        :param replicas: The replicas of this NodePool.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def status(self):
        """Gets the status of this NodePool.  # noqa: E501


        :return: The status of this NodePool.  # noqa: E501
        :rtype: NodePoolStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodePool.


        :param status: The status of this NodePool.  # noqa: E501
        :type: NodePoolStatus
        """

        self._status = status

    @property
    def subnet(self):
        """Gets the subnet of this NodePool.  # noqa: E501

        The subnet upon which the nodes are created.  # noqa: E501

        :return: The subnet of this NodePool.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this NodePool.

        The subnet upon which the nodes are created.  # noqa: E501

        :param subnet: The subnet of this NodePool.  # noqa: E501
        :type: str
        """

        self._subnet = subnet

    @property
    def taints(self):
        """Gets the taints of this NodePool.  # noqa: E501

        The taints set on the Nodes created.  # noqa: E501

        :return: The taints of this NodePool.  # noqa: E501
        :rtype: list[Taint]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        """Sets the taints of this NodePool.

        The taints set on the Nodes created.  # noqa: E501

        :param taints: The taints of this NodePool.  # noqa: E501
        :type: list[Taint]
        """

        self._taints = taints

    @property
    def tuning_configs(self):
        """Gets the tuning_configs of this NodePool.  # noqa: E501

        The names of the tuning configs for this node pool.  # noqa: E501

        :return: The tuning_configs of this NodePool.  # noqa: E501
        :rtype: list[str]
        """
        return self._tuning_configs

    @tuning_configs.setter
    def tuning_configs(self, tuning_configs):
        """Sets the tuning_configs of this NodePool.

        The names of the tuning configs for this node pool.  # noqa: E501

        :param tuning_configs: The tuning_configs of this NodePool.  # noqa: E501
        :type: list[str]
        """

        self._tuning_configs = tuning_configs

    @property
    def version(self):
        """Gets the version of this NodePool.  # noqa: E501


        :return: The version of this NodePool.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodePool.


        :param version: The version of this NodePool.  # noqa: E501
        :type: Version
        """

        self._version = version

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
        if not isinstance(other, NodePool):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodePool):
            return True

        return self.to_dict() != other.to_dict()
