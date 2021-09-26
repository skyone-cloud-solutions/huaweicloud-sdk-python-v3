# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQpsTimelineRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        '_from': 'int',
        'to': 'int',
        'hosts': 'str',
        'instances': 'str',
        'group_by': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances',
        'group_by': 'group_by'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, hosts=None, instances=None, group_by=None):
        """ListQpsTimelineRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self._group_by = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if group_by is not None:
            self.group_by = group_by

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListQpsTimelineRequest.

        企业项目id

        :return: The enterprise_project_id of this ListQpsTimelineRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListQpsTimelineRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListQpsTimelineRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        """Gets the _from of this ListQpsTimelineRequest.

        起始时间（13位毫秒时间戳）

        :return: The _from of this ListQpsTimelineRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListQpsTimelineRequest.

        起始时间（13位毫秒时间戳）

        :param _from: The _from of this ListQpsTimelineRequest.
        :type: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListQpsTimelineRequest.

        结束时间（13位毫秒时间戳）

        :return: The to of this ListQpsTimelineRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListQpsTimelineRequest.

        结束时间（13位毫秒时间戳）

        :param to: The to of this ListQpsTimelineRequest.
        :type: int
        """
        self._to = to

    @property
    def hosts(self):
        """Gets the hosts of this ListQpsTimelineRequest.

        域名id（通过ListHost接口查询）

        :return: The hosts of this ListQpsTimelineRequest.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListQpsTimelineRequest.

        域名id（通过ListHost接口查询）

        :param hosts: The hosts of this ListQpsTimelineRequest.
        :type: str
        """
        self._hosts = hosts

    @property
    def instances(self):
        """Gets the instances of this ListQpsTimelineRequest.

        独享实例实例id（仅实例化模式涉及）

        :return: The instances of this ListQpsTimelineRequest.
        :rtype: str
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListQpsTimelineRequest.

        独享实例实例id（仅实例化模式涉及）

        :param instances: The instances of this ListQpsTimelineRequest.
        :type: str
        """
        self._instances = instances

    @property
    def group_by(self):
        """Gets the group_by of this ListQpsTimelineRequest.

        展示维度，按天展示时传\"DAY\"

        :return: The group_by of this ListQpsTimelineRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ListQpsTimelineRequest.

        展示维度，按天展示时传\"DAY\"

        :param group_by: The group_by of this ListQpsTimelineRequest.
        :type: str
        """
        self._group_by = group_by

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
        if not isinstance(other, ListQpsTimelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
