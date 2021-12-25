# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Network:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'direction': 'str',
        'protocol': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'src_domain': 'str',
        'src_geo': 'Geo',
        'destc_ip': 'str',
        'dest_port': 'int',
        'dest_domain': 'str',
        'dest_geo': 'Geo'
    }

    attribute_map = {
        'direction': 'direction',
        'protocol': 'protocol',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'src_domain': 'src_domain',
        'src_geo': 'src_geo',
        'destc_ip': 'destc_ip',
        'dest_port': 'dest_port',
        'dest_domain': 'dest_domain',
        'dest_geo': 'dest_geo'
    }

    def __init__(self, direction=None, protocol=None, src_ip=None, src_port=None, src_domain=None, src_geo=None, destc_ip=None, dest_port=None, dest_domain=None, dest_geo=None):
        """Network - a model defined in huaweicloud sdk"""
        
        

        self._direction = None
        self._protocol = None
        self._src_ip = None
        self._src_port = None
        self._src_domain = None
        self._src_geo = None
        self._destc_ip = None
        self._dest_port = None
        self._dest_domain = None
        self._dest_geo = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if protocol is not None:
            self.protocol = protocol
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if src_domain is not None:
            self.src_domain = src_domain
        if src_geo is not None:
            self.src_geo = src_geo
        if destc_ip is not None:
            self.destc_ip = destc_ip
        if dest_port is not None:
            self.dest_port = dest_port
        if dest_domain is not None:
            self.dest_domain = dest_domain
        if dest_geo is not None:
            self.dest_geo = dest_geo

    @property
    def direction(self):
        """Gets the direction of this Network.

        方向，取值范围：IN、OUT。

        :return: The direction of this Network.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Network.

        方向，取值范围：IN、OUT。

        :param direction: The direction of this Network.
        :type: str
        """
        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this Network.

        协议。

        :return: The protocol of this Network.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Network.

        协议。

        :param protocol: The protocol of this Network.
        :type: str
        """
        self._protocol = protocol

    @property
    def src_ip(self):
        """Gets the src_ip of this Network.

        源IP地址。

        :return: The src_ip of this Network.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this Network.

        源IP地址。

        :param src_ip: The src_ip of this Network.
        :type: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this Network.

        源端口，0–65535。

        :return: The src_port of this Network.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this Network.

        源端口，0–65535。

        :param src_port: The src_port of this Network.
        :type: int
        """
        self._src_port = src_port

    @property
    def src_domain(self):
        """Gets the src_domain of this Network.

        源域名，最大128个字符。

        :return: The src_domain of this Network.
        :rtype: str
        """
        return self._src_domain

    @src_domain.setter
    def src_domain(self, src_domain):
        """Sets the src_domain of this Network.

        源域名，最大128个字符。

        :param src_domain: The src_domain of this Network.
        :type: str
        """
        self._src_domain = src_domain

    @property
    def src_geo(self):
        """Gets the src_geo of this Network.


        :return: The src_geo of this Network.
        :rtype: Geo
        """
        return self._src_geo

    @src_geo.setter
    def src_geo(self, src_geo):
        """Sets the src_geo of this Network.


        :param src_geo: The src_geo of this Network.
        :type: Geo
        """
        self._src_geo = src_geo

    @property
    def destc_ip(self):
        """Gets the destc_ip of this Network.

        目标IP地址。

        :return: The destc_ip of this Network.
        :rtype: str
        """
        return self._destc_ip

    @destc_ip.setter
    def destc_ip(self, destc_ip):
        """Sets the destc_ip of this Network.

        目标IP地址。

        :param destc_ip: The destc_ip of this Network.
        :type: str
        """
        self._destc_ip = destc_ip

    @property
    def dest_port(self):
        """Gets the dest_port of this Network.

        目标端口，0–65535。

        :return: The dest_port of this Network.
        :rtype: int
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this Network.

        目标端口，0–65535。

        :param dest_port: The dest_port of this Network.
        :type: int
        """
        self._dest_port = dest_port

    @property
    def dest_domain(self):
        """Gets the dest_domain of this Network.

        目标域名，最大128个字符。

        :return: The dest_domain of this Network.
        :rtype: str
        """
        return self._dest_domain

    @dest_domain.setter
    def dest_domain(self, dest_domain):
        """Sets the dest_domain of this Network.

        目标域名，最大128个字符。

        :param dest_domain: The dest_domain of this Network.
        :type: str
        """
        self._dest_domain = dest_domain

    @property
    def dest_geo(self):
        """Gets the dest_geo of this Network.


        :return: The dest_geo of this Network.
        :rtype: Geo
        """
        return self._dest_geo

    @dest_geo.setter
    def dest_geo(self, dest_geo):
        """Sets the dest_geo of this Network.


        :param dest_geo: The dest_geo of this Network.
        :type: Geo
        """
        self._dest_geo = dest_geo

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
        if not isinstance(other, Network):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
