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
from openapi_client.models.inline_response20024 import InlineResponse20024  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20024(unittest.TestCase):
    """InlineResponse20024 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20024
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20024.InlineResponse20024()  # noqa: E501
        if include_optional :
            return InlineResponse20024(
                items = [
                    openapi_client.models.ht_passwd_user.HTPasswdUser(
                        id = '0', 
                        password = '0', 
                        username = '0', )
                    ], 
                page = 56, 
                size = 56, 
                total = 56
            )
        else :
            return InlineResponse20024(
        )

    def testInlineResponse20024(self):
        """Test InlineResponse20024"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
