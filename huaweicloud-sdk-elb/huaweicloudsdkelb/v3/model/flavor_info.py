# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connection': 'int',
        'cps': 'int',
        'qps': 'int',
        'bandwidth': 'int',
        'lcu': 'int'
    }

    attribute_map = {
        'connection': 'connection',
        'cps': 'cps',
        'qps': 'qps',
        'bandwidth': 'bandwidth',
        'lcu': 'lcu'
    }

    def __init__(self, connection=None, cps=None, qps=None, bandwidth=None, lcu=None):
        """FlavorInfo - a model defined in huaweicloud sdk"""
        
        

        self._connection = None
        self._cps = None
        self._qps = None
        self._bandwidth = None
        self._lcu = None
        self.discriminator = None

        self.connection = connection
        self.cps = cps
        if qps is not None:
            self.qps = qps
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if lcu is not None:
            self.lcu = lcu

    @property
    def connection(self):
        """Gets the connection of this FlavorInfo.

        并发数。

        :return: The connection of this FlavorInfo.
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this FlavorInfo.

        并发数。

        :param connection: The connection of this FlavorInfo.
        :type: int
        """
        self._connection = connection

    @property
    def cps(self):
        """Gets the cps of this FlavorInfo.

        新建数。

        :return: The cps of this FlavorInfo.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        """Sets the cps of this FlavorInfo.

        新建数。

        :param cps: The cps of this FlavorInfo.
        :type: int
        """
        self._cps = cps

    @property
    def qps(self):
        """Gets the qps of this FlavorInfo.

        7层每秒查询数。

        :return: The qps of this FlavorInfo.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this FlavorInfo.

        7层每秒查询数。

        :param qps: The qps of this FlavorInfo.
        :type: int
        """
        self._qps = qps

    @property
    def bandwidth(self):
        """Gets the bandwidth of this FlavorInfo.

        带宽。

        :return: The bandwidth of this FlavorInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this FlavorInfo.

        带宽。

        :param bandwidth: The bandwidth of this FlavorInfo.
        :type: int
        """
        self._bandwidth = bandwidth

    @property
    def lcu(self):
        """Gets the lcu of this FlavorInfo.

        flavor对应的lcu数量。

        :return: The lcu of this FlavorInfo.
        :rtype: int
        """
        return self._lcu

    @lcu.setter
    def lcu(self, lcu):
        """Sets the lcu of this FlavorInfo.

        flavor对应的lcu数量。

        :param lcu: The lcu of this FlavorInfo.
        :type: int
        """
        self._lcu = lcu

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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
