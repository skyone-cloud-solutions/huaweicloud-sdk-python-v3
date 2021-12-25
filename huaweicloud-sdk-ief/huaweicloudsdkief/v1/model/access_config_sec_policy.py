# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigSecPolicy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'optional': 'bool',
        'metadata': 'ValueInPropertyVisitorsRegisterTypeMetadata'
    }

    attribute_map = {
        'value': 'value',
        'optional': 'optional',
        'metadata': 'metadata'
    }

    def __init__(self, value=None, optional=None, metadata=None):
        """AccessConfigSecPolicy - a model defined in huaweicloud sdk"""
        
        

        self._value = None
        self._optional = None
        self._metadata = None
        self.discriminator = None

        self.value = value
        if optional is not None:
            self.optional = optional
        if metadata is not None:
            self.metadata = metadata

    @property
    def value(self):
        """Gets the value of this AccessConfigSecPolicy.

        value 最大长度512， value允许英文字母、数字、下划线、中划线、点、逗号、@、#、+、\\、/、？、^、=、%、&、:、~

        :return: The value of this AccessConfigSecPolicy.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AccessConfigSecPolicy.

        value 最大长度512， value允许英文字母、数字、下划线、中划线、点、逗号、@、#、+、\\、/、？、^、=、%、&、:、~

        :param value: The value of this AccessConfigSecPolicy.
        :type: str
        """
        self._value = value

    @property
    def optional(self):
        """Gets the optional of this AccessConfigSecPolicy.

        标识属性是否可选，默认为true

        :return: The optional of this AccessConfigSecPolicy.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this AccessConfigSecPolicy.

        标识属性是否可选，默认为true

        :param optional: The optional of this AccessConfigSecPolicy.
        :type: bool
        """
        self._optional = optional

    @property
    def metadata(self):
        """Gets the metadata of this AccessConfigSecPolicy.


        :return: The metadata of this AccessConfigSecPolicy.
        :rtype: ValueInPropertyVisitorsRegisterTypeMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AccessConfigSecPolicy.


        :param metadata: The metadata of this AccessConfigSecPolicy.
        :type: ValueInPropertyVisitorsRegisterTypeMetadata
        """
        self._metadata = metadata

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
        if not isinstance(other, AccessConfigSecPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
