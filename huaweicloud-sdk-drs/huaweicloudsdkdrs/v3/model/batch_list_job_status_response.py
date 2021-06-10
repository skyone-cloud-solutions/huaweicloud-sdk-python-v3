# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class BatchListJobStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'results': 'list[QueryJobStatusResp]',
        'count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'count': 'count'
    }

    def __init__(self, results=None, count=None):
        """BatchListJobStatusResponse - a model defined in huaweicloud sdk"""
        
        super(BatchListJobStatusResponse, self).__init__()

        self._results = None
        self._count = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if count is not None:
            self.count = count

    @property
    def results(self):
        """Gets the results of this BatchListJobStatusResponse.

        任务状态信息

        :return: The results of this BatchListJobStatusResponse.
        :rtype: list[QueryJobStatusResp]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchListJobStatusResponse.

        任务状态信息

        :param results: The results of this BatchListJobStatusResponse.
        :type: list[QueryJobStatusResp]
        """
        self._results = results

    @property
    def count(self):
        """Gets the count of this BatchListJobStatusResponse.

        返回任务数量

        :return: The count of this BatchListJobStatusResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchListJobStatusResponse.

        返回任务数量

        :param count: The count of this BatchListJobStatusResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, BatchListJobStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
