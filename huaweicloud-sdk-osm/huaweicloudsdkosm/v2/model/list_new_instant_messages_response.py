# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNewInstantMessagesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'imstatus': 'list[ImStatusV2]',
        'immsg': 'list[UserInstantIncidentMsgV2]',
        'last_message_time_id': 'str'
    }

    attribute_map = {
        'imstatus': 'imstatus',
        'immsg': 'immsg',
        'last_message_time_id': 'last_message_time_id'
    }

    def __init__(self, imstatus=None, immsg=None, last_message_time_id=None):
        """ListNewInstantMessagesResponse - a model defined in huaweicloud sdk"""
        
        super(ListNewInstantMessagesResponse, self).__init__()

        self._imstatus = None
        self._immsg = None
        self._last_message_time_id = None
        self.discriminator = None

        if imstatus is not None:
            self.imstatus = imstatus
        if immsg is not None:
            self.immsg = immsg
        if last_message_time_id is not None:
            self.last_message_time_id = last_message_time_id

    @property
    def imstatus(self):
        """Gets the imstatus of this ListNewInstantMessagesResponse.

        状态列表

        :return: The imstatus of this ListNewInstantMessagesResponse.
        :rtype: list[ImStatusV2]
        """
        return self._imstatus

    @imstatus.setter
    def imstatus(self, imstatus):
        """Sets the imstatus of this ListNewInstantMessagesResponse.

        状态列表

        :param imstatus: The imstatus of this ListNewInstantMessagesResponse.
        :type: list[ImStatusV2]
        """
        self._imstatus = imstatus

    @property
    def immsg(self):
        """Gets the immsg of this ListNewInstantMessagesResponse.

        留言内容列表

        :return: The immsg of this ListNewInstantMessagesResponse.
        :rtype: list[UserInstantIncidentMsgV2]
        """
        return self._immsg

    @immsg.setter
    def immsg(self, immsg):
        """Sets the immsg of this ListNewInstantMessagesResponse.

        留言内容列表

        :param immsg: The immsg of this ListNewInstantMessagesResponse.
        :type: list[UserInstantIncidentMsgV2]
        """
        self._immsg = immsg

    @property
    def last_message_time_id(self):
        """Gets the last_message_time_id of this ListNewInstantMessagesResponse.

        上次查询留言时间

        :return: The last_message_time_id of this ListNewInstantMessagesResponse.
        :rtype: str
        """
        return self._last_message_time_id

    @last_message_time_id.setter
    def last_message_time_id(self, last_message_time_id):
        """Sets the last_message_time_id of this ListNewInstantMessagesResponse.

        上次查询留言时间

        :param last_message_time_id: The last_message_time_id of this ListNewInstantMessagesResponse.
        :type: str
        """
        self._last_message_time_id = last_message_time_id

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
        if not isinstance(other, ListNewInstantMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
