# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTask:


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
        'progress': 'int',
        'start_date': 'int',
        'end_date': 'int',
        'migrate_speed': 'float',
        'user_op': 'str'
    }

    attribute_map = {
        'name': 'name',
        'progress': 'progress',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'migrate_speed': 'migrate_speed',
        'user_op': 'user_op'
    }

    def __init__(self, name=None, progress=None, start_date=None, end_date=None, migrate_speed=None, user_op=None):
        """SubTask - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._progress = None
        self._start_date = None
        self._end_date = None
        self._migrate_speed = None
        self._user_op = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.progress = progress
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if user_op is not None:
            self.user_op = user_op

    @property
    def name(self):
        """Gets the name of this SubTask.

        子任务名称

        :return: The name of this SubTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubTask.

        子任务名称

        :param name: The name of this SubTask.
        :type: str
        """
        self._name = name

    @property
    def progress(self):
        """Gets the progress of this SubTask.

        子任务的进度，取值为0-100之间的整数

        :return: The progress of this SubTask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SubTask.

        子任务的进度，取值为0-100之间的整数

        :param progress: The progress of this SubTask.
        :type: int
        """
        self._progress = progress

    @property
    def start_date(self):
        """Gets the start_date of this SubTask.

        子任务开始时间

        :return: The start_date of this SubTask.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubTask.

        子任务开始时间

        :param start_date: The start_date of this SubTask.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SubTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :return: The end_date of this SubTask.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SubTask.

        子任务结束时间（如果子任务还没有结束，则为空）

        :param end_date: The end_date of this SubTask.
        :type: int
        """
        self._end_date = end_date

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this SubTask.

        迁移速率，Mbit/s

        :return: The migrate_speed of this SubTask.
        :rtype: float
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this SubTask.

        迁移速率，Mbit/s

        :param migrate_speed: The migrate_speed of this SubTask.
        :type: float
        """
        self._migrate_speed = migrate_speed

    @property
    def user_op(self):
        """Gets the user_op of this SubTask.

        触发子任务的用户操作名称

        :return: The user_op of this SubTask.
        :rtype: str
        """
        return self._user_op

    @user_op.setter
    def user_op(self, user_op):
        """Sets the user_op of this SubTask.

        触发子任务的用户操作名称

        :param user_op: The user_op of this SubTask.
        :type: str
        """
        self._user_op = user_op

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
        if not isinstance(other, SubTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
