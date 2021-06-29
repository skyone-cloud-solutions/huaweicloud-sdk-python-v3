# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkas.v1.model.all_quotas import AllQuotas
from huaweicloudsdkas.v1.model.all_resources import AllResources
from huaweicloudsdkas.v1.model.attach_callback_instance_life_cycle_hook_request import AttachCallbackInstanceLifeCycleHookRequest
from huaweicloudsdkas.v1.model.attach_callback_instance_life_cycle_hook_response import AttachCallbackInstanceLifeCycleHookResponse
from huaweicloudsdkas.v1.model.bandwidth_info import BandwidthInfo
from huaweicloudsdkas.v1.model.bandwidth_result import BandwidthResult
from huaweicloudsdkas.v1.model.batch_add_instances_option import BatchAddInstancesOption
from huaweicloudsdkas.v1.model.batch_add_scaling_instances_request import BatchAddScalingInstancesRequest
from huaweicloudsdkas.v1.model.batch_add_scaling_instances_response import BatchAddScalingInstancesResponse
from huaweicloudsdkas.v1.model.batch_delete_scaling_config_option import BatchDeleteScalingConfigOption
from huaweicloudsdkas.v1.model.batch_delete_scaling_configs_request import BatchDeleteScalingConfigsRequest
from huaweicloudsdkas.v1.model.batch_delete_scaling_configs_response import BatchDeleteScalingConfigsResponse
from huaweicloudsdkas.v1.model.batch_delete_scaling_policies_option import BatchDeleteScalingPoliciesOption
from huaweicloudsdkas.v1.model.batch_delete_scaling_policies_request import BatchDeleteScalingPoliciesRequest
from huaweicloudsdkas.v1.model.batch_delete_scaling_policies_response import BatchDeleteScalingPoliciesResponse
from huaweicloudsdkas.v1.model.batch_enter_standby_instances_option import BatchEnterStandbyInstancesOption
from huaweicloudsdkas.v1.model.batch_exit_stand_by_instances_option import BatchExitStandByInstancesOption
from huaweicloudsdkas.v1.model.batch_pause_scaling_policies_option import BatchPauseScalingPoliciesOption
from huaweicloudsdkas.v1.model.batch_pause_scaling_policies_request import BatchPauseScalingPoliciesRequest
from huaweicloudsdkas.v1.model.batch_pause_scaling_policies_response import BatchPauseScalingPoliciesResponse
from huaweicloudsdkas.v1.model.batch_protect_instances_option import BatchProtectInstancesOption
from huaweicloudsdkas.v1.model.batch_protect_scaling_instances_request import BatchProtectScalingInstancesRequest
from huaweicloudsdkas.v1.model.batch_protect_scaling_instances_response import BatchProtectScalingInstancesResponse
from huaweicloudsdkas.v1.model.batch_remove_instances_option import BatchRemoveInstancesOption
from huaweicloudsdkas.v1.model.batch_remove_scaling_instances_request import BatchRemoveScalingInstancesRequest
from huaweicloudsdkas.v1.model.batch_remove_scaling_instances_response import BatchRemoveScalingInstancesResponse
from huaweicloudsdkas.v1.model.batch_resume_scaling_policies_option import BatchResumeScalingPoliciesOption
from huaweicloudsdkas.v1.model.batch_resume_scaling_policies_request import BatchResumeScalingPoliciesRequest
from huaweicloudsdkas.v1.model.batch_resume_scaling_policies_response import BatchResumeScalingPoliciesResponse
from huaweicloudsdkas.v1.model.batch_set_scaling_instances_standby_request import BatchSetScalingInstancesStandbyRequest
from huaweicloudsdkas.v1.model.batch_set_scaling_instances_standby_response import BatchSetScalingInstancesStandbyResponse
from huaweicloudsdkas.v1.model.batch_unprotect_instances_option import BatchUnprotectInstancesOption
from huaweicloudsdkas.v1.model.batch_unprotect_scaling_instances_request import BatchUnprotectScalingInstancesRequest
from huaweicloudsdkas.v1.model.batch_unprotect_scaling_instances_response import BatchUnprotectScalingInstancesResponse
from huaweicloudsdkas.v1.model.batch_unset_scaling_instances_stantby_request import BatchUnsetScalingInstancesStantbyRequest
from huaweicloudsdkas.v1.model.batch_unset_scaling_instances_stantby_response import BatchUnsetScalingInstancesStantbyResponse
from huaweicloudsdkas.v1.model.callback_life_cycle_hook_option import CallbackLifeCycleHookOption
from huaweicloudsdkas.v1.model.create_life_cycle_hook_option import CreateLifeCycleHookOption
from huaweicloudsdkas.v1.model.create_lify_cycle_hook_request import CreateLifyCycleHookRequest
from huaweicloudsdkas.v1.model.create_lify_cycle_hook_response import CreateLifyCycleHookResponse
from huaweicloudsdkas.v1.model.create_notification_option import CreateNotificationOption
from huaweicloudsdkas.v1.model.create_scaling_config_option import CreateScalingConfigOption
from huaweicloudsdkas.v1.model.create_scaling_config_request import CreateScalingConfigRequest
from huaweicloudsdkas.v1.model.create_scaling_config_response import CreateScalingConfigResponse
from huaweicloudsdkas.v1.model.create_scaling_group_option import CreateScalingGroupOption
from huaweicloudsdkas.v1.model.create_scaling_group_request import CreateScalingGroupRequest
from huaweicloudsdkas.v1.model.create_scaling_group_response import CreateScalingGroupResponse
from huaweicloudsdkas.v1.model.create_scaling_notification_request import CreateScalingNotificationRequest
from huaweicloudsdkas.v1.model.create_scaling_notification_response import CreateScalingNotificationResponse
from huaweicloudsdkas.v1.model.create_scaling_policy_option import CreateScalingPolicyOption
from huaweicloudsdkas.v1.model.create_scaling_policy_request import CreateScalingPolicyRequest
from huaweicloudsdkas.v1.model.create_scaling_policy_response import CreateScalingPolicyResponse
from huaweicloudsdkas.v1.model.create_scaling_policy_v2_option import CreateScalingPolicyV2Option
from huaweicloudsdkas.v1.model.create_scaling_tag_info_request import CreateScalingTagInfoRequest
from huaweicloudsdkas.v1.model.create_scaling_tag_info_response import CreateScalingTagInfoResponse
from huaweicloudsdkas.v1.model.create_scaling_v2_policy_request import CreateScalingV2PolicyRequest
from huaweicloudsdkas.v1.model.create_scaling_v2_policy_response import CreateScalingV2PolicyResponse
from huaweicloudsdkas.v1.model.create_tags_option import CreateTagsOption
from huaweicloudsdkas.v1.model.delete_lifecycle_hook_request import DeleteLifecycleHookRequest
from huaweicloudsdkas.v1.model.delete_lifecycle_hook_response import DeleteLifecycleHookResponse
from huaweicloudsdkas.v1.model.delete_scaling_config_request import DeleteScalingConfigRequest
from huaweicloudsdkas.v1.model.delete_scaling_config_response import DeleteScalingConfigResponse
from huaweicloudsdkas.v1.model.delete_scaling_group_request import DeleteScalingGroupRequest
from huaweicloudsdkas.v1.model.delete_scaling_group_response import DeleteScalingGroupResponse
from huaweicloudsdkas.v1.model.delete_scaling_instance_request import DeleteScalingInstanceRequest
from huaweicloudsdkas.v1.model.delete_scaling_instance_response import DeleteScalingInstanceResponse
from huaweicloudsdkas.v1.model.delete_scaling_notification_request import DeleteScalingNotificationRequest
from huaweicloudsdkas.v1.model.delete_scaling_notification_response import DeleteScalingNotificationResponse
from huaweicloudsdkas.v1.model.delete_scaling_policy_request import DeleteScalingPolicyRequest
from huaweicloudsdkas.v1.model.delete_scaling_policy_response import DeleteScalingPolicyResponse
from huaweicloudsdkas.v1.model.delete_scaling_tag_info_request import DeleteScalingTagInfoRequest
from huaweicloudsdkas.v1.model.delete_scaling_tag_info_response import DeleteScalingTagInfoResponse
from huaweicloudsdkas.v1.model.delete_tags_option import DeleteTagsOption
from huaweicloudsdkas.v1.model.disk_info import DiskInfo
from huaweicloudsdkas.v1.model.disk_result import DiskResult
from huaweicloudsdkas.v1.model.eip_info import EipInfo
from huaweicloudsdkas.v1.model.eip_meta_data import EipMetaData
from huaweicloudsdkas.v1.model.eip_result import EipResult
from huaweicloudsdkas.v1.model.execute_scaling_policy_option import ExecuteScalingPolicyOption
from huaweicloudsdkas.v1.model.execute_scaling_policy_request import ExecuteScalingPolicyRequest
from huaweicloudsdkas.v1.model.execute_scaling_policy_response import ExecuteScalingPolicyResponse
from huaweicloudsdkas.v1.model.instance_config import InstanceConfig
from huaweicloudsdkas.v1.model.instance_config_result import InstanceConfigResult
from huaweicloudsdkas.v1.model.instance_hanging_infos import InstanceHangingInfos
from huaweicloudsdkas.v1.model.ipv6_bandwidth import Ipv6Bandwidth
from huaweicloudsdkas.v1.model.job_records import JobRecords
from huaweicloudsdkas.v1.model.lbaas_listener import LbaasListener
from huaweicloudsdkas.v1.model.lbaas_listeners import LbaasListeners
from huaweicloudsdkas.v1.model.lbaas_listeners_result import LbaasListenersResult
from huaweicloudsdkas.v1.model.lifecycle_hook_list import LifecycleHookList
from huaweicloudsdkas.v1.model.links import Links
from huaweicloudsdkas.v1.model.list_all_scaling_v2_policies_request import ListAllScalingV2PoliciesRequest
from huaweicloudsdkas.v1.model.list_all_scaling_v2_policies_response import ListAllScalingV2PoliciesResponse
from huaweicloudsdkas.v1.model.list_api_versions_request import ListApiVersionsRequest
from huaweicloudsdkas.v1.model.list_api_versions_response import ListApiVersionsResponse
from huaweicloudsdkas.v1.model.list_hook_instances_request import ListHookInstancesRequest
from huaweicloudsdkas.v1.model.list_hook_instances_response import ListHookInstancesResponse
from huaweicloudsdkas.v1.model.list_life_cycle_hooks_request import ListLifeCycleHooksRequest
from huaweicloudsdkas.v1.model.list_life_cycle_hooks_response import ListLifeCycleHooksResponse
from huaweicloudsdkas.v1.model.list_resource_instances_request import ListResourceInstancesRequest
from huaweicloudsdkas.v1.model.list_resource_instances_response import ListResourceInstancesResponse
from huaweicloudsdkas.v1.model.list_scaling_activity_logs_request import ListScalingActivityLogsRequest
from huaweicloudsdkas.v1.model.list_scaling_activity_logs_response import ListScalingActivityLogsResponse
from huaweicloudsdkas.v1.model.list_scaling_activity_v2_logs_request import ListScalingActivityV2LogsRequest
from huaweicloudsdkas.v1.model.list_scaling_activity_v2_logs_response import ListScalingActivityV2LogsResponse
from huaweicloudsdkas.v1.model.list_scaling_configs_request import ListScalingConfigsRequest
from huaweicloudsdkas.v1.model.list_scaling_configs_response import ListScalingConfigsResponse
from huaweicloudsdkas.v1.model.list_scaling_groups_request import ListScalingGroupsRequest
from huaweicloudsdkas.v1.model.list_scaling_groups_response import ListScalingGroupsResponse
from huaweicloudsdkas.v1.model.list_scaling_instances_request import ListScalingInstancesRequest
from huaweicloudsdkas.v1.model.list_scaling_instances_response import ListScalingInstancesResponse
from huaweicloudsdkas.v1.model.list_scaling_notifications_request import ListScalingNotificationsRequest
from huaweicloudsdkas.v1.model.list_scaling_notifications_response import ListScalingNotificationsResponse
from huaweicloudsdkas.v1.model.list_scaling_policies_request import ListScalingPoliciesRequest
from huaweicloudsdkas.v1.model.list_scaling_policies_response import ListScalingPoliciesResponse
from huaweicloudsdkas.v1.model.list_scaling_policy_execute_logs_request import ListScalingPolicyExecuteLogsRequest
from huaweicloudsdkas.v1.model.list_scaling_policy_execute_logs_response import ListScalingPolicyExecuteLogsResponse
from huaweicloudsdkas.v1.model.list_scaling_tag_infos_by_resource_id_request import ListScalingTagInfosByResourceIdRequest
from huaweicloudsdkas.v1.model.list_scaling_tag_infos_by_resource_id_response import ListScalingTagInfosByResourceIdResponse
from huaweicloudsdkas.v1.model.list_scaling_tag_infos_by_tenant_id_request import ListScalingTagInfosByTenantIdRequest
from huaweicloudsdkas.v1.model.list_scaling_tag_infos_by_tenant_id_response import ListScalingTagInfosByTenantIdResponse
from huaweicloudsdkas.v1.model.list_scaling_v2_policies_request import ListScalingV2PoliciesRequest
from huaweicloudsdkas.v1.model.list_scaling_v2_policies_response import ListScalingV2PoliciesResponse
from huaweicloudsdkas.v1.model.matches import Matches
from huaweicloudsdkas.v1.model.meta_data import MetaData
from huaweicloudsdkas.v1.model.modify_lb import ModifyLb
from huaweicloudsdkas.v1.model.networks import Networks
from huaweicloudsdkas.v1.model.networks_result import NetworksResult
from huaweicloudsdkas.v1.model.pause_scaling_group_option import PauseScalingGroupOption
from huaweicloudsdkas.v1.model.pause_scaling_group_request import PauseScalingGroupRequest
from huaweicloudsdkas.v1.model.pause_scaling_group_response import PauseScalingGroupResponse
from huaweicloudsdkas.v1.model.pause_scaling_policy_option import PauseScalingPolicyOption
from huaweicloudsdkas.v1.model.pause_scaling_policy_request import PauseScalingPolicyRequest
from huaweicloudsdkas.v1.model.pause_scaling_policy_response import PauseScalingPolicyResponse
from huaweicloudsdkas.v1.model.personality_info import PersonalityInfo
from huaweicloudsdkas.v1.model.personality_result import PersonalityResult
from huaweicloudsdkas.v1.model.policy_instance_quotas import PolicyInstanceQuotas
from huaweicloudsdkas.v1.model.policy_instance_resources import PolicyInstanceResources
from huaweicloudsdkas.v1.model.public_ip import PublicIp
from huaweicloudsdkas.v1.model.publicip_result import PublicipResult
from huaweicloudsdkas.v1.model.query_tags_option import QueryTagsOption
from huaweicloudsdkas.v1.model.resource_tags import ResourceTags
from huaweicloudsdkas.v1.model.resources import Resources
from huaweicloudsdkas.v1.model.resume_scaling_group_option import ResumeScalingGroupOption
from huaweicloudsdkas.v1.model.resume_scaling_group_request import ResumeScalingGroupRequest
from huaweicloudsdkas.v1.model.resume_scaling_group_response import ResumeScalingGroupResponse
from huaweicloudsdkas.v1.model.resume_scaling_policy_option import ResumeScalingPolicyOption
from huaweicloudsdkas.v1.model.resume_scaling_policy_request import ResumeScalingPolicyRequest
from huaweicloudsdkas.v1.model.resume_scaling_policy_response import ResumeScalingPolicyResponse
from huaweicloudsdkas.v1.model.scaling_activity_log_list import ScalingActivityLogList
from huaweicloudsdkas.v1.model.scaling_activity_log_v2 import ScalingActivityLogV2
from huaweicloudsdkas.v1.model.scaling_all_policy_detail import ScalingAllPolicyDetail
from huaweicloudsdkas.v1.model.scaling_configuration import ScalingConfiguration
from huaweicloudsdkas.v1.model.scaling_group_instance import ScalingGroupInstance
from huaweicloudsdkas.v1.model.scaling_groups import ScalingGroups
from huaweicloudsdkas.v1.model.scaling_instance import ScalingInstance
from huaweicloudsdkas.v1.model.scaling_policies_v2 import ScalingPoliciesV2
from huaweicloudsdkas.v1.model.scaling_policy_action_v1 import ScalingPolicyActionV1
from huaweicloudsdkas.v1.model.scaling_policy_action_v2 import ScalingPolicyActionV2
from huaweicloudsdkas.v1.model.scaling_policy_execute_log_list import ScalingPolicyExecuteLogList
from huaweicloudsdkas.v1.model.scaling_policy_v2_meta_data import ScalingPolicyV2MetaData
from huaweicloudsdkas.v1.model.scaling_v1_policy_detail import ScalingV1PolicyDetail
from huaweicloudsdkas.v1.model.scaling_v2_policy_detail import ScalingV2PolicyDetail
from huaweicloudsdkas.v1.model.scheduled_policy import ScheduledPolicy
from huaweicloudsdkas.v1.model.security_group import SecurityGroup
from huaweicloudsdkas.v1.model.security_groups import SecurityGroups
from huaweicloudsdkas.v1.model.security_groups_result import SecurityGroupsResult
from huaweicloudsdkas.v1.model.show_api_version_request import ShowApiVersionRequest
from huaweicloudsdkas.v1.model.show_api_version_response import ShowApiVersionResponse
from huaweicloudsdkas.v1.model.show_life_cycle_hook_request import ShowLifeCycleHookRequest
from huaweicloudsdkas.v1.model.show_life_cycle_hook_response import ShowLifeCycleHookResponse
from huaweicloudsdkas.v1.model.show_policy_and_instance_quota_request import ShowPolicyAndInstanceQuotaRequest
from huaweicloudsdkas.v1.model.show_policy_and_instance_quota_response import ShowPolicyAndInstanceQuotaResponse
from huaweicloudsdkas.v1.model.show_resource_quota_request import ShowResourceQuotaRequest
from huaweicloudsdkas.v1.model.show_resource_quota_response import ShowResourceQuotaResponse
from huaweicloudsdkas.v1.model.show_scaling_config_request import ShowScalingConfigRequest
from huaweicloudsdkas.v1.model.show_scaling_config_response import ShowScalingConfigResponse
from huaweicloudsdkas.v1.model.show_scaling_group_request import ShowScalingGroupRequest
from huaweicloudsdkas.v1.model.show_scaling_group_response import ShowScalingGroupResponse
from huaweicloudsdkas.v1.model.show_scaling_policy_request import ShowScalingPolicyRequest
from huaweicloudsdkas.v1.model.show_scaling_policy_response import ShowScalingPolicyResponse
from huaweicloudsdkas.v1.model.show_scaling_v2_policy_request import ShowScalingV2PolicyRequest
from huaweicloudsdkas.v1.model.show_scaling_v2_policy_response import ShowScalingV2PolicyResponse
from huaweicloudsdkas.v1.model.tags_multi_value import TagsMultiValue
from huaweicloudsdkas.v1.model.tags_single_value import TagsSingleValue
from huaweicloudsdkas.v1.model.topics import Topics
from huaweicloudsdkas.v1.model.update_life_cycle_hook_option import UpdateLifeCycleHookOption
from huaweicloudsdkas.v1.model.update_life_cycle_hook_request import UpdateLifeCycleHookRequest
from huaweicloudsdkas.v1.model.update_life_cycle_hook_response import UpdateLifeCycleHookResponse
from huaweicloudsdkas.v1.model.update_scaling_group_option import UpdateScalingGroupOption
from huaweicloudsdkas.v1.model.update_scaling_group_request import UpdateScalingGroupRequest
from huaweicloudsdkas.v1.model.update_scaling_group_response import UpdateScalingGroupResponse
from huaweicloudsdkas.v1.model.update_scaling_policy_option import UpdateScalingPolicyOption
from huaweicloudsdkas.v1.model.update_scaling_policy_request import UpdateScalingPolicyRequest
from huaweicloudsdkas.v1.model.update_scaling_policy_response import UpdateScalingPolicyResponse
from huaweicloudsdkas.v1.model.update_scaling_v2_policy_option import UpdateScalingV2PolicyOption
from huaweicloudsdkas.v1.model.update_scaling_v2_policy_request import UpdateScalingV2PolicyRequest
from huaweicloudsdkas.v1.model.update_scaling_v2_policy_response import UpdateScalingV2PolicyResponse
from huaweicloudsdkas.v1.model.version_info import VersionInfo
from huaweicloudsdkas.v1.model.vm_meta_data import VmMetaData
