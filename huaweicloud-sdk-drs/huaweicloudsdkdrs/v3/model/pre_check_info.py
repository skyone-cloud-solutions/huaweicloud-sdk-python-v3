# coding: utf-8

import pprint
import re

import six





class PreCheckInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'precheck_mode': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'precheck_mode': 'precheck_mode'
    }

    def __init__(self, job_id=None, precheck_mode=None):
        """PreCheckInfo - a model defined in huaweicloud sdk"""
        
        

        self._job_id = None
        self._precheck_mode = None
        self.discriminator = None

        self.job_id = job_id
        self.precheck_mode = precheck_mode

    @property
    def job_id(self):
        """Gets the job_id of this PreCheckInfo.

        任务id

        :return: The job_id of this PreCheckInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this PreCheckInfo.

        任务id

        :param job_id: The job_id of this PreCheckInfo.
        :type: str
        """
        self._job_id = job_id

    @property
    def precheck_mode(self):
        """Gets the precheck_mode of this PreCheckInfo.

        预检查模式

        :return: The precheck_mode of this PreCheckInfo.
        :rtype: str
        """
        return self._precheck_mode

    @precheck_mode.setter
    def precheck_mode(self, precheck_mode):
        """Sets the precheck_mode of this PreCheckInfo.

        预检查模式

        :param precheck_mode: The precheck_mode of this PreCheckInfo.
        :type: str
        """
        self._precheck_mode = precheck_mode

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
        if not isinstance(other, PreCheckInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
