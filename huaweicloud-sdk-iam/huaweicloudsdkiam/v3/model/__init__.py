# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkiam.v3.model.acl_policy_option import AclPolicyOption
from huaweicloudsdkiam.v3.model.acl_policy_result import AclPolicyResult
from huaweicloudsdkiam.v3.model.agency_all_project_role import AgencyAllProjectRole
from huaweicloudsdkiam.v3.model.agency_auth import AgencyAuth
from huaweicloudsdkiam.v3.model.agency_auth_identity import AgencyAuthIdentity
from huaweicloudsdkiam.v3.model.agency_policy import AgencyPolicy
from huaweicloudsdkiam.v3.model.agency_policy_resource import AgencyPolicyResource
from huaweicloudsdkiam.v3.model.agency_policy_role_option import AgencyPolicyRoleOption
from huaweicloudsdkiam.v3.model.agency_policy_role_result import AgencyPolicyRoleResult
from huaweicloudsdkiam.v3.model.agency_policy_statement import AgencyPolicyStatement
from huaweicloudsdkiam.v3.model.agency_result import AgencyResult
from huaweicloudsdkiam.v3.model.allow_address_netmasks_option import AllowAddressNetmasksOption
from huaweicloudsdkiam.v3.model.allow_address_netmasks_result import AllowAddressNetmasksResult
from huaweicloudsdkiam.v3.model.allow_ip_ranges_option import AllowIpRangesOption
from huaweicloudsdkiam.v3.model.allow_ip_ranges_result import AllowIpRangesResult
from huaweicloudsdkiam.v3.model.associate_agency_with_all_projects_permission_request import AssociateAgencyWithAllProjectsPermissionRequest
from huaweicloudsdkiam.v3.model.associate_agency_with_all_projects_permission_response import AssociateAgencyWithAllProjectsPermissionResponse
from huaweicloudsdkiam.v3.model.associate_agency_with_domain_permission_request import AssociateAgencyWithDomainPermissionRequest
from huaweicloudsdkiam.v3.model.associate_agency_with_domain_permission_response import AssociateAgencyWithDomainPermissionResponse
from huaweicloudsdkiam.v3.model.associate_agency_with_project_permission_request import AssociateAgencyWithProjectPermissionRequest
from huaweicloudsdkiam.v3.model.associate_agency_with_project_permission_response import AssociateAgencyWithProjectPermissionResponse
from huaweicloudsdkiam.v3.model.assumerole_sessionuser import AssumeroleSessionuser
from huaweicloudsdkiam.v3.model.auth_project_result import AuthProjectResult
from huaweicloudsdkiam.v3.model.catalog import Catalog
from huaweicloudsdkiam.v3.model.catalog_endpoints import CatalogEndpoints
from huaweicloudsdkiam.v3.model.check_all_projects_permission_for_agency_request import CheckAllProjectsPermissionForAgencyRequest
from huaweicloudsdkiam.v3.model.check_all_projects_permission_for_agency_response import CheckAllProjectsPermissionForAgencyResponse
from huaweicloudsdkiam.v3.model.check_domain_permission_for_agency_request import CheckDomainPermissionForAgencyRequest
from huaweicloudsdkiam.v3.model.check_domain_permission_for_agency_response import CheckDomainPermissionForAgencyResponse
from huaweicloudsdkiam.v3.model.check_project_permission_for_agency_request import CheckProjectPermissionForAgencyRequest
from huaweicloudsdkiam.v3.model.check_project_permission_for_agency_response import CheckProjectPermissionForAgencyResponse
from huaweicloudsdkiam.v3.model.config import Config
from huaweicloudsdkiam.v3.model.config_by_option import ConfigByOption
from huaweicloudsdkiam.v3.model.create_agency_custom_policy_request import CreateAgencyCustomPolicyRequest
from huaweicloudsdkiam.v3.model.create_agency_custom_policy_request_body import CreateAgencyCustomPolicyRequestBody
from huaweicloudsdkiam.v3.model.create_agency_custom_policy_response import CreateAgencyCustomPolicyResponse
from huaweicloudsdkiam.v3.model.create_agency_option import CreateAgencyOption
from huaweicloudsdkiam.v3.model.create_agency_request import CreateAgencyRequest
from huaweicloudsdkiam.v3.model.create_agency_request_body import CreateAgencyRequestBody
from huaweicloudsdkiam.v3.model.create_agency_response import CreateAgencyResponse
from huaweicloudsdkiam.v3.model.create_cloud_service_custom_policy_request import CreateCloudServiceCustomPolicyRequest
from huaweicloudsdkiam.v3.model.create_cloud_service_custom_policy_request_body import CreateCloudServiceCustomPolicyRequestBody
from huaweicloudsdkiam.v3.model.create_cloud_service_custom_policy_response import CreateCloudServiceCustomPolicyResponse
from huaweicloudsdkiam.v3.model.create_credential_option import CreateCredentialOption
from huaweicloudsdkiam.v3.model.create_credential_result import CreateCredentialResult
from huaweicloudsdkiam.v3.model.create_permanent_access_key_request import CreatePermanentAccessKeyRequest
from huaweicloudsdkiam.v3.model.create_permanent_access_key_request_body import CreatePermanentAccessKeyRequestBody
from huaweicloudsdkiam.v3.model.create_permanent_access_key_response import CreatePermanentAccessKeyResponse
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_agency_request import CreateTemporaryAccessKeyByAgencyRequest
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_agency_request_body import CreateTemporaryAccessKeyByAgencyRequestBody
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_agency_response import CreateTemporaryAccessKeyByAgencyResponse
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_token_request import CreateTemporaryAccessKeyByTokenRequest
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_token_request_body import CreateTemporaryAccessKeyByTokenRequestBody
from huaweicloudsdkiam.v3.model.create_temporary_access_key_by_token_response import CreateTemporaryAccessKeyByTokenResponse
from huaweicloudsdkiam.v3.model.create_user_option import CreateUserOption
from huaweicloudsdkiam.v3.model.create_user_request import CreateUserRequest
from huaweicloudsdkiam.v3.model.create_user_request_body import CreateUserRequestBody
from huaweicloudsdkiam.v3.model.create_user_response import CreateUserResponse
from huaweicloudsdkiam.v3.model.create_user_result import CreateUserResult
from huaweicloudsdkiam.v3.model.credential import Credential
from huaweicloudsdkiam.v3.model.credentials import Credentials
from huaweicloudsdkiam.v3.model.delete_agency_request import DeleteAgencyRequest
from huaweicloudsdkiam.v3.model.delete_agency_response import DeleteAgencyResponse
from huaweicloudsdkiam.v3.model.delete_custom_policy_request import DeleteCustomPolicyRequest
from huaweicloudsdkiam.v3.model.delete_custom_policy_response import DeleteCustomPolicyResponse
from huaweicloudsdkiam.v3.model.delete_permanent_access_key_request import DeletePermanentAccessKeyRequest
from huaweicloudsdkiam.v3.model.delete_permanent_access_key_response import DeletePermanentAccessKeyResponse
from huaweicloudsdkiam.v3.model.domains import Domains
from huaweicloudsdkiam.v3.model.endpoint import Endpoint
from huaweicloudsdkiam.v3.model.identity_assumerole import IdentityAssumerole
from huaweicloudsdkiam.v3.model.identity_token import IdentityToken
from huaweicloudsdkiam.v3.model.keystone_add_user_to_group_request import KeystoneAddUserToGroupRequest
from huaweicloudsdkiam.v3.model.keystone_add_user_to_group_response import KeystoneAddUserToGroupResponse
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_all_project_permission_request import KeystoneAssociateGroupWithAllProjectPermissionRequest
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_all_project_permission_response import KeystoneAssociateGroupWithAllProjectPermissionResponse
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_domain_permission_request import KeystoneAssociateGroupWithDomainPermissionRequest
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_domain_permission_response import KeystoneAssociateGroupWithDomainPermissionResponse
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_project_permission_request import KeystoneAssociateGroupWithProjectPermissionRequest
from huaweicloudsdkiam.v3.model.keystone_associate_group_with_project_permission_response import KeystoneAssociateGroupWithProjectPermissionResponse
from huaweicloudsdkiam.v3.model.keystone_check_domain_permission_for_group_request import KeystoneCheckDomainPermissionForGroupRequest
from huaweicloudsdkiam.v3.model.keystone_check_domain_permission_for_group_response import KeystoneCheckDomainPermissionForGroupResponse
from huaweicloudsdkiam.v3.model.keystone_check_project_permission_for_group_request import KeystoneCheckProjectPermissionForGroupRequest
from huaweicloudsdkiam.v3.model.keystone_check_project_permission_for_group_response import KeystoneCheckProjectPermissionForGroupResponse
from huaweicloudsdkiam.v3.model.keystone_check_user_in_group_request import KeystoneCheckUserInGroupRequest
from huaweicloudsdkiam.v3.model.keystone_check_user_in_group_response import KeystoneCheckUserInGroupResponse
from huaweicloudsdkiam.v3.model.keystone_create_group_option import KeystoneCreateGroupOption
from huaweicloudsdkiam.v3.model.keystone_create_group_request import KeystoneCreateGroupRequest
from huaweicloudsdkiam.v3.model.keystone_create_group_request_body import KeystoneCreateGroupRequestBody
from huaweicloudsdkiam.v3.model.keystone_create_group_response import KeystoneCreateGroupResponse
from huaweicloudsdkiam.v3.model.keystone_create_project_option import KeystoneCreateProjectOption
from huaweicloudsdkiam.v3.model.keystone_create_project_request import KeystoneCreateProjectRequest
from huaweicloudsdkiam.v3.model.keystone_create_project_request_body import KeystoneCreateProjectRequestBody
from huaweicloudsdkiam.v3.model.keystone_create_project_response import KeystoneCreateProjectResponse
from huaweicloudsdkiam.v3.model.keystone_create_user_option import KeystoneCreateUserOption
from huaweicloudsdkiam.v3.model.keystone_create_user_request import KeystoneCreateUserRequest
from huaweicloudsdkiam.v3.model.keystone_create_user_request_body import KeystoneCreateUserRequestBody
from huaweicloudsdkiam.v3.model.keystone_create_user_response import KeystoneCreateUserResponse
from huaweicloudsdkiam.v3.model.keystone_create_user_result import KeystoneCreateUserResult
from huaweicloudsdkiam.v3.model.keystone_delete_group_request import KeystoneDeleteGroupRequest
from huaweicloudsdkiam.v3.model.keystone_delete_group_response import KeystoneDeleteGroupResponse
from huaweicloudsdkiam.v3.model.keystone_delete_user_request import KeystoneDeleteUserRequest
from huaweicloudsdkiam.v3.model.keystone_delete_user_response import KeystoneDeleteUserResponse
from huaweicloudsdkiam.v3.model.keystone_group_result import KeystoneGroupResult
from huaweicloudsdkiam.v3.model.keystone_group_result_with_links_self import KeystoneGroupResultWithLinksSelf
from huaweicloudsdkiam.v3.model.keystone_list_auth_domains_request import KeystoneListAuthDomainsRequest
from huaweicloudsdkiam.v3.model.keystone_list_auth_domains_response import KeystoneListAuthDomainsResponse
from huaweicloudsdkiam.v3.model.keystone_list_auth_projects_request import KeystoneListAuthProjectsRequest
from huaweicloudsdkiam.v3.model.keystone_list_auth_projects_response import KeystoneListAuthProjectsResponse
from huaweicloudsdkiam.v3.model.keystone_list_domain_permissions_for_group_request import KeystoneListDomainPermissionsForGroupRequest
from huaweicloudsdkiam.v3.model.keystone_list_domain_permissions_for_group_response import KeystoneListDomainPermissionsForGroupResponse
from huaweicloudsdkiam.v3.model.keystone_list_endpoints_request import KeystoneListEndpointsRequest
from huaweicloudsdkiam.v3.model.keystone_list_endpoints_response import KeystoneListEndpointsResponse
from huaweicloudsdkiam.v3.model.keystone_list_groups_for_user_request import KeystoneListGroupsForUserRequest
from huaweicloudsdkiam.v3.model.keystone_list_groups_for_user_response import KeystoneListGroupsForUserResponse
from huaweicloudsdkiam.v3.model.keystone_list_groups_request import KeystoneListGroupsRequest
from huaweicloudsdkiam.v3.model.keystone_list_groups_response import KeystoneListGroupsResponse
from huaweicloudsdkiam.v3.model.keystone_list_permissions_request import KeystoneListPermissionsRequest
from huaweicloudsdkiam.v3.model.keystone_list_permissions_response import KeystoneListPermissionsResponse
from huaweicloudsdkiam.v3.model.keystone_list_project_permissions_for_group_request import KeystoneListProjectPermissionsForGroupRequest
from huaweicloudsdkiam.v3.model.keystone_list_project_permissions_for_group_response import KeystoneListProjectPermissionsForGroupResponse
from huaweicloudsdkiam.v3.model.keystone_list_projects_for_user_request import KeystoneListProjectsForUserRequest
from huaweicloudsdkiam.v3.model.keystone_list_projects_for_user_response import KeystoneListProjectsForUserResponse
from huaweicloudsdkiam.v3.model.keystone_list_projects_request import KeystoneListProjectsRequest
from huaweicloudsdkiam.v3.model.keystone_list_projects_response import KeystoneListProjectsResponse
from huaweicloudsdkiam.v3.model.keystone_list_regions_request import KeystoneListRegionsRequest
from huaweicloudsdkiam.v3.model.keystone_list_regions_response import KeystoneListRegionsResponse
from huaweicloudsdkiam.v3.model.keystone_list_services_request import KeystoneListServicesRequest
from huaweicloudsdkiam.v3.model.keystone_list_services_response import KeystoneListServicesResponse
from huaweicloudsdkiam.v3.model.keystone_list_users_for_group_by_admin_request import KeystoneListUsersForGroupByAdminRequest
from huaweicloudsdkiam.v3.model.keystone_list_users_for_group_by_admin_response import KeystoneListUsersForGroupByAdminResponse
from huaweicloudsdkiam.v3.model.keystone_list_users_request import KeystoneListUsersRequest
from huaweicloudsdkiam.v3.model.keystone_list_users_response import KeystoneListUsersResponse
from huaweicloudsdkiam.v3.model.keystone_list_users_result import KeystoneListUsersResult
from huaweicloudsdkiam.v3.model.keystone_list_versions_request import KeystoneListVersionsRequest
from huaweicloudsdkiam.v3.model.keystone_list_versions_response import KeystoneListVersionsResponse
from huaweicloudsdkiam.v3.model.keystone_remove_domain_permission_from_group_request import KeystoneRemoveDomainPermissionFromGroupRequest
from huaweicloudsdkiam.v3.model.keystone_remove_domain_permission_from_group_response import KeystoneRemoveDomainPermissionFromGroupResponse
from huaweicloudsdkiam.v3.model.keystone_remove_project_permission_from_group_request import KeystoneRemoveProjectPermissionFromGroupRequest
from huaweicloudsdkiam.v3.model.keystone_remove_project_permission_from_group_response import KeystoneRemoveProjectPermissionFromGroupResponse
from huaweicloudsdkiam.v3.model.keystone_remove_user_from_group_request import KeystoneRemoveUserFromGroupRequest
from huaweicloudsdkiam.v3.model.keystone_remove_user_from_group_response import KeystoneRemoveUserFromGroupResponse
from huaweicloudsdkiam.v3.model.keystone_show_catalog_request import KeystoneShowCatalogRequest
from huaweicloudsdkiam.v3.model.keystone_show_catalog_response import KeystoneShowCatalogResponse
from huaweicloudsdkiam.v3.model.keystone_show_endpoint_request import KeystoneShowEndpointRequest
from huaweicloudsdkiam.v3.model.keystone_show_endpoint_response import KeystoneShowEndpointResponse
from huaweicloudsdkiam.v3.model.keystone_show_group_request import KeystoneShowGroupRequest
from huaweicloudsdkiam.v3.model.keystone_show_group_response import KeystoneShowGroupResponse
from huaweicloudsdkiam.v3.model.keystone_show_permission_request import KeystoneShowPermissionRequest
from huaweicloudsdkiam.v3.model.keystone_show_permission_response import KeystoneShowPermissionResponse
from huaweicloudsdkiam.v3.model.keystone_show_project_request import KeystoneShowProjectRequest
from huaweicloudsdkiam.v3.model.keystone_show_project_response import KeystoneShowProjectResponse
from huaweicloudsdkiam.v3.model.keystone_show_region_request import KeystoneShowRegionRequest
from huaweicloudsdkiam.v3.model.keystone_show_region_response import KeystoneShowRegionResponse
from huaweicloudsdkiam.v3.model.keystone_show_security_compliance_by_option_request import KeystoneShowSecurityComplianceByOptionRequest
from huaweicloudsdkiam.v3.model.keystone_show_security_compliance_by_option_response import KeystoneShowSecurityComplianceByOptionResponse
from huaweicloudsdkiam.v3.model.keystone_show_security_compliance_request import KeystoneShowSecurityComplianceRequest
from huaweicloudsdkiam.v3.model.keystone_show_security_compliance_response import KeystoneShowSecurityComplianceResponse
from huaweicloudsdkiam.v3.model.keystone_show_service_request import KeystoneShowServiceRequest
from huaweicloudsdkiam.v3.model.keystone_show_service_response import KeystoneShowServiceResponse
from huaweicloudsdkiam.v3.model.keystone_show_user_request import KeystoneShowUserRequest
from huaweicloudsdkiam.v3.model.keystone_show_user_response import KeystoneShowUserResponse
from huaweicloudsdkiam.v3.model.keystone_show_user_result import KeystoneShowUserResult
from huaweicloudsdkiam.v3.model.keystone_show_version_request import KeystoneShowVersionRequest
from huaweicloudsdkiam.v3.model.keystone_show_version_response import KeystoneShowVersionResponse
from huaweicloudsdkiam.v3.model.keystone_update_group_option import KeystoneUpdateGroupOption
from huaweicloudsdkiam.v3.model.keystone_update_group_request import KeystoneUpdateGroupRequest
from huaweicloudsdkiam.v3.model.keystone_update_group_request_body import KeystoneUpdateGroupRequestBody
from huaweicloudsdkiam.v3.model.keystone_update_group_response import KeystoneUpdateGroupResponse
from huaweicloudsdkiam.v3.model.keystone_update_password_option import KeystoneUpdatePasswordOption
from huaweicloudsdkiam.v3.model.keystone_update_project_option import KeystoneUpdateProjectOption
from huaweicloudsdkiam.v3.model.keystone_update_project_request import KeystoneUpdateProjectRequest
from huaweicloudsdkiam.v3.model.keystone_update_project_request_body import KeystoneUpdateProjectRequestBody
from huaweicloudsdkiam.v3.model.keystone_update_project_response import KeystoneUpdateProjectResponse
from huaweicloudsdkiam.v3.model.keystone_update_project_result import KeystoneUpdateProjectResult
from huaweicloudsdkiam.v3.model.keystone_update_user_by_admin_request import KeystoneUpdateUserByAdminRequest
from huaweicloudsdkiam.v3.model.keystone_update_user_by_admin_request_body import KeystoneUpdateUserByAdminRequestBody
from huaweicloudsdkiam.v3.model.keystone_update_user_by_admin_response import KeystoneUpdateUserByAdminResponse
from huaweicloudsdkiam.v3.model.keystone_update_user_by_admin_result import KeystoneUpdateUserByAdminResult
from huaweicloudsdkiam.v3.model.keystone_update_user_option import KeystoneUpdateUserOption
from huaweicloudsdkiam.v3.model.keystone_update_user_password_request import KeystoneUpdateUserPasswordRequest
from huaweicloudsdkiam.v3.model.keystone_update_user_password_request_body import KeystoneUpdateUserPasswordRequestBody
from huaweicloudsdkiam.v3.model.keystone_update_user_password_response import KeystoneUpdateUserPasswordResponse
from huaweicloudsdkiam.v3.model.keystone_user_result import KeystoneUserResult
from huaweicloudsdkiam.v3.model.keystone_user_result_extra import KeystoneUserResultExtra
from huaweicloudsdkiam.v3.model.links import Links
from huaweicloudsdkiam.v3.model.links_self import LinksSelf
from huaweicloudsdkiam.v3.model.list_agencies_request import ListAgenciesRequest
from huaweicloudsdkiam.v3.model.list_agencies_response import ListAgenciesResponse
from huaweicloudsdkiam.v3.model.list_all_projects_permissions_for_agency_request import ListAllProjectsPermissionsForAgencyRequest
from huaweicloudsdkiam.v3.model.list_all_projects_permissions_for_agency_response import ListAllProjectsPermissionsForAgencyResponse
from huaweicloudsdkiam.v3.model.list_custom_policies_request import ListCustomPoliciesRequest
from huaweicloudsdkiam.v3.model.list_custom_policies_response import ListCustomPoliciesResponse
from huaweicloudsdkiam.v3.model.list_domain_permissions_for_agency_request import ListDomainPermissionsForAgencyRequest
from huaweicloudsdkiam.v3.model.list_domain_permissions_for_agency_response import ListDomainPermissionsForAgencyResponse
from huaweicloudsdkiam.v3.model.list_permanent_access_keys_request import ListPermanentAccessKeysRequest
from huaweicloudsdkiam.v3.model.list_permanent_access_keys_response import ListPermanentAccessKeysResponse
from huaweicloudsdkiam.v3.model.list_project_permissions_for_agency_request import ListProjectPermissionsForAgencyRequest
from huaweicloudsdkiam.v3.model.list_project_permissions_for_agency_response import ListProjectPermissionsForAgencyResponse
from huaweicloudsdkiam.v3.model.list_user_login_protects_request import ListUserLoginProtectsRequest
from huaweicloudsdkiam.v3.model.list_user_login_protects_response import ListUserLoginProtectsResponse
from huaweicloudsdkiam.v3.model.list_user_mfa_devices_request import ListUserMfaDevicesRequest
from huaweicloudsdkiam.v3.model.list_user_mfa_devices_response import ListUserMfaDevicesResponse
from huaweicloudsdkiam.v3.model.login_policy_option import LoginPolicyOption
from huaweicloudsdkiam.v3.model.login_policy_result import LoginPolicyResult
from huaweicloudsdkiam.v3.model.login_protect_result import LoginProtectResult
from huaweicloudsdkiam.v3.model.mfa_device_result import MfaDeviceResult
from huaweicloudsdkiam.v3.model.password_policy_option import PasswordPolicyOption
from huaweicloudsdkiam.v3.model.password_policy_result import PasswordPolicyResult
from huaweicloudsdkiam.v3.model.policy_depends import PolicyDepends
from huaweicloudsdkiam.v3.model.policy_role_result import PolicyRoleResult
from huaweicloudsdkiam.v3.model.policy_statement import PolicyStatement
from huaweicloudsdkiam.v3.model.project_details_and_status_result import ProjectDetailsAndStatusResult
from huaweicloudsdkiam.v3.model.project_result import ProjectResult
from huaweicloudsdkiam.v3.model.protect_policy_option import ProtectPolicyOption
from huaweicloudsdkiam.v3.model.protect_policy_result import ProtectPolicyResult
from huaweicloudsdkiam.v3.model.quota_result import QuotaResult
from huaweicloudsdkiam.v3.model.region import Region
from huaweicloudsdkiam.v3.model.region_locales import RegionLocales
from huaweicloudsdkiam.v3.model.remove_all_projects_permission_from_agency_request import RemoveAllProjectsPermissionFromAgencyRequest
from huaweicloudsdkiam.v3.model.remove_all_projects_permission_from_agency_response import RemoveAllProjectsPermissionFromAgencyResponse
from huaweicloudsdkiam.v3.model.remove_domain_permission_from_agency_request import RemoveDomainPermissionFromAgencyRequest
from huaweicloudsdkiam.v3.model.remove_domain_permission_from_agency_response import RemoveDomainPermissionFromAgencyResponse
from huaweicloudsdkiam.v3.model.remove_project_permission_from_agency_request import RemoveProjectPermissionFromAgencyRequest
from huaweicloudsdkiam.v3.model.remove_project_permission_from_agency_response import RemoveProjectPermissionFromAgencyResponse
from huaweicloudsdkiam.v3.model.resources import Resources
from huaweicloudsdkiam.v3.model.role_policy import RolePolicy
from huaweicloudsdkiam.v3.model.role_result import RoleResult
from huaweicloudsdkiam.v3.model.security_compliance import SecurityCompliance
from huaweicloudsdkiam.v3.model.service import Service
from huaweicloudsdkiam.v3.model.service_policy import ServicePolicy
from huaweicloudsdkiam.v3.model.service_policy_role_option import ServicePolicyRoleOption
from huaweicloudsdkiam.v3.model.service_policy_role_result import ServicePolicyRoleResult
from huaweicloudsdkiam.v3.model.service_statement import ServiceStatement
from huaweicloudsdkiam.v3.model.show_agency_request import ShowAgencyRequest
from huaweicloudsdkiam.v3.model.show_agency_response import ShowAgencyResponse
from huaweicloudsdkiam.v3.model.show_credential import ShowCredential
from huaweicloudsdkiam.v3.model.show_custom_policy_request import ShowCustomPolicyRequest
from huaweicloudsdkiam.v3.model.show_custom_policy_response import ShowCustomPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_api_acl_policy_request import ShowDomainApiAclPolicyRequest
from huaweicloudsdkiam.v3.model.show_domain_api_acl_policy_response import ShowDomainApiAclPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_console_acl_policy_request import ShowDomainConsoleAclPolicyRequest
from huaweicloudsdkiam.v3.model.show_domain_console_acl_policy_response import ShowDomainConsoleAclPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_login_policy_request import ShowDomainLoginPolicyRequest
from huaweicloudsdkiam.v3.model.show_domain_login_policy_response import ShowDomainLoginPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_password_policy_request import ShowDomainPasswordPolicyRequest
from huaweicloudsdkiam.v3.model.show_domain_password_policy_response import ShowDomainPasswordPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_protect_policy_request import ShowDomainProtectPolicyRequest
from huaweicloudsdkiam.v3.model.show_domain_protect_policy_response import ShowDomainProtectPolicyResponse
from huaweicloudsdkiam.v3.model.show_domain_quota_request import ShowDomainQuotaRequest
from huaweicloudsdkiam.v3.model.show_domain_quota_response import ShowDomainQuotaResponse
from huaweicloudsdkiam.v3.model.show_permanent_access_key_request import ShowPermanentAccessKeyRequest
from huaweicloudsdkiam.v3.model.show_permanent_access_key_response import ShowPermanentAccessKeyResponse
from huaweicloudsdkiam.v3.model.show_project_details_and_status_request import ShowProjectDetailsAndStatusRequest
from huaweicloudsdkiam.v3.model.show_project_details_and_status_response import ShowProjectDetailsAndStatusResponse
from huaweicloudsdkiam.v3.model.show_project_quota_request import ShowProjectQuotaRequest
from huaweicloudsdkiam.v3.model.show_project_quota_response import ShowProjectQuotaResponse
from huaweicloudsdkiam.v3.model.show_user_login_protect_request import ShowUserLoginProtectRequest
from huaweicloudsdkiam.v3.model.show_user_login_protect_response import ShowUserLoginProtectResponse
from huaweicloudsdkiam.v3.model.show_user_mfa_device_request import ShowUserMfaDeviceRequest
from huaweicloudsdkiam.v3.model.show_user_mfa_device_response import ShowUserMfaDeviceResponse
from huaweicloudsdkiam.v3.model.show_user_request import ShowUserRequest
from huaweicloudsdkiam.v3.model.show_user_response import ShowUserResponse
from huaweicloudsdkiam.v3.model.show_user_result import ShowUserResult
from huaweicloudsdkiam.v3.model.token_auth import TokenAuth
from huaweicloudsdkiam.v3.model.token_auth_identity import TokenAuthIdentity
from huaweicloudsdkiam.v3.model.update_agency_custom_policy_request import UpdateAgencyCustomPolicyRequest
from huaweicloudsdkiam.v3.model.update_agency_custom_policy_request_body import UpdateAgencyCustomPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_agency_custom_policy_response import UpdateAgencyCustomPolicyResponse
from huaweicloudsdkiam.v3.model.update_agency_option import UpdateAgencyOption
from huaweicloudsdkiam.v3.model.update_agency_request import UpdateAgencyRequest
from huaweicloudsdkiam.v3.model.update_agency_request_body import UpdateAgencyRequestBody
from huaweicloudsdkiam.v3.model.update_agency_response import UpdateAgencyResponse
from huaweicloudsdkiam.v3.model.update_cloud_service_custom_policy_request import UpdateCloudServiceCustomPolicyRequest
from huaweicloudsdkiam.v3.model.update_cloud_service_custom_policy_request_body import UpdateCloudServiceCustomPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_cloud_service_custom_policy_response import UpdateCloudServiceCustomPolicyResponse
from huaweicloudsdkiam.v3.model.update_credential_option import UpdateCredentialOption
from huaweicloudsdkiam.v3.model.update_credential_result import UpdateCredentialResult
from huaweicloudsdkiam.v3.model.update_domain_api_acl_policy_request import UpdateDomainApiAclPolicyRequest
from huaweicloudsdkiam.v3.model.update_domain_api_acl_policy_request_body import UpdateDomainApiAclPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_domain_api_acl_policy_response import UpdateDomainApiAclPolicyResponse
from huaweicloudsdkiam.v3.model.update_domain_console_acl_policy_request import UpdateDomainConsoleAclPolicyRequest
from huaweicloudsdkiam.v3.model.update_domain_console_acl_policy_request_body import UpdateDomainConsoleAclPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_domain_console_acl_policy_response import UpdateDomainConsoleAclPolicyResponse
from huaweicloudsdkiam.v3.model.update_domain_login_policy_request import UpdateDomainLoginPolicyRequest
from huaweicloudsdkiam.v3.model.update_domain_login_policy_request_body import UpdateDomainLoginPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_domain_login_policy_response import UpdateDomainLoginPolicyResponse
from huaweicloudsdkiam.v3.model.update_domain_password_policy_request import UpdateDomainPasswordPolicyRequest
from huaweicloudsdkiam.v3.model.update_domain_password_policy_request_body import UpdateDomainPasswordPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_domain_password_policy_response import UpdateDomainPasswordPolicyResponse
from huaweicloudsdkiam.v3.model.update_domain_protect_policy_request import UpdateDomainProtectPolicyRequest
from huaweicloudsdkiam.v3.model.update_domain_protect_policy_request_body import UpdateDomainProtectPolicyRequestBody
from huaweicloudsdkiam.v3.model.update_domain_protect_policy_response import UpdateDomainProtectPolicyResponse
from huaweicloudsdkiam.v3.model.update_permanent_access_key_request import UpdatePermanentAccessKeyRequest
from huaweicloudsdkiam.v3.model.update_permanent_access_key_request_body import UpdatePermanentAccessKeyRequestBody
from huaweicloudsdkiam.v3.model.update_permanent_access_key_response import UpdatePermanentAccessKeyResponse
from huaweicloudsdkiam.v3.model.update_project_option import UpdateProjectOption
from huaweicloudsdkiam.v3.model.update_project_status_request import UpdateProjectStatusRequest
from huaweicloudsdkiam.v3.model.update_project_status_request_body import UpdateProjectStatusRequestBody
from huaweicloudsdkiam.v3.model.update_project_status_response import UpdateProjectStatusResponse
from huaweicloudsdkiam.v3.model.update_user_information_option import UpdateUserInformationOption
from huaweicloudsdkiam.v3.model.update_user_information_request import UpdateUserInformationRequest
from huaweicloudsdkiam.v3.model.update_user_information_request_body import UpdateUserInformationRequestBody
from huaweicloudsdkiam.v3.model.update_user_information_response import UpdateUserInformationResponse
from huaweicloudsdkiam.v3.model.update_user_option import UpdateUserOption
from huaweicloudsdkiam.v3.model.update_user_request import UpdateUserRequest
from huaweicloudsdkiam.v3.model.update_user_request_body import UpdateUserRequestBody
from huaweicloudsdkiam.v3.model.update_user_response import UpdateUserResponse
from huaweicloudsdkiam.v3.model.update_user_result import UpdateUserResult
from huaweicloudsdkiam.v3.model.version import Version
from huaweicloudsdkiam.v3.model.version_links import VersionLinks
from huaweicloudsdkiam.v3.model.version_mediatypes import VersionMediatypes
from huaweicloudsdkiam.v3.model.versions import Versions
