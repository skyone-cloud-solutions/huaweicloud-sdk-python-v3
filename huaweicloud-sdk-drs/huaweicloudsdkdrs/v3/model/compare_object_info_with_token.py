# coding: utf-8

import pprint
import re

import six





class CompareObjectInfoWithToken:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'table_name_with_token': 'list[CompareTableInfoWithToken]'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name_with_token': 'table_name_with_token'
    }

    def __init__(self, db_name=None, table_name_with_token=None):
        """CompareObjectInfoWithToken - a model defined in huaweicloud sdk"""
        
        

        self._db_name = None
        self._table_name_with_token = None
        self.discriminator = None

        self.db_name = db_name
        if table_name_with_token is not None:
            self.table_name_with_token = table_name_with_token

    @property
    def db_name(self):
        """Gets the db_name of this CompareObjectInfoWithToken.

        库名。

        :return: The db_name of this CompareObjectInfoWithToken.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this CompareObjectInfoWithToken.

        库名。

        :param db_name: The db_name of this CompareObjectInfoWithToken.
        :type: str
        """
        self._db_name = db_name

    @property
    def table_name_with_token(self):
        """Gets the table_name_with_token of this CompareObjectInfoWithToken.

        该库下的表信息列表（带token）。

        :return: The table_name_with_token of this CompareObjectInfoWithToken.
        :rtype: list[CompareTableInfoWithToken]
        """
        return self._table_name_with_token

    @table_name_with_token.setter
    def table_name_with_token(self, table_name_with_token):
        """Sets the table_name_with_token of this CompareObjectInfoWithToken.

        该库下的表信息列表（带token）。

        :param table_name_with_token: The table_name_with_token of this CompareObjectInfoWithToken.
        :type: list[CompareTableInfoWithToken]
        """
        self._table_name_with_token = table_name_with_token

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
        if not isinstance(other, CompareObjectInfoWithToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
