# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListHistoryOperateLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'ops_list': 'list[OperateLog]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'ops_list': 'ops_list'
    }

    def __init__(self, total_count=None, ops_list=None):
        """ListHistoryOperateLogsResponse - a model defined in huaweicloud sdk"""
        
        super(ListHistoryOperateLogsResponse, self).__init__()

        self._total_count = None
        self._ops_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if ops_list is not None:
            self.ops_list = ops_list

    @property
    def total_count(self):
        """Gets the total_count of this ListHistoryOperateLogsResponse.

        总记录数

        :return: The total_count of this ListHistoryOperateLogsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListHistoryOperateLogsResponse.

        总记录数

        :param total_count: The total_count of this ListHistoryOperateLogsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def ops_list(self):
        """Gets the ops_list of this ListHistoryOperateLogsResponse.

        操作列表

        :return: The ops_list of this ListHistoryOperateLogsResponse.
        :rtype: list[OperateLog]
        """
        return self._ops_list

    @ops_list.setter
    def ops_list(self, ops_list):
        """Sets the ops_list of this ListHistoryOperateLogsResponse.

        操作列表

        :param ops_list: The ops_list of this ListHistoryOperateLogsResponse.
        :type: list[OperateLog]
        """
        self._ops_list = ops_list

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHistoryOperateLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
