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
from openapi_client.models.inline_response20038 import InlineResponse20038  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20038(unittest.TestCase):
    """InlineResponse20038 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20038
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20038.InlineResponse20038()  # noqa: E501
        if include_optional :
            return InlineResponse20038(
                items = [
                    openapi_client.models.encryption_key.EncryptionKey(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        name = '0', )
                    ], 
                page = 56, 
                size = 56, 
                total = 56
            )
        else :
            return InlineResponse20038(
        )

    def testInlineResponse20038(self):
        """Test InlineResponse20038"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
