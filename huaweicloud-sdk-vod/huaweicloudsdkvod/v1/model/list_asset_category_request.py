# coding: utf-8

import pprint
import re

import six





class ListAssetCategoryRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        """ListAssetCategoryRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self.discriminator = None

        self.id = id

    @property
    def id(self):
        """Gets the id of this ListAssetCategoryRequest.

        视频分类ID。 若设置为0，则查询所有一级分类。

        :return: The id of this ListAssetCategoryRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAssetCategoryRequest.

        视频分类ID。 若设置为0，则查询所有一级分类。

        :param id: The id of this ListAssetCategoryRequest.
        :type: int
        """
        self._id = id

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
        if not isinstance(other, ListAssetCategoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
