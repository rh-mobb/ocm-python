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
from openapi_client.models.aws import AWS  # noqa: E501
from openapi_client.rest import ApiException

class TestAWS(unittest.TestCase):
    """AWS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AWS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.aws.AWS()  # noqa: E501
        if include_optional :
            return AWS(
                kms_key_arn = '0', 
                sts = openapi_client.models.sts.STS(
                    oidc_endpoint_url = '0', 
                    auto_mode = True, 
                    enabled = True, 
                    external_id = '0', 
                    instance_iam_roles = openapi_client.models.instance_iam_roles.InstanceIAMRoles(
                        master_role_arn = '0', 
                        worker_role_arn = '0', ), 
                    managed_policies = True, 
                    oidc_config = openapi_client.models.oidc_config.OidcConfig(
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
                        secret_arn = '0', ), 
                    operator_iam_roles = [
                        openapi_client.models.operator_iam_role.OperatorIAMRole(
                            id = '0', 
                            name = '0', 
                            namespace = '0', 
                            role_arn = '0', 
                            service_account = '0', )
                        ], 
                    operator_role_prefix = '0', 
                    permission_boundary = '0', 
                    role_arn = '0', 
                    support_role_arn = '0', ), 
                access_key_id = '0', 
                account_id = '0', 
                audit_log = openapi_client.models.audit_log.AuditLog(
                    role_arn = '0', ), 
                billing_account_id = '0', 
                ec2_metadata_http_tokens = 'optional', 
                etcd_encryption = openapi_client.models.aws_etcd_encryption.AwsEtcdEncryption(
                    kms_key_arn = '0', ), 
                private_link = True, 
                private_link_configuration = openapi_client.models.private_link_cluster_configuration.PrivateLinkClusterConfiguration(
                    principals = [
                        openapi_client.models.private_link_principal.PrivateLinkPrincipal(
                            kind = '0', 
                            id = '0', 
                            href = '0', 
                            principal = '0', )
                        ], ), 
                secret_access_key = '0', 
                subnet_ids = [
                    '0'
                    ], 
                tags = {
                    'key' : '0'
                    }
            )
        else :
            return AWS(
        )

    def testAWS(self):
        """Test AWS"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
