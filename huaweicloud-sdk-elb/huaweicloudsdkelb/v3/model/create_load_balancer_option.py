# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadBalancerOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'vip_address': 'str',
        'vip_subnet_cidr_id': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'provider': 'str',
        'l4_flavor_id': 'str',
        'project_id': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'admin_state_up': 'bool',
        'l7_flavor_id': 'str',
        'billing_info': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'publicip_ids': 'list[str]',
        'publicip': 'CreateLoadBalancerPublicIpOption',
        'elb_virsubnet_ids': 'list[str]',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'bool',
        'prepaid_options': 'PrepaidCreateOption',
        'autoscaling': 'CreateLoadbalancerAutoscalingOption'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'provider': 'provider',
        'l4_flavor_id': 'l4_flavor_id',
        'project_id': 'project_id',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up',
        'l7_flavor_id': 'l7_flavor_id',
        'billing_info': 'billing_info',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'publicip_ids': 'publicip_ids',
        'publicip': 'publicip',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable',
        'prepaid_options': 'prepaid_options',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, name=None, description=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_virsubnet_id=None, provider=None, l4_flavor_id=None, project_id=None, guaranteed=None, vpc_id=None, availability_zone_list=None, enterprise_project_id=None, tags=None, admin_state_up=None, l7_flavor_id=None, billing_info=None, ipv6_bandwidth=None, publicip_ids=None, publicip=None, elb_virsubnet_ids=None, ip_target_enable=None, deletion_protection_enable=None, prepaid_options=None, autoscaling=None):
        """CreateLoadBalancerOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._ipv6_vip_virsubnet_id = None
        self._provider = None
        self._l4_flavor_id = None
        self._project_id = None
        self._guaranteed = None
        self._vpc_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._tags = None
        self._admin_state_up = None
        self._l7_flavor_id = None
        self._billing_info = None
        self._ipv6_bandwidth = None
        self._publicip_ids = None
        self._publicip = None
        self._elb_virsubnet_ids = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self._prepaid_options = None
        self._autoscaling = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if provider is not None:
            self.provider = provider
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if project_id is not None:
            self.project_id = project_id
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if billing_info is not None:
            self.billing_info = billing_info
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        if publicip is not None:
            self.publicip = publicip
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options
        if autoscaling is not None:
            self.autoscaling = autoscaling

    @property
    def name(self):
        """Gets the name of this CreateLoadBalancerOption.

        负载均衡器的名称。

        :return: The name of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadBalancerOption.

        负载均衡器的名称。

        :param name: The name of this CreateLoadBalancerOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateLoadBalancerOption.

        负载均衡器的描述。

        :return: The description of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadBalancerOption.

        负载均衡器的描述。

        :param description: The description of this CreateLoadBalancerOption.
        :type: str
        """
        self._description = description

    @property
    def vip_address(self):
        """Gets the vip_address of this CreateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  使用说明： - 传入vip_address时必须传入vip_subnet_cidr_id。 - 不传入vip_address，但传入vip_subnet_cidr_id，则自动分配IPv4虚拟IP。 - 不传入vip_address，且不传vip_subnet_cidr_id，则不分配虚拟IP，vip_address=null。

        :return: The vip_address of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this CreateLoadBalancerOption.

        负载均衡器的IPv4虚拟IP。该地址必须包含在所在子网的IPv4网段内，且未被占用。  使用说明： - 传入vip_address时必须传入vip_subnet_cidr_id。 - 不传入vip_address，但传入vip_subnet_cidr_id，则自动分配IPv4虚拟IP。 - 不传入vip_address，且不传vip_subnet_cidr_id，则不分配虚拟IP，vip_address=null。

        :param vip_address: The vip_address of this CreateLoadBalancerOption.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        负载均衡器所在子网的IPv4子网ID。若需要创建带IPv4虚拟IP的LB，该字段必须传入。 可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 使用说明： - vpc_id, vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 若同时传入vpc_id和vip_subnet_cidr_id，则vip_subnet_cidr_id对应的子网必须属于vpc_id对应的VPC。

        :return: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        负载均衡器所在子网的IPv4子网ID。若需要创建带IPv4虚拟IP的LB，该字段必须传入。 可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的neutron_subnet_id得到。 使用说明： - vpc_id, vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 若同时传入vpc_id和vip_subnet_cidr_id，则vip_subnet_cidr_id对应的子网必须属于vpc_id对应的VPC。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 需要对应的子网开启IPv6。  [不支持IPv6，请勿使用](tag:dt,dt_test)

        :return: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        双栈类型负载均衡器所在子网的IPv6网络ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。 - 需要对应的子网开启IPv6。  [不支持IPv6，请勿使用](tag:dt,dt_test)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def provider(self):
        """Gets the provider of this CreateLoadBalancerOption.

        负载均衡器的生产者名称。固定为vlb。

        :return: The provider of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateLoadBalancerOption.

        负载均衡器的生产者名称。固定为vlb。

        :param provider: The provider of this CreateLoadBalancerOption.
        :type: str
        """
        self._provider = provider

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this CreateLoadBalancerOption.

        四层Flavor ID。[创建负载均衡器时l4_flavor_id和l7_flavor_id不能都不传](tag:dt,dt_test) [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso) 注意：当l4_flavor_id和l7_flavor_id都不传的时，会选择默认flavor。

        :return: The l4_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this CreateLoadBalancerOption.

        四层Flavor ID。[创建负载均衡器时l4_flavor_id和l7_flavor_id不能都不传](tag:dt,dt_test) [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso) 注意：当l4_flavor_id和l7_flavor_id都不传的时，会选择默认flavor。

        :param l4_flavor_id: The l4_flavor_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :return: The project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :param project_id: The project_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._project_id = project_id

    @property
    def guaranteed(self):
        """Gets the guaranteed of this CreateLoadBalancerOption.

        是否独享型负载均衡器。取值： - true：独享型。 - false：共享型。  当前只支持设置为true，设置为false会返回400 Bad Request 。默认：true。

        :return: The guaranteed of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this CreateLoadBalancerOption.

        是否独享型负载均衡器。取值： - true：独享型。 - false：共享型。  当前只支持设置为true，设置为false会返回400 Bad Request 。默认：true。

        :param guaranteed: The guaranteed of this CreateLoadBalancerOption.
        :type: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateLoadBalancerOption.

        负载均衡器所在的VPC ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/vpcs 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The vpc_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateLoadBalancerOption.

        负载均衡器所在的VPC ID。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/vpcs 响应参数中的id得到。  使用说明： - vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param vpc_id: The vpc_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this CreateLoadBalancerOption.

        可用区列表。可通过GET https&#58;//{ELB_Endponit}/v3/{project_id}/elb/availability-zones接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。

        :return: The availability_zone_list of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this CreateLoadBalancerOption.

        可用区列表。可通过GET https&#58;//{ELB_Endponit}/v3/{project_id}/elb/availability-zones接口来查询可用区集合列表。创建负载均衡器时，从查询结果选择某一个可用区集合，并从中选择一个或多个可用区。

        :param availability_zone_list: The availability_zone_list of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateLoadBalancerOption.

        负载均衡器所属的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The enterprise_project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateLoadBalancerOption.

        负载均衡器所属的企业项目ID。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param enterprise_project_id: The enterprise_project_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateLoadBalancerOption.

        负载均衡的标签列表。示例：\"tags\":[{\"key\":\"my_tag\",\"value\":\"my_tag_value\"}]

        :return: The tags of this CreateLoadBalancerOption.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateLoadBalancerOption.

        负载均衡的标签列表。示例：\"tags\":[{\"key\":\"my_tag\",\"value\":\"my_tag_value\"}]

        :param tags: The tags of this CreateLoadBalancerOption.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateLoadBalancerOption.

        负载均衡器的管理状态。只能设置为true。默认：true。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The admin_state_up of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateLoadBalancerOption.

        负载均衡器的管理状态。只能设置为true。默认：true。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param admin_state_up: The admin_state_up of this CreateLoadBalancerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this CreateLoadBalancerOption.

        七层Flavor ID。[创建负载均衡器时l4_flavor_id和l7_flavor_id不能都不传](tag:dt,dt_test) [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso) 注意：当l4_flavor_id和l7_flavor_id都不传的时，会选择默认flavor。

        :return: The l7_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this CreateLoadBalancerOption.

        七层Flavor ID。[创建负载均衡器时l4_flavor_id和l7_flavor_id不能都不传](tag:dt,dt_test) [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso) 注意：当l4_flavor_id和l7_flavor_id都不传的时，会选择默认flavor。

        :param l7_flavor_id: The l7_flavor_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerOption.

        资源账单信息，取值： - 空：按需计费。 - 非空：包周期计费。 包周期计费billing_info字段的格式为：order_id&#58;product_id&#58;region_id&#58;project_id，如： CS2107161019CDJZZ&#58;OFFI569702121789763584&#58;eu-de&#58;057ef081eb00d2732fd1c01a9be75e6f 使用说明： - admin权限才能更新此字段。 [不支持该字段，请勿使用](tag:dt,dt_test)

        :return: The billing_info of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerOption.

        资源账单信息，取值： - 空：按需计费。 - 非空：包周期计费。 包周期计费billing_info字段的格式为：order_id&#58;product_id&#58;region_id&#58;project_id，如： CS2107161019CDJZZ&#58;OFFI569702121789763584&#58;eu-de&#58;057ef081eb00d2732fd1c01a9be75e6f 使用说明： - admin权限才能更新此字段。 [不支持该字段，请勿使用](tag:dt,dt_test)

        :param billing_info: The billing_info of this CreateLoadBalancerOption.
        :type: str
        """
        self._billing_info = billing_info

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this CreateLoadBalancerOption.


        :return: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :rtype: BandwidthRef
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this CreateLoadBalancerOption.


        :param ipv6_bandwidth: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :type: BandwidthRef
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def publicip_ids(self):
        """Gets the publicip_ids of this CreateLoadBalancerOption.

        负载均衡器绑定的公网IP ID。只支持绑定数组中的第一个EIP，其他将被忽略。

        :return: The publicip_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        """Sets the publicip_ids of this CreateLoadBalancerOption.

        负载均衡器绑定的公网IP ID。只支持绑定数组中的第一个EIP，其他将被忽略。

        :param publicip_ids: The publicip_ids of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def publicip(self):
        """Gets the publicip of this CreateLoadBalancerOption.


        :return: The publicip of this CreateLoadBalancerOption.
        :rtype: CreateLoadBalancerPublicIpOption
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreateLoadBalancerOption.


        :param publicip: The publicip of this CreateLoadBalancerOption.
        :type: CreateLoadBalancerPublicIpOption
        """
        self._publicip = publicip

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  使用说明： - 若不指定该字段，则会在当前负载均衡器所在子网作为下联面子网。  - 若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。  - 下联面子网必须属于该LB所在的VPC。  - 不支持边缘云子网。

        :return: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。  使用说明： - 若不指定该字段，则会在当前负载均衡器所在子网作为下联面子网。  - 若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。  - 下联面子网必须属于该LB所在的VPC。  - 不支持边缘云子网。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this CreateLoadBalancerOption.

        是否启用跨VPC后端转发。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性。  开启跨VPC后端转发后，后端服务器组支持添加其他VPC、其他公有云、云下数据中心的服务器。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The ip_target_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this CreateLoadBalancerOption.

        是否启用跨VPC后端转发。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性。  开启跨VPC后端转发后，后端服务器组支持添加其他VPC、其他公有云、云下数据中心的服务器。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param ip_target_enable: The ip_target_enable of this CreateLoadBalancerOption.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this CreateLoadBalancerOption.

        是否开启删除保护。取值：false不开启，true开启。默认false不开启。 > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :return: The deletion_protection_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this CreateLoadBalancerOption.

        是否开启删除保护。取值：false不开启，true开启。默认false不开启。 > 退场时需要先关闭所有资源的删除保护开关。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :param deletion_protection_enable: The deletion_protection_enable of this CreateLoadBalancerOption.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def prepaid_options(self):
        """Gets the prepaid_options of this CreateLoadBalancerOption.


        :return: The prepaid_options of this CreateLoadBalancerOption.
        :rtype: PrepaidCreateOption
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        """Sets the prepaid_options of this CreateLoadBalancerOption.


        :param prepaid_options: The prepaid_options of this CreateLoadBalancerOption.
        :type: PrepaidCreateOption
        """
        self._prepaid_options = prepaid_options

    @property
    def autoscaling(self):
        """Gets the autoscaling of this CreateLoadBalancerOption.


        :return: The autoscaling of this CreateLoadBalancerOption.
        :rtype: CreateLoadbalancerAutoscalingOption
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this CreateLoadBalancerOption.


        :param autoscaling: The autoscaling of this CreateLoadBalancerOption.
        :type: CreateLoadbalancerAutoscalingOption
        """
        self._autoscaling = autoscaling

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
