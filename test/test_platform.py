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

import ocm_client
from ocm_client.models.platform import Platform  # noqa: E501
from ocm_client.rest import ApiException

class TestPlatform(unittest.TestCase):
    """Platform unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Platform
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ocm_client.models.platform.Platform()  # noqa: E501
        if include_optional :
            return Platform(
            )
        else :
            return Platform(
        )

    def testPlatform(self):
        """Test Platform"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
