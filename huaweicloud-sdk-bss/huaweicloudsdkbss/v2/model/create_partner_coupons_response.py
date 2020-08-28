# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreatePartnerCouponsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_infos': 'list[CouponSimpleInfo]',
        'error_details': 'list[ErrorDetail]'
    }

    attribute_map = {
        'coupon_infos': 'coupon_infos',
        'error_details': 'error_details'
    }

    def __init__(self, coupon_infos=None, error_details=None):
        """CreatePartnerCouponsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._coupon_infos = None
        self._error_details = None
        self.discriminator = None

        if coupon_infos is not None:
            self.coupon_infos = coupon_infos
        if error_details is not None:
            self.error_details = error_details

    @property
    def coupon_infos(self):
        """Gets the coupon_infos of this CreatePartnerCouponsResponse.

        |参数名称：成功的客户ID和对应的券ID列表| |参数约束以及描述：成功的客户ID和对应的券ID列表|

        :return: The coupon_infos of this CreatePartnerCouponsResponse.
        :rtype: list[CouponSimpleInfo]
        """
        return self._coupon_infos

    @coupon_infos.setter
    def coupon_infos(self, coupon_infos):
        """Sets the coupon_infos of this CreatePartnerCouponsResponse.

        |参数名称：成功的客户ID和对应的券ID列表| |参数约束以及描述：成功的客户ID和对应的券ID列表|

        :param coupon_infos: The coupon_infos of this CreatePartnerCouponsResponse.
        :type: list[CouponSimpleInfo]
        """
        self._coupon_infos = coupon_infos

    @property
    def error_details(self):
        """Gets the error_details of this CreatePartnerCouponsResponse.

        |参数名称：错误的客户列表和错误信息| |参数约束以及描述：错误的客户列表和错误信息|

        :return: The error_details of this CreatePartnerCouponsResponse.
        :rtype: list[ErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this CreatePartnerCouponsResponse.

        |参数名称：错误的客户列表和错误信息| |参数约束以及描述：错误的客户列表和错误信息|

        :param error_details: The error_details of this CreatePartnerCouponsResponse.
        :type: list[ErrorDetail]
        """
        self._error_details = error_details

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
        if not isinstance(other, CreatePartnerCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
