# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectsSet:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'update_time': 'datetime',
        'description': 'str',
        'id': 'int',
        'name': 'str',
        'status': 'int',
        'group': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'group': 'group'
    }

    def __init__(self, create_time=None, update_time=None, description=None, id=None, name=None, status=None, group=None):
        """ProjectsSet - a model defined in huaweicloud sdk"""
        
        

        self._create_time = None
        self._update_time = None
        self._description = None
        self._id = None
        self._name = None
        self._status = None
        self._group = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if group is not None:
            self.group = group

    @property
    def create_time(self):
        """Gets the create_time of this ProjectsSet.

        创建时间

        :return: The create_time of this ProjectsSet.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProjectsSet.

        创建时间

        :param create_time: The create_time of this ProjectsSet.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ProjectsSet.

        更新时间

        :return: The update_time of this ProjectsSet.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ProjectsSet.

        更新时间

        :param update_time: The update_time of this ProjectsSet.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def description(self):
        """Gets the description of this ProjectsSet.

        描述

        :return: The description of this ProjectsSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectsSet.

        描述

        :param description: The description of this ProjectsSet.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ProjectsSet.

        工程id

        :return: The id of this ProjectsSet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectsSet.

        工程id

        :param id: The id of this ProjectsSet.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectsSet.

        工程名字

        :return: The name of this ProjectsSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectsSet.

        工程名字

        :param name: The name of this ProjectsSet.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ProjectsSet.

        工程状态

        :return: The status of this ProjectsSet.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectsSet.

        工程状态

        :param status: The status of this ProjectsSet.
        :type: int
        """
        self._status = status

    @property
    def group(self):
        """Gets the group of this ProjectsSet.

        工程所属组

        :return: The group of this ProjectsSet.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProjectsSet.

        工程所属组

        :param group: The group of this ProjectsSet.
        :type: str
        """
        self._group = group

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
        if not isinstance(other, ProjectsSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
