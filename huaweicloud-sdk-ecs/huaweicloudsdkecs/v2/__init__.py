# coding: utf-8

from __future__ import absolute_import

# import EcsClient
from huaweicloudsdkecs.v2.ecs_client import EcsClient
from huaweicloudsdkecs.v2.ecs_async_client import EcsAsyncClient
# import models into sdk package
from huaweicloudsdkecs.v2.model.add_server_group_member_request import AddServerGroupMemberRequest
from huaweicloudsdkecs.v2.model.add_server_group_member_request_body import AddServerGroupMemberRequestBody
from huaweicloudsdkecs.v2.model.add_server_group_member_response import AddServerGroupMemberResponse
from huaweicloudsdkecs.v2.model.associate_server_virtual_ip_option import AssociateServerVirtualIpOption
from huaweicloudsdkecs.v2.model.associate_server_virtual_ip_request import AssociateServerVirtualIpRequest
from huaweicloudsdkecs.v2.model.associate_server_virtual_ip_request_body import AssociateServerVirtualIpRequestBody
from huaweicloudsdkecs.v2.model.associate_server_virtual_ip_response import AssociateServerVirtualIpResponse
from huaweicloudsdkecs.v2.model.attach_server_volume_option import AttachServerVolumeOption
from huaweicloudsdkecs.v2.model.attach_server_volume_request import AttachServerVolumeRequest
from huaweicloudsdkecs.v2.model.attach_server_volume_request_body import AttachServerVolumeRequestBody
from huaweicloudsdkecs.v2.model.attach_server_volume_response import AttachServerVolumeResponse
from huaweicloudsdkecs.v2.model.batch_add_server_nic_option import BatchAddServerNicOption
from huaweicloudsdkecs.v2.model.batch_add_server_nics_request import BatchAddServerNicsRequest
from huaweicloudsdkecs.v2.model.batch_add_server_nics_request_body import BatchAddServerNicsRequestBody
from huaweicloudsdkecs.v2.model.batch_add_server_nics_response import BatchAddServerNicsResponse
from huaweicloudsdkecs.v2.model.batch_attach_sharable_volumes_option import BatchAttachSharableVolumesOption
from huaweicloudsdkecs.v2.model.batch_attach_sharable_volumes_request import BatchAttachSharableVolumesRequest
from huaweicloudsdkecs.v2.model.batch_attach_sharable_volumes_request_body import BatchAttachSharableVolumesRequestBody
from huaweicloudsdkecs.v2.model.batch_attach_sharable_volumes_response import BatchAttachSharableVolumesResponse
from huaweicloudsdkecs.v2.model.batch_create_server_tags_request import BatchCreateServerTagsRequest
from huaweicloudsdkecs.v2.model.batch_create_server_tags_request_body import BatchCreateServerTagsRequestBody
from huaweicloudsdkecs.v2.model.batch_create_server_tags_response import BatchCreateServerTagsResponse
from huaweicloudsdkecs.v2.model.batch_delete_server_nic_option import BatchDeleteServerNicOption
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_request import BatchDeleteServerNicsRequest
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_request_body import BatchDeleteServerNicsRequestBody
from huaweicloudsdkecs.v2.model.batch_delete_server_nics_response import BatchDeleteServerNicsResponse
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_request import BatchDeleteServerTagsRequest
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_request_body import BatchDeleteServerTagsRequestBody
from huaweicloudsdkecs.v2.model.batch_delete_server_tags_response import BatchDeleteServerTagsResponse
from huaweicloudsdkecs.v2.model.batch_reboot_servers_request import BatchRebootServersRequest
from huaweicloudsdkecs.v2.model.batch_reboot_servers_request_body import BatchRebootServersRequestBody
from huaweicloudsdkecs.v2.model.batch_reboot_servers_response import BatchRebootServersResponse
from huaweicloudsdkecs.v2.model.batch_reboot_severs_option import BatchRebootSeversOption
from huaweicloudsdkecs.v2.model.batch_reset_servers_password_request import BatchResetServersPasswordRequest
from huaweicloudsdkecs.v2.model.batch_reset_servers_password_request_body import BatchResetServersPasswordRequestBody
from huaweicloudsdkecs.v2.model.batch_reset_servers_password_response import BatchResetServersPasswordResponse
from huaweicloudsdkecs.v2.model.batch_start_servers_option import BatchStartServersOption
from huaweicloudsdkecs.v2.model.batch_start_servers_request import BatchStartServersRequest
from huaweicloudsdkecs.v2.model.batch_start_servers_request_body import BatchStartServersRequestBody
from huaweicloudsdkecs.v2.model.batch_start_servers_response import BatchStartServersResponse
from huaweicloudsdkecs.v2.model.batch_stop_servers_option import BatchStopServersOption
from huaweicloudsdkecs.v2.model.batch_stop_servers_request import BatchStopServersRequest
from huaweicloudsdkecs.v2.model.batch_stop_servers_request_body import BatchStopServersRequestBody
from huaweicloudsdkecs.v2.model.batch_stop_servers_response import BatchStopServersResponse
from huaweicloudsdkecs.v2.model.batch_update_servers_name_request import BatchUpdateServersNameRequest
from huaweicloudsdkecs.v2.model.batch_update_servers_name_request_body import BatchUpdateServersNameRequestBody
from huaweicloudsdkecs.v2.model.batch_update_servers_name_response import BatchUpdateServersNameResponse
from huaweicloudsdkecs.v2.model.block_device_attachable_quantity import BlockDeviceAttachableQuantity
from huaweicloudsdkecs.v2.model.change_server_os_with_cloud_init_option import ChangeServerOsWithCloudInitOption
from huaweicloudsdkecs.v2.model.change_server_os_with_cloud_init_request import ChangeServerOsWithCloudInitRequest
from huaweicloudsdkecs.v2.model.change_server_os_with_cloud_init_request_body import ChangeServerOsWithCloudInitRequestBody
from huaweicloudsdkecs.v2.model.change_server_os_with_cloud_init_response import ChangeServerOsWithCloudInitResponse
from huaweicloudsdkecs.v2.model.change_server_os_without_cloud_init_option import ChangeServerOsWithoutCloudInitOption
from huaweicloudsdkecs.v2.model.change_server_os_without_cloud_init_request import ChangeServerOsWithoutCloudInitRequest
from huaweicloudsdkecs.v2.model.change_server_os_without_cloud_init_request_body import ChangeServerOsWithoutCloudInitRequestBody
from huaweicloudsdkecs.v2.model.change_server_os_without_cloud_init_response import ChangeServerOsWithoutCloudInitResponse
from huaweicloudsdkecs.v2.model.change_severs_os_metadata import ChangeSeversOsMetadata
from huaweicloudsdkecs.v2.model.cpu_options import CpuOptions
from huaweicloudsdkecs.v2.model.create_post_paid_servers_request import CreatePostPaidServersRequest
from huaweicloudsdkecs.v2.model.create_post_paid_servers_request_body import CreatePostPaidServersRequestBody
from huaweicloudsdkecs.v2.model.create_post_paid_servers_response import CreatePostPaidServersResponse
from huaweicloudsdkecs.v2.model.create_server_group_option import CreateServerGroupOption
from huaweicloudsdkecs.v2.model.create_server_group_request import CreateServerGroupRequest
from huaweicloudsdkecs.v2.model.create_server_group_request_body import CreateServerGroupRequestBody
from huaweicloudsdkecs.v2.model.create_server_group_response import CreateServerGroupResponse
from huaweicloudsdkecs.v2.model.create_server_group_result import CreateServerGroupResult
from huaweicloudsdkecs.v2.model.create_servers_request import CreateServersRequest
from huaweicloudsdkecs.v2.model.create_servers_request_body import CreateServersRequestBody
from huaweicloudsdkecs.v2.model.create_servers_response import CreateServersResponse
from huaweicloudsdkecs.v2.model.delete_server_group_member_request import DeleteServerGroupMemberRequest
from huaweicloudsdkecs.v2.model.delete_server_group_member_request_body import DeleteServerGroupMemberRequestBody
from huaweicloudsdkecs.v2.model.delete_server_group_member_response import DeleteServerGroupMemberResponse
from huaweicloudsdkecs.v2.model.delete_server_group_request import DeleteServerGroupRequest
from huaweicloudsdkecs.v2.model.delete_server_group_response import DeleteServerGroupResponse
from huaweicloudsdkecs.v2.model.delete_server_metadata_request import DeleteServerMetadataRequest
from huaweicloudsdkecs.v2.model.delete_server_metadata_response import DeleteServerMetadataResponse
from huaweicloudsdkecs.v2.model.delete_server_password_request import DeleteServerPasswordRequest
from huaweicloudsdkecs.v2.model.delete_server_password_response import DeleteServerPasswordResponse
from huaweicloudsdkecs.v2.model.delete_servers_request import DeleteServersRequest
from huaweicloudsdkecs.v2.model.delete_servers_request_body import DeleteServersRequestBody
from huaweicloudsdkecs.v2.model.delete_servers_response import DeleteServersResponse
from huaweicloudsdkecs.v2.model.detach_server_volume_request import DetachServerVolumeRequest
from huaweicloudsdkecs.v2.model.detach_server_volume_response import DetachServerVolumeResponse
from huaweicloudsdkecs.v2.model.disassociate_server_virtual_ip_option import DisassociateServerVirtualIpOption
from huaweicloudsdkecs.v2.model.disassociate_server_virtual_ip_request import DisassociateServerVirtualIpRequest
from huaweicloudsdkecs.v2.model.disassociate_server_virtual_ip_request_body import DisassociateServerVirtualIpRequestBody
from huaweicloudsdkecs.v2.model.disassociate_server_virtual_ip_response import DisassociateServerVirtualIpResponse
from huaweicloudsdkecs.v2.model.flavor import Flavor
from huaweicloudsdkecs.v2.model.flavor_extra_spec import FlavorExtraSpec
from huaweicloudsdkecs.v2.model.flavor_link import FlavorLink
from huaweicloudsdkecs.v2.model.get_server_remote_console_option import GetServerRemoteConsoleOption
from huaweicloudsdkecs.v2.model.hypervisor import Hypervisor
from huaweicloudsdkecs.v2.model.interface_attachable_quantity import InterfaceAttachableQuantity
from huaweicloudsdkecs.v2.model.interface_attachment import InterfaceAttachment
from huaweicloudsdkecs.v2.model.ipv6_bandwidth import Ipv6Bandwidth
from huaweicloudsdkecs.v2.model.job_entities import JobEntities
from huaweicloudsdkecs.v2.model.link import Link
from huaweicloudsdkecs.v2.model.list_flavors_request import ListFlavorsRequest
from huaweicloudsdkecs.v2.model.list_flavors_response import ListFlavorsResponse
from huaweicloudsdkecs.v2.model.list_resize_flavors_request import ListResizeFlavorsRequest
from huaweicloudsdkecs.v2.model.list_resize_flavors_response import ListResizeFlavorsResponse
from huaweicloudsdkecs.v2.model.list_resize_flavors_result import ListResizeFlavorsResult
from huaweicloudsdkecs.v2.model.list_server_block_devices_request import ListServerBlockDevicesRequest
from huaweicloudsdkecs.v2.model.list_server_block_devices_response import ListServerBlockDevicesResponse
from huaweicloudsdkecs.v2.model.list_server_groups_page_info_result import ListServerGroupsPageInfoResult
from huaweicloudsdkecs.v2.model.list_server_groups_request import ListServerGroupsRequest
from huaweicloudsdkecs.v2.model.list_server_groups_response import ListServerGroupsResponse
from huaweicloudsdkecs.v2.model.list_server_groups_result import ListServerGroupsResult
from huaweicloudsdkecs.v2.model.list_server_interfaces_request import ListServerInterfacesRequest
from huaweicloudsdkecs.v2.model.list_server_interfaces_response import ListServerInterfacesResponse
from huaweicloudsdkecs.v2.model.list_server_tags_request import ListServerTagsRequest
from huaweicloudsdkecs.v2.model.list_server_tags_response import ListServerTagsResponse
from huaweicloudsdkecs.v2.model.list_servers_details_request import ListServersDetailsRequest
from huaweicloudsdkecs.v2.model.list_servers_details_response import ListServersDetailsResponse
from huaweicloudsdkecs.v2.model.migrate_server_option import MigrateServerOption
from huaweicloudsdkecs.v2.model.migrate_server_request import MigrateServerRequest
from huaweicloudsdkecs.v2.model.migrate_server_request_body import MigrateServerRequestBody
from huaweicloudsdkecs.v2.model.migrate_server_response import MigrateServerResponse
from huaweicloudsdkecs.v2.model.nova_add_security_group_option import NovaAddSecurityGroupOption
from huaweicloudsdkecs.v2.model.nova_associate_security_group_request import NovaAssociateSecurityGroupRequest
from huaweicloudsdkecs.v2.model.nova_associate_security_group_request_body import NovaAssociateSecurityGroupRequestBody
from huaweicloudsdkecs.v2.model.nova_associate_security_group_response import NovaAssociateSecurityGroupResponse
from huaweicloudsdkecs.v2.model.nova_availability_zone import NovaAvailabilityZone
from huaweicloudsdkecs.v2.model.nova_availability_zone_state import NovaAvailabilityZoneState
from huaweicloudsdkecs.v2.model.nova_create_keypair_option import NovaCreateKeypairOption
from huaweicloudsdkecs.v2.model.nova_create_keypair_request import NovaCreateKeypairRequest
from huaweicloudsdkecs.v2.model.nova_create_keypair_request_body import NovaCreateKeypairRequestBody
from huaweicloudsdkecs.v2.model.nova_create_keypair_response import NovaCreateKeypairResponse
from huaweicloudsdkecs.v2.model.nova_create_servers_option import NovaCreateServersOption
from huaweicloudsdkecs.v2.model.nova_create_servers_request import NovaCreateServersRequest
from huaweicloudsdkecs.v2.model.nova_create_servers_request_body import NovaCreateServersRequestBody
from huaweicloudsdkecs.v2.model.nova_create_servers_response import NovaCreateServersResponse
from huaweicloudsdkecs.v2.model.nova_create_servers_result import NovaCreateServersResult
from huaweicloudsdkecs.v2.model.nova_create_servers_scheduler_hint import NovaCreateServersSchedulerHint
from huaweicloudsdkecs.v2.model.nova_delete_keypair_request import NovaDeleteKeypairRequest
from huaweicloudsdkecs.v2.model.nova_delete_keypair_response import NovaDeleteKeypairResponse
from huaweicloudsdkecs.v2.model.nova_delete_server_request import NovaDeleteServerRequest
from huaweicloudsdkecs.v2.model.nova_delete_server_response import NovaDeleteServerResponse
from huaweicloudsdkecs.v2.model.nova_disassociate_security_group_request import NovaDisassociateSecurityGroupRequest
from huaweicloudsdkecs.v2.model.nova_disassociate_security_group_request_body import NovaDisassociateSecurityGroupRequestBody
from huaweicloudsdkecs.v2.model.nova_disassociate_security_group_response import NovaDisassociateSecurityGroupResponse
from huaweicloudsdkecs.v2.model.nova_keypair import NovaKeypair
from huaweicloudsdkecs.v2.model.nova_keypair_detail import NovaKeypairDetail
from huaweicloudsdkecs.v2.model.nova_link import NovaLink
from huaweicloudsdkecs.v2.model.nova_list_availability_zones_request import NovaListAvailabilityZonesRequest
from huaweicloudsdkecs.v2.model.nova_list_availability_zones_response import NovaListAvailabilityZonesResponse
from huaweicloudsdkecs.v2.model.nova_list_keypairs_request import NovaListKeypairsRequest
from huaweicloudsdkecs.v2.model.nova_list_keypairs_response import NovaListKeypairsResponse
from huaweicloudsdkecs.v2.model.nova_list_keypairs_result import NovaListKeypairsResult
from huaweicloudsdkecs.v2.model.nova_list_server_security_groups_request import NovaListServerSecurityGroupsRequest
from huaweicloudsdkecs.v2.model.nova_list_server_security_groups_response import NovaListServerSecurityGroupsResponse
from huaweicloudsdkecs.v2.model.nova_list_servers_details_request import NovaListServersDetailsRequest
from huaweicloudsdkecs.v2.model.nova_list_servers_details_response import NovaListServersDetailsResponse
from huaweicloudsdkecs.v2.model.nova_network import NovaNetwork
from huaweicloudsdkecs.v2.model.nova_remove_security_group_option import NovaRemoveSecurityGroupOption
from huaweicloudsdkecs.v2.model.nova_security_group import NovaSecurityGroup
from huaweicloudsdkecs.v2.model.nova_security_group_common_group import NovaSecurityGroupCommonGroup
from huaweicloudsdkecs.v2.model.nova_security_group_common_ip_range import NovaSecurityGroupCommonIpRange
from huaweicloudsdkecs.v2.model.nova_security_group_common_rule import NovaSecurityGroupCommonRule
from huaweicloudsdkecs.v2.model.nova_server import NovaServer
from huaweicloudsdkecs.v2.model.nova_server_block_device_mapping import NovaServerBlockDeviceMapping
from huaweicloudsdkecs.v2.model.nova_server_fault import NovaServerFault
from huaweicloudsdkecs.v2.model.nova_server_flavor import NovaServerFlavor
from huaweicloudsdkecs.v2.model.nova_server_image import NovaServerImage
from huaweicloudsdkecs.v2.model.nova_server_network import NovaServerNetwork
from huaweicloudsdkecs.v2.model.nova_server_security_group import NovaServerSecurityGroup
from huaweicloudsdkecs.v2.model.nova_server_volume import NovaServerVolume
from huaweicloudsdkecs.v2.model.nova_show_keypair_request import NovaShowKeypairRequest
from huaweicloudsdkecs.v2.model.nova_show_keypair_response import NovaShowKeypairResponse
from huaweicloudsdkecs.v2.model.nova_show_server_request import NovaShowServerRequest
from huaweicloudsdkecs.v2.model.nova_show_server_response import NovaShowServerResponse
from huaweicloudsdkecs.v2.model.nova_simple_keypair import NovaSimpleKeypair
from huaweicloudsdkecs.v2.model.page_link import PageLink
from huaweicloudsdkecs.v2.model.post_paid_server import PostPaidServer
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume import PostPaidServerDataVolume
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume_extend_param import PostPaidServerDataVolumeExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_data_volume_metadata import PostPaidServerDataVolumeMetadata
from huaweicloudsdkecs.v2.model.post_paid_server_eip import PostPaidServerEip
from huaweicloudsdkecs.v2.model.post_paid_server_eip_bandwidth import PostPaidServerEipBandwidth
from huaweicloudsdkecs.v2.model.post_paid_server_eip_extend_param import PostPaidServerEipExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_extend_param import PostPaidServerExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_ipv6_bandwidth import PostPaidServerIpv6Bandwidth
from huaweicloudsdkecs.v2.model.post_paid_server_nic import PostPaidServerNic
from huaweicloudsdkecs.v2.model.post_paid_server_publicip import PostPaidServerPublicip
from huaweicloudsdkecs.v2.model.post_paid_server_root_volume import PostPaidServerRootVolume
from huaweicloudsdkecs.v2.model.post_paid_server_root_volume_extend_param import PostPaidServerRootVolumeExtendParam
from huaweicloudsdkecs.v2.model.post_paid_server_scheduler_hints import PostPaidServerSchedulerHints
from huaweicloudsdkecs.v2.model.post_paid_server_security_group import PostPaidServerSecurityGroup
from huaweicloudsdkecs.v2.model.post_paid_server_tag import PostPaidServerTag
from huaweicloudsdkecs.v2.model.pre_paid_server import PrePaidServer
from huaweicloudsdkecs.v2.model.pre_paid_server_data_volume import PrePaidServerDataVolume
from huaweicloudsdkecs.v2.model.pre_paid_server_data_volume_extend_param import PrePaidServerDataVolumeExtendParam
from huaweicloudsdkecs.v2.model.pre_paid_server_data_volume_metadata import PrePaidServerDataVolumeMetadata
from huaweicloudsdkecs.v2.model.pre_paid_server_eip import PrePaidServerEip
from huaweicloudsdkecs.v2.model.pre_paid_server_eip_bandwidth import PrePaidServerEipBandwidth
from huaweicloudsdkecs.v2.model.pre_paid_server_eip_extend_param import PrePaidServerEipExtendParam
from huaweicloudsdkecs.v2.model.pre_paid_server_extend_param import PrePaidServerExtendParam
from huaweicloudsdkecs.v2.model.pre_paid_server_ipv6_bandwidth import PrePaidServerIpv6Bandwidth
from huaweicloudsdkecs.v2.model.pre_paid_server_nic import PrePaidServerNic
from huaweicloudsdkecs.v2.model.pre_paid_server_publicip import PrePaidServerPublicip
from huaweicloudsdkecs.v2.model.pre_paid_server_root_volume import PrePaidServerRootVolume
from huaweicloudsdkecs.v2.model.pre_paid_server_root_volume_extend_param import PrePaidServerRootVolumeExtendParam
from huaweicloudsdkecs.v2.model.pre_paid_server_scheduler_hints import PrePaidServerSchedulerHints
from huaweicloudsdkecs.v2.model.pre_paid_server_security_group import PrePaidServerSecurityGroup
from huaweicloudsdkecs.v2.model.pre_paid_server_tag import PrePaidServerTag
from huaweicloudsdkecs.v2.model.project_flavor_limit import ProjectFlavorLimit
from huaweicloudsdkecs.v2.model.project_tag import ProjectTag
from huaweicloudsdkecs.v2.model.register_server_auto_recovery_request import RegisterServerAutoRecoveryRequest
from huaweicloudsdkecs.v2.model.register_server_auto_recovery_request_body import RegisterServerAutoRecoveryRequestBody
from huaweicloudsdkecs.v2.model.register_server_auto_recovery_response import RegisterServerAutoRecoveryResponse
from huaweicloudsdkecs.v2.model.reinstall_server_with_cloud_init_option import ReinstallServerWithCloudInitOption
from huaweicloudsdkecs.v2.model.reinstall_server_with_cloud_init_request import ReinstallServerWithCloudInitRequest
from huaweicloudsdkecs.v2.model.reinstall_server_with_cloud_init_request_body import ReinstallServerWithCloudInitRequestBody
from huaweicloudsdkecs.v2.model.reinstall_server_with_cloud_init_response import ReinstallServerWithCloudInitResponse
from huaweicloudsdkecs.v2.model.reinstall_server_without_cloud_init_option import ReinstallServerWithoutCloudInitOption
from huaweicloudsdkecs.v2.model.reinstall_server_without_cloud_init_request import ReinstallServerWithoutCloudInitRequest
from huaweicloudsdkecs.v2.model.reinstall_server_without_cloud_init_request_body import ReinstallServerWithoutCloudInitRequestBody
from huaweicloudsdkecs.v2.model.reinstall_server_without_cloud_init_response import ReinstallServerWithoutCloudInitResponse
from huaweicloudsdkecs.v2.model.reinstall_sever_metadata import ReinstallSeverMetadata
from huaweicloudsdkecs.v2.model.reset_server_password_option import ResetServerPasswordOption
from huaweicloudsdkecs.v2.model.reset_server_password_request import ResetServerPasswordRequest
from huaweicloudsdkecs.v2.model.reset_server_password_request_body import ResetServerPasswordRequestBody
from huaweicloudsdkecs.v2.model.reset_server_password_response import ResetServerPasswordResponse
from huaweicloudsdkecs.v2.model.resize_post_paid_server_option import ResizePostPaidServerOption
from huaweicloudsdkecs.v2.model.resize_post_paid_server_request import ResizePostPaidServerRequest
from huaweicloudsdkecs.v2.model.resize_post_paid_server_request_body import ResizePostPaidServerRequestBody
from huaweicloudsdkecs.v2.model.resize_post_paid_server_response import ResizePostPaidServerResponse
from huaweicloudsdkecs.v2.model.resize_pre_paid_server_option import ResizePrePaidServerOption
from huaweicloudsdkecs.v2.model.resize_server_extend_param import ResizeServerExtendParam
from huaweicloudsdkecs.v2.model.resize_server_request import ResizeServerRequest
from huaweicloudsdkecs.v2.model.resize_server_request_body import ResizeServerRequestBody
from huaweicloudsdkecs.v2.model.resize_server_response import ResizeServerResponse
from huaweicloudsdkecs.v2.model.server_address import ServerAddress
from huaweicloudsdkecs.v2.model.server_attachable_quantity import ServerAttachableQuantity
from huaweicloudsdkecs.v2.model.server_block_device import ServerBlockDevice
from huaweicloudsdkecs.v2.model.server_detail import ServerDetail
from huaweicloudsdkecs.v2.model.server_extend_volume_attachment import ServerExtendVolumeAttachment
from huaweicloudsdkecs.v2.model.server_fault import ServerFault
from huaweicloudsdkecs.v2.model.server_flavor import ServerFlavor
from huaweicloudsdkecs.v2.model.server_group_member import ServerGroupMember
from huaweicloudsdkecs.v2.model.server_id import ServerId
from huaweicloudsdkecs.v2.model.server_image import ServerImage
from huaweicloudsdkecs.v2.model.server_interface_fixed_ip import ServerInterfaceFixedIp
from huaweicloudsdkecs.v2.model.server_limits import ServerLimits
from huaweicloudsdkecs.v2.model.server_nic_security_group import ServerNicSecurityGroup
from huaweicloudsdkecs.v2.model.server_remote_console import ServerRemoteConsole
from huaweicloudsdkecs.v2.model.server_scheduler_hints import ServerSchedulerHints
from huaweicloudsdkecs.v2.model.server_security_group import ServerSecurityGroup
from huaweicloudsdkecs.v2.model.server_system_tag import ServerSystemTag
from huaweicloudsdkecs.v2.model.server_tag import ServerTag
from huaweicloudsdkecs.v2.model.show_job_request import ShowJobRequest
from huaweicloudsdkecs.v2.model.show_job_response import ShowJobResponse
from huaweicloudsdkecs.v2.model.show_reset_password_flag_request import ShowResetPasswordFlagRequest
from huaweicloudsdkecs.v2.model.show_reset_password_flag_response import ShowResetPasswordFlagResponse
from huaweicloudsdkecs.v2.model.show_server_auto_recovery_request import ShowServerAutoRecoveryRequest
from huaweicloudsdkecs.v2.model.show_server_auto_recovery_response import ShowServerAutoRecoveryResponse
from huaweicloudsdkecs.v2.model.show_server_block_device_request import ShowServerBlockDeviceRequest
from huaweicloudsdkecs.v2.model.show_server_block_device_response import ShowServerBlockDeviceResponse
from huaweicloudsdkecs.v2.model.show_server_group_request import ShowServerGroupRequest
from huaweicloudsdkecs.v2.model.show_server_group_response import ShowServerGroupResponse
from huaweicloudsdkecs.v2.model.show_server_group_result import ShowServerGroupResult
from huaweicloudsdkecs.v2.model.show_server_limits_request import ShowServerLimitsRequest
from huaweicloudsdkecs.v2.model.show_server_limits_response import ShowServerLimitsResponse
from huaweicloudsdkecs.v2.model.show_server_password_request import ShowServerPasswordRequest
from huaweicloudsdkecs.v2.model.show_server_password_response import ShowServerPasswordResponse
from huaweicloudsdkecs.v2.model.show_server_remote_console_request import ShowServerRemoteConsoleRequest
from huaweicloudsdkecs.v2.model.show_server_remote_console_request_body import ShowServerRemoteConsoleRequestBody
from huaweicloudsdkecs.v2.model.show_server_remote_console_response import ShowServerRemoteConsoleResponse
from huaweicloudsdkecs.v2.model.show_server_request import ShowServerRequest
from huaweicloudsdkecs.v2.model.show_server_response import ShowServerResponse
from huaweicloudsdkecs.v2.model.show_server_tags_request import ShowServerTagsRequest
from huaweicloudsdkecs.v2.model.show_server_tags_response import ShowServerTagsResponse
from huaweicloudsdkecs.v2.model.simple_flavor import SimpleFlavor
from huaweicloudsdkecs.v2.model.sub_job import SubJob
from huaweicloudsdkecs.v2.model.sub_job_entities import SubJobEntities
from huaweicloudsdkecs.v2.model.update_server_address import UpdateServerAddress
from huaweicloudsdkecs.v2.model.update_server_auto_terminate_time_request import UpdateServerAutoTerminateTimeRequest
from huaweicloudsdkecs.v2.model.update_server_auto_terminate_time_request_body import UpdateServerAutoTerminateTimeRequestBody
from huaweicloudsdkecs.v2.model.update_server_auto_terminate_time_response import UpdateServerAutoTerminateTimeResponse
from huaweicloudsdkecs.v2.model.update_server_metadata_request import UpdateServerMetadataRequest
from huaweicloudsdkecs.v2.model.update_server_metadata_request_body import UpdateServerMetadataRequestBody
from huaweicloudsdkecs.v2.model.update_server_metadata_response import UpdateServerMetadataResponse
from huaweicloudsdkecs.v2.model.update_server_option import UpdateServerOption
from huaweicloudsdkecs.v2.model.update_server_request import UpdateServerRequest
from huaweicloudsdkecs.v2.model.update_server_request_body import UpdateServerRequestBody
from huaweicloudsdkecs.v2.model.update_server_response import UpdateServerResponse
from huaweicloudsdkecs.v2.model.update_server_result import UpdateServerResult

