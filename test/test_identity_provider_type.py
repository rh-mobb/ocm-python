# coding: utf-8

"""
    clusters_mgmt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: ocm-feedback@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.identity_provider_type import IdentityProviderType  # noqa: E501
from openapi_client.rest import ApiException

class TestIdentityProviderType(unittest.TestCase):
    """IdentityProviderType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IdentityProviderType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.identity_provider_type.IdentityProviderType()  # noqa: E501
        if include_optional :
            return IdentityProviderType(
            )
        else :
            return IdentityProviderType(
        )

    def testIdentityProviderType(self):
        """Test IdentityProviderType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()