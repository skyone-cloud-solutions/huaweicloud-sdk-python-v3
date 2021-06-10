# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCaseTemplatesResponse(SdkResponse):


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
        'incident_template_list': 'list[IncidentTempV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'incident_template_list': 'incident_template_list'
    }

    def __init__(self, total_count=None, incident_template_list=None):
        """ListCaseTemplatesResponse - a model defined in huaweicloud sdk"""
        
        super(ListCaseTemplatesResponse, self).__init__()

        self._total_count = None
        self._incident_template_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if incident_template_list is not None:
            self.incident_template_list = incident_template_list

    @property
    def total_count(self):
        """Gets the total_count of this ListCaseTemplatesResponse.

        总数

        :return: The total_count of this ListCaseTemplatesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCaseTemplatesResponse.

        总数

        :param total_count: The total_count of this ListCaseTemplatesResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def incident_template_list(self):
        """Gets the incident_template_list of this ListCaseTemplatesResponse.

        模板列表

        :return: The incident_template_list of this ListCaseTemplatesResponse.
        :rtype: list[IncidentTempV2]
        """
        return self._incident_template_list

    @incident_template_list.setter
    def incident_template_list(self, incident_template_list):
        """Sets the incident_template_list of this ListCaseTemplatesResponse.

        模板列表

        :param incident_template_list: The incident_template_list of this ListCaseTemplatesResponse.
        :type: list[IncidentTempV2]
        """
        self._incident_template_list = incident_template_list

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
        if not isinstance(other, ListCaseTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
