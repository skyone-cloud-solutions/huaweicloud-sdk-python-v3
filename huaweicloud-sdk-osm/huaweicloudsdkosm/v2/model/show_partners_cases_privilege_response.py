# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowPartnersCasesPrivilegeResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'has_privilege': 'bool'
    }

    attribute_map = {
        'has_privilege': 'has_privilege'
    }

    def __init__(self, has_privilege=None):
        """ShowPartnersCasesPrivilegeResponse - a model defined in huaweicloud sdk"""
        
        super(ShowPartnersCasesPrivilegeResponse, self).__init__()

        self._has_privilege = None
        self.discriminator = None

        if has_privilege is not None:
            self.has_privilege = has_privilege

    @property
    def has_privilege(self):
        """Gets the has_privilege of this ShowPartnersCasesPrivilegeResponse.

        是否有权限

        :return: The has_privilege of this ShowPartnersCasesPrivilegeResponse.
        :rtype: bool
        """
        return self._has_privilege

    @has_privilege.setter
    def has_privilege(self, has_privilege):
        """Sets the has_privilege of this ShowPartnersCasesPrivilegeResponse.

        是否有权限

        :param has_privilege: The has_privilege of this ShowPartnersCasesPrivilegeResponse.
        :type: bool
        """
        self._has_privilege = has_privilege

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
        if not isinstance(other, ShowPartnersCasesPrivilegeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
