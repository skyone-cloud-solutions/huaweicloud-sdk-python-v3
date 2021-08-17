# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutTaskReq:


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
        'type': 'str',
        'os_type': 'str',
        'id': 'str',
        'priority': 'int',
        'region_id': 'str',
        'start_target_server': 'bool',
        'enterprise_project_id': 'str',
        'migration_ip': 'str',
        'region_name': 'str',
        'project_name': 'str',
        'project_id': 'str',
        'vm_template_id': 'str',
        'source_server': 'PostSourceServerBody',
        'target_server': 'TargetServer',
        'state': 'str',
        'estimate_complete_time': 'int',
        'connected': 'bool',
        'create_date': 'int',
        'start_date': 'int',
        'finish_date': 'int',
        'migrate_speed': 'float',
        'error_json': 'str',
        'total_time': 'int',
        'float_ip': 'str',
        'remain_seconds': 'int',
        'target_snapshot_id': 'str',
        'clone_server': 'CloneServer',
        'sub_tasks': 'list[SubTask]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'os_type': 'os_type',
        'id': 'id',
        'priority': 'priority',
        'region_id': 'region_id',
        'start_target_server': 'start_target_server',
        'enterprise_project_id': 'enterprise_project_id',
        'migration_ip': 'migration_ip',
        'region_name': 'region_name',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'vm_template_id': 'vm_template_id',
        'source_server': 'source_server',
        'target_server': 'target_server',
        'state': 'state',
        'estimate_complete_time': 'estimate_complete_time',
        'connected': 'connected',
        'create_date': 'create_date',
        'start_date': 'start_date',
        'finish_date': 'finish_date',
        'migrate_speed': 'migrate_speed',
        'error_json': 'error_json',
        'total_time': 'total_time',
        'float_ip': 'float_ip',
        'remain_seconds': 'remain_seconds',
        'target_snapshot_id': 'target_snapshot_id',
        'clone_server': 'clone_server',
        'sub_tasks': 'sub_tasks'
    }

    def __init__(self, name=None, type=None, os_type=None, id=None, priority=None, region_id=None, start_target_server=None, enterprise_project_id=None, migration_ip=None, region_name=None, project_name=None, project_id=None, vm_template_id=None, source_server=None, target_server=None, state=None, estimate_complete_time=None, connected=None, create_date=None, start_date=None, finish_date=None, migrate_speed=None, error_json=None, total_time=None, float_ip=None, remain_seconds=None, target_snapshot_id=None, clone_server=None, sub_tasks=None):
        """PutTaskReq - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._os_type = None
        self._id = None
        self._priority = None
        self._region_id = None
        self._start_target_server = None
        self._enterprise_project_id = None
        self._migration_ip = None
        self._region_name = None
        self._project_name = None
        self._project_id = None
        self._vm_template_id = None
        self._source_server = None
        self._target_server = None
        self._state = None
        self._estimate_complete_time = None
        self._connected = None
        self._create_date = None
        self._start_date = None
        self._finish_date = None
        self._migrate_speed = None
        self._error_json = None
        self._total_time = None
        self._float_ip = None
        self._remain_seconds = None
        self._target_snapshot_id = None
        self._clone_server = None
        self._sub_tasks = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if os_type is not None:
            self.os_type = os_type
        if id is not None:
            self.id = id
        if priority is not None:
            self.priority = priority
        if region_id is not None:
            self.region_id = region_id
        if start_target_server is not None:
            self.start_target_server = start_target_server
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if migration_ip is not None:
            self.migration_ip = migration_ip
        if region_name is not None:
            self.region_name = region_name
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if vm_template_id is not None:
            self.vm_template_id = vm_template_id
        if source_server is not None:
            self.source_server = source_server
        if target_server is not None:
            self.target_server = target_server
        if state is not None:
            self.state = state
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if connected is not None:
            self.connected = connected
        if create_date is not None:
            self.create_date = create_date
        if start_date is not None:
            self.start_date = start_date
        if finish_date is not None:
            self.finish_date = finish_date
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if error_json is not None:
            self.error_json = error_json
        if total_time is not None:
            self.total_time = total_time
        if float_ip is not None:
            self.float_ip = float_ip
        if remain_seconds is not None:
            self.remain_seconds = remain_seconds
        if target_snapshot_id is not None:
            self.target_snapshot_id = target_snapshot_id
        if clone_server is not None:
            self.clone_server = clone_server
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks

    @property
    def name(self):
        """Gets the name of this PutTaskReq.

        任务名称（用户自定义）

        :return: The name of this PutTaskReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutTaskReq.

        任务名称（用户自定义）

        :param name: The name of this PutTaskReq.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this PutTaskReq.

        任务类型，创建时必选，更新时可选 

        :return: The type of this PutTaskReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PutTaskReq.

        任务类型，创建时必选，更新时可选 

        :param type: The type of this PutTaskReq.
        :type: str
        """
        self._type = type

    @property
    def os_type(self):
        """Gets the os_type of this PutTaskReq.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :return: The os_type of this PutTaskReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this PutTaskReq.

        操作系统类型，分为WINDOWS和LINUX，创建时必选，更新时可选

        :param os_type: The os_type of this PutTaskReq.
        :type: str
        """
        self._os_type = os_type

    @property
    def id(self):
        """Gets the id of this PutTaskReq.

        迁移任务id

        :return: The id of this PutTaskReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PutTaskReq.

        迁移任务id

        :param id: The id of this PutTaskReq.
        :type: str
        """
        self._id = id

    @property
    def priority(self):
        """Gets the priority of this PutTaskReq.

        进程优先级  0：低  1：标准（默认）  2：高 

        :return: The priority of this PutTaskReq.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PutTaskReq.

        进程优先级  0：低  1：标准（默认）  2：高 

        :param priority: The priority of this PutTaskReq.
        :type: int
        """
        self._priority = priority

    @property
    def region_id(self):
        """Gets the region_id of this PutTaskReq.

        目的端服务器的区域ID

        :return: The region_id of this PutTaskReq.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PutTaskReq.

        目的端服务器的区域ID

        :param region_id: The region_id of this PutTaskReq.
        :type: str
        """
        self._region_id = region_id

    @property
    def start_target_server(self):
        """Gets the start_target_server of this PutTaskReq.

        迁移完成后是否启动目的端服务器  true：启动  false：停止 

        :return: The start_target_server of this PutTaskReq.
        :rtype: bool
        """
        return self._start_target_server

    @start_target_server.setter
    def start_target_server(self, start_target_server):
        """Sets the start_target_server of this PutTaskReq.

        迁移完成后是否启动目的端服务器  true：启动  false：停止 

        :param start_target_server: The start_target_server of this PutTaskReq.
        :type: bool
        """
        self._start_target_server = start_target_server

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PutTaskReq.

        企业项目id

        :return: The enterprise_project_id of this PutTaskReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PutTaskReq.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this PutTaskReq.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def migration_ip(self):
        """Gets the migration_ip of this PutTaskReq.

        目的端服务器的IP地址。  公网迁移时请填写弹性IP地址  专线迁移时请填写私有IP地址 

        :return: The migration_ip of this PutTaskReq.
        :rtype: str
        """
        return self._migration_ip

    @migration_ip.setter
    def migration_ip(self, migration_ip):
        """Sets the migration_ip of this PutTaskReq.

        目的端服务器的IP地址。  公网迁移时请填写弹性IP地址  专线迁移时请填写私有IP地址 

        :param migration_ip: The migration_ip of this PutTaskReq.
        :type: str
        """
        self._migration_ip = migration_ip

    @property
    def region_name(self):
        """Gets the region_name of this PutTaskReq.

        目的端服务器的区域名称

        :return: The region_name of this PutTaskReq.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this PutTaskReq.

        目的端服务器的区域名称

        :param region_name: The region_name of this PutTaskReq.
        :type: str
        """
        self._region_name = region_name

    @property
    def project_name(self):
        """Gets the project_name of this PutTaskReq.

        目的端服务器所在项目名称

        :return: The project_name of this PutTaskReq.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this PutTaskReq.

        目的端服务器所在项目名称

        :param project_name: The project_name of this PutTaskReq.
        :type: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        """Gets the project_id of this PutTaskReq.

        目的端服务器所在项目ID

        :return: The project_id of this PutTaskReq.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PutTaskReq.

        目的端服务器所在项目ID

        :param project_id: The project_id of this PutTaskReq.
        :type: str
        """
        self._project_id = project_id

    @property
    def vm_template_id(self):
        """Gets the vm_template_id of this PutTaskReq.

        模板ID

        :return: The vm_template_id of this PutTaskReq.
        :rtype: str
        """
        return self._vm_template_id

    @vm_template_id.setter
    def vm_template_id(self, vm_template_id):
        """Sets the vm_template_id of this PutTaskReq.

        模板ID

        :param vm_template_id: The vm_template_id of this PutTaskReq.
        :type: str
        """
        self._vm_template_id = vm_template_id

    @property
    def source_server(self):
        """Gets the source_server of this PutTaskReq.


        :return: The source_server of this PutTaskReq.
        :rtype: PostSourceServerBody
        """
        return self._source_server

    @source_server.setter
    def source_server(self, source_server):
        """Sets the source_server of this PutTaskReq.


        :param source_server: The source_server of this PutTaskReq.
        :type: PostSourceServerBody
        """
        self._source_server = source_server

    @property
    def target_server(self):
        """Gets the target_server of this PutTaskReq.


        :return: The target_server of this PutTaskReq.
        :rtype: TargetServer
        """
        return self._target_server

    @target_server.setter
    def target_server(self, target_server):
        """Sets the target_server of this PutTaskReq.


        :param target_server: The target_server of this PutTaskReq.
        :type: TargetServer
        """
        self._target_server = target_server

    @property
    def state(self):
        """Gets the state of this PutTaskReq.

        任务状态

        :return: The state of this PutTaskReq.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PutTaskReq.

        任务状态

        :param state: The state of this PutTaskReq.
        :type: str
        """
        self._state = state

    @property
    def estimate_complete_time(self):
        """Gets the estimate_complete_time of this PutTaskReq.

        预估完成时间

        :return: The estimate_complete_time of this PutTaskReq.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        """Sets the estimate_complete_time of this PutTaskReq.

        预估完成时间

        :param estimate_complete_time: The estimate_complete_time of this PutTaskReq.
        :type: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def connected(self):
        """Gets the connected of this PutTaskReq.

        连接状态

        :return: The connected of this PutTaskReq.
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this PutTaskReq.

        连接状态

        :param connected: The connected of this PutTaskReq.
        :type: bool
        """
        self._connected = connected

    @property
    def create_date(self):
        """Gets the create_date of this PutTaskReq.

        任务创建时间

        :return: The create_date of this PutTaskReq.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PutTaskReq.

        任务创建时间

        :param create_date: The create_date of this PutTaskReq.
        :type: int
        """
        self._create_date = create_date

    @property
    def start_date(self):
        """Gets the start_date of this PutTaskReq.

        任务开始时间

        :return: The start_date of this PutTaskReq.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PutTaskReq.

        任务开始时间

        :param start_date: The start_date of this PutTaskReq.
        :type: int
        """
        self._start_date = start_date

    @property
    def finish_date(self):
        """Gets the finish_date of this PutTaskReq.

        任务结束时间

        :return: The finish_date of this PutTaskReq.
        :rtype: int
        """
        return self._finish_date

    @finish_date.setter
    def finish_date(self, finish_date):
        """Sets the finish_date of this PutTaskReq.

        任务结束时间

        :param finish_date: The finish_date of this PutTaskReq.
        :type: int
        """
        self._finish_date = finish_date

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this PutTaskReq.

        迁移速率，单位：MB/S

        :return: The migrate_speed of this PutTaskReq.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this PutTaskReq.

        迁移速率，单位：MB/S

        :param migrate_speed: The migrate_speed of this PutTaskReq.
        :type: float
        """
        self._migrate_speed = migrate_speed

    @property
    def error_json(self):
        """Gets the error_json of this PutTaskReq.

        错误信息

        :return: The error_json of this PutTaskReq.
        :rtype: str
        """
        return self._error_json

    @error_json.setter
    def error_json(self, error_json):
        """Sets the error_json of this PutTaskReq.

        错误信息

        :param error_json: The error_json of this PutTaskReq.
        :type: str
        """
        self._error_json = error_json

    @property
    def total_time(self):
        """Gets the total_time of this PutTaskReq.

        任务总耗时

        :return: The total_time of this PutTaskReq.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this PutTaskReq.

        任务总耗时

        :param total_time: The total_time of this PutTaskReq.
        :type: int
        """
        self._total_time = total_time

    @property
    def float_ip(self):
        """Gets the float_ip of this PutTaskReq.

        暂时保留float,兼容现网老版本的SMS-Agent

        :return: The float_ip of this PutTaskReq.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        """Sets the float_ip of this PutTaskReq.

        暂时保留float,兼容现网老版本的SMS-Agent

        :param float_ip: The float_ip of this PutTaskReq.
        :type: str
        """
        self._float_ip = float_ip

    @property
    def remain_seconds(self):
        """Gets the remain_seconds of this PutTaskReq.

        迁移剩余时间（秒）

        :return: The remain_seconds of this PutTaskReq.
        :rtype: int
        """
        return self._remain_seconds

    @remain_seconds.setter
    def remain_seconds(self, remain_seconds):
        """Sets the remain_seconds of this PutTaskReq.

        迁移剩余时间（秒）

        :param remain_seconds: The remain_seconds of this PutTaskReq.
        :type: int
        """
        self._remain_seconds = remain_seconds

    @property
    def target_snapshot_id(self):
        """Gets the target_snapshot_id of this PutTaskReq.

        目的端的快照id

        :return: The target_snapshot_id of this PutTaskReq.
        :rtype: str
        """
        return self._target_snapshot_id

    @target_snapshot_id.setter
    def target_snapshot_id(self, target_snapshot_id):
        """Sets the target_snapshot_id of this PutTaskReq.

        目的端的快照id

        :param target_snapshot_id: The target_snapshot_id of this PutTaskReq.
        :type: str
        """
        self._target_snapshot_id = target_snapshot_id

    @property
    def clone_server(self):
        """Gets the clone_server of this PutTaskReq.


        :return: The clone_server of this PutTaskReq.
        :rtype: CloneServer
        """
        return self._clone_server

    @clone_server.setter
    def clone_server(self, clone_server):
        """Sets the clone_server of this PutTaskReq.


        :param clone_server: The clone_server of this PutTaskReq.
        :type: CloneServer
        """
        self._clone_server = clone_server

    @property
    def sub_tasks(self):
        """Gets the sub_tasks of this PutTaskReq.

        任务包含的子任务列表

        :return: The sub_tasks of this PutTaskReq.
        :rtype: list[SubTask]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        """Sets the sub_tasks of this PutTaskReq.

        任务包含的子任务列表

        :param sub_tasks: The sub_tasks of this PutTaskReq.
        :type: list[SubTask]
        """
        self._sub_tasks = sub_tasks

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
        if not isinstance(other, PutTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
