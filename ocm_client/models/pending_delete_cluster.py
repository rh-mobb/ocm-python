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


class PendingDeleteCluster(object):
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
        'best_effort': 'bool',
        'cluster': 'Cluster',
        'creation_timestamp': 'datetime'
    }

    attribute_map = {
        'kind': 'kind',
        'id': 'id',
        'href': 'href',
        'best_effort': 'best_effort',
        'cluster': 'cluster',
        'creation_timestamp': 'creation_timestamp'
    }

    def __init__(self, kind=None, id=None, href=None, best_effort=None, cluster=None, creation_timestamp=None, local_vars_configuration=None):  # noqa: E501
        """PendingDeleteCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._id = None
        self._href = None
        self._best_effort = None
        self._cluster = None
        self._creation_timestamp = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if best_effort is not None:
            self.best_effort = best_effort
        if cluster is not None:
            self.cluster = cluster
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp

    @property
    def kind(self):
        """Gets the kind of this PendingDeleteCluster.  # noqa: E501

        Indicates the type of this object. Will be 'PendingDeleteCluster' if this is a complete object or 'PendingDeleteClusterLink' if it is just a link.  # noqa: E501

        :return: The kind of this PendingDeleteCluster.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PendingDeleteCluster.

        Indicates the type of this object. Will be 'PendingDeleteCluster' if this is a complete object or 'PendingDeleteClusterLink' if it is just a link.  # noqa: E501

        :param kind: The kind of this PendingDeleteCluster.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def id(self):
        """Gets the id of this PendingDeleteCluster.  # noqa: E501

        Unique identifier of the object.  # noqa: E501

        :return: The id of this PendingDeleteCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PendingDeleteCluster.

        Unique identifier of the object.  # noqa: E501

        :param id: The id of this PendingDeleteCluster.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this PendingDeleteCluster.  # noqa: E501

        Self link.  # noqa: E501

        :return: The href of this PendingDeleteCluster.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PendingDeleteCluster.

        Self link.  # noqa: E501

        :param href: The href of this PendingDeleteCluster.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def best_effort(self):
        """Gets the best_effort of this PendingDeleteCluster.  # noqa: E501

        Flag indicating if the cluster deletion should be best-effort mode or not.  # noqa: E501

        :return: The best_effort of this PendingDeleteCluster.  # noqa: E501
        :rtype: bool
        """
        return self._best_effort

    @best_effort.setter
    def best_effort(self, best_effort):
        """Sets the best_effort of this PendingDeleteCluster.

        Flag indicating if the cluster deletion should be best-effort mode or not.  # noqa: E501

        :param best_effort: The best_effort of this PendingDeleteCluster.  # noqa: E501
        :type: bool
        """

        self._best_effort = best_effort

    @property
    def cluster(self):
        """Gets the cluster of this PendingDeleteCluster.  # noqa: E501


        :return: The cluster of this PendingDeleteCluster.  # noqa: E501
        :rtype: Cluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this PendingDeleteCluster.


        :param cluster: The cluster of this PendingDeleteCluster.  # noqa: E501
        :type: Cluster
        """

        self._cluster = cluster

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this PendingDeleteCluster.  # noqa: E501

        Date and time when the cluster was initially created, using the format defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).  # noqa: E501

        :return: The creation_timestamp of this PendingDeleteCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this PendingDeleteCluster.

        Date and time when the cluster was initially created, using the format defined in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt).  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this PendingDeleteCluster.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

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
        if not isinstance(other, PendingDeleteCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PendingDeleteCluster):
            return True

        return self.to_dict() != other.to_dict()
