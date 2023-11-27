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
from ocm_client.models.network_verification import NetworkVerification  # noqa: E501
from ocm_client.rest import ApiException

class TestNetworkVerification(unittest.TestCase):
    """NetworkVerification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkVerification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ocm_client.models.network_verification.NetworkVerification()  # noqa: E501
        if include_optional :
            return NetworkVerification(
                cloud_provider_data = ocm_client.models.cloud_provider_data.CloudProviderData(
                    aws = ocm_client.models.aws.AWS(
                        kms_key_arn = '0', 
                        sts = ocm_client.models.sts.STS(
                            oidc_endpoint_url = '0', 
                            auto_mode = True, 
                            enabled = True, 
                            external_id = '0', 
                            instance_iam_roles = ocm_client.models.instance_iam_roles.InstanceIAMRoles(
                                master_role_arn = '0', 
                                worker_role_arn = '0', ), 
                            managed_policies = True, 
                            oidc_config = ocm_client.models.oidc_config.OidcConfig(
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
                                ocm_client.models.operator_iam_role.OperatorIAMRole(
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
                        additional_compute_security_group_ids = [
                            '0'
                            ], 
                        additional_control_plane_security_group_ids = [
                            '0'
                            ], 
                        additional_infra_security_group_ids = [
                            '0'
                            ], 
                        audit_log = ocm_client.models.audit_log.AuditLog(
                            role_arn = '0', ), 
                        billing_account_id = '0', 
                        ec2_metadata_http_tokens = 'optional', 
                        etcd_encryption = ocm_client.models.aws_etcd_encryption.AwsEtcdEncryption(
                            kms_key_arn = '0', ), 
                        private_hosted_zone_id = '0', 
                        private_hosted_zone_role_arn = '0', 
                        private_link = True, 
                        private_link_configuration = ocm_client.models.private_link_cluster_configuration.PrivateLinkClusterConfiguration(
                            principals = [
                                ocm_client.models.private_link_principal.PrivateLinkPrincipal(
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
                            }, ), 
                    gcp = ocm_client.models.gcp.GCP(
                        auth_uri = '0', 
                        auth_provider_x509_cert_url = '0', 
                        client_id = '0', 
                        client_x509_cert_url = '0', 
                        client_email = '0', 
                        private_key = '0', 
                        private_key_id = '0', 
                        project_id = '0', 
                        security = ocm_client.models.gcp_security.GcpSecurity(
                            secure_boot = True, ), 
                        token_uri = '0', 
                        type = '0', ), 
                    availability_zones = [
                        '0'
                        ], 
                    key_location = '0', 
                    key_ring_name = '0', 
                    region = ocm_client.models.cloud_region.CloudRegion(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        ccs_only = True, 
                        kms_location_id = '0', 
                        kms_location_name = '0', 
                        cloud_provider = ocm_client.models.cloud_provider.CloudProvider(
                            kind = '0', 
                            id = '0', 
                            href = '0', 
                            display_name = '0', 
                            name = '0', 
                            regions = [
                                ocm_client.models.cloud_region.CloudRegion(
                                    kind = '0', 
                                    id = '0', 
                                    href = '0', 
                                    ccs_only = True, 
                                    kms_location_id = '0', 
                                    kms_location_name = '0', 
                                    display_name = '0', 
                                    enabled = True, 
                                    govcloud = True, 
                                    name = '0', 
                                    supports_hypershift = True, 
                                    supports_multi_az = True, )
                                ], ), 
                        display_name = '0', 
                        enabled = True, 
                        govcloud = True, 
                        name = '0', 
                        supports_hypershift = True, 
                        supports_multi_az = True, ), 
                    subnets = [
                        '0'
                        ], 
                    version = ocm_client.models.version.Version(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        gcp_marketplace_enabled = True, 
                        rosa_enabled = True, 
                        available_upgrades = [
                            '0'
                            ], 
                        channel_group = '0', 
                        default = True, 
                        enabled = True, 
                        end_of_life_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        hosted_control_plane_enabled = True, 
                        image_overrides = ocm_client.models.image_overrides.ImageOverrides(
                            kind = '0', 
                            id = '0', 
                            href = '0', ), 
                        raw_id = '0', 
                        release_image = '0', ), ), 
                cluster_id = '0', 
                items = [
                    ocm_client.models.subnet_network_verification.SubnetNetworkVerification(
                        kind = '0', 
                        id = '0', 
                        href = '0', 
                        details = [
                            '0'
                            ], 
                        state = '0', 
                        tags = {
                            'key' : '0'
                            }, )
                    ], 
                total = 56
            )
        else :
            return NetworkVerification(
        )

    def testNetworkVerification(self):
        """Test NetworkVerification"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
