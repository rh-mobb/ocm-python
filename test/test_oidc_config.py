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
from openapi_client.models.oidc_config import OidcConfig  # noqa: E501
from openapi_client.rest import ApiException

class TestOidcConfig(unittest.TestCase):
    """OidcConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OidcConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.oidc_config.OidcConfig()  # noqa: E501
        if include_optional :
            return OidcConfig(
                href = '0', 
                id = '0', 
                creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                installer_role_arn = '0', 
                issuer_url = '0', 
                last_update_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_used_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                managed = True, 
                organization_id = '0', 
                reusable = True, 
                secret_arn = '0'
            )
        else :
            return OidcConfig(
        )

    def testOidcConfig(self):
        """Test OidcConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
