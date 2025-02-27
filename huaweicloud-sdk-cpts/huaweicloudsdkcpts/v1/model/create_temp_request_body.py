# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTempRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'int',
        'temp_type': 'int',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'temp_type': 'temp_type',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, project_id=None, temp_type=None, name=None, description=None):
        """CreateTempRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._temp_type = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.project_id = project_id
        self.temp_type = temp_type
        self.name = name
        if description is not None:
            self.description = description

    @property
    def project_id(self):
        """Gets the project_id of this CreateTempRequestBody.

        project_id

        :return: The project_id of this CreateTempRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateTempRequestBody.

        project_id

        :param project_id: The project_id of this CreateTempRequestBody.
        :type: int
        """
        self._project_id = project_id

    @property
    def temp_type(self):
        """Gets the temp_type of this CreateTempRequestBody.

        temp_type

        :return: The temp_type of this CreateTempRequestBody.
        :rtype: int
        """
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type):
        """Sets the temp_type of this CreateTempRequestBody.

        temp_type

        :param temp_type: The temp_type of this CreateTempRequestBody.
        :type: int
        """
        self._temp_type = temp_type

    @property
    def name(self):
        """Gets the name of this CreateTempRequestBody.

        name

        :return: The name of this CreateTempRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTempRequestBody.

        name

        :param name: The name of this CreateTempRequestBody.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateTempRequestBody.

        description

        :return: The description of this CreateTempRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTempRequestBody.

        description

        :param description: The description of this CreateTempRequestBody.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, CreateTempRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
