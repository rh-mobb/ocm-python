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
from openapi_client.models.ht_passwd_user import HTPasswdUser  # noqa: E501
from openapi_client.rest import ApiException

class TestHTPasswdUser(unittest.TestCase):
    """HTPasswdUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HTPasswdUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.ht_passwd_user.HTPasswdUser()  # noqa: E501
        if include_optional :
            return HTPasswdUser(
                id = '0', 
                password = '0', 
                username = '0'
            )
        else :
            return HTPasswdUser(
        )

    def testHTPasswdUser(self):
        """Test HTPasswdUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
