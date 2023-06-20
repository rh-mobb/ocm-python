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
from openapi_client.models.limited_support_reason import LimitedSupportReason  # noqa: E501
from openapi_client.rest import ApiException

class TestLimitedSupportReason(unittest.TestCase):
    """LimitedSupportReason unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LimitedSupportReason
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.limited_support_reason.LimitedSupportReason()  # noqa: E501
        if include_optional :
            return LimitedSupportReason(
                kind = '0', 
                id = '0', 
                href = '0', 
                creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                details = '0', 
                detection_type = 'auto', 
                summary = '0', 
                template = openapi_client.models.limited_support_reason_template.LimitedSupportReasonTemplate(
                    kind = '0', 
                    id = '0', 
                    href = '0', 
                    details = '0', 
                    summary = '0', )
            )
        else :
            return LimitedSupportReason(
        )

    def testLimitedSupportReason(self):
        """Test LimitedSupportReason"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
