# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDocWatermarkRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'doc_type': 'str',
        'file_password': 'str',
        'marked_file_password': 'str',
        'readonly_password': 'str',
        'visible_watermark': 'str',
        'font_size': 'str',
        'rotation': 'str',
        'opacity': 'str',
        'blind_watermark': 'str',
        'file': 'file',
        'image_mark': 'file',
        'visible_type': 'str'
    }

    attribute_map = {
        'doc_type': 'doc_type',
        'file_password': 'file_password',
        'marked_file_password': 'marked_file_password',
        'readonly_password': 'readonly_password',
        'visible_watermark': 'visible_watermark',
        'font_size': 'font_size',
        'rotation': 'rotation',
        'opacity': 'opacity',
        'blind_watermark': 'blind_watermark',
        'file': 'file',
        'image_mark': 'image_mark',
        'visible_type': 'visible_type'
    }

    def __init__(self, doc_type=None, file_password=None, marked_file_password=None, readonly_password=None, visible_watermark=None, font_size=None, rotation=None, opacity=None, blind_watermark=None, file=None, image_mark=None, visible_type=None):
        """CreateDocWatermarkRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._doc_type = None
        self._file_password = None
        self._marked_file_password = None
        self._readonly_password = None
        self._visible_watermark = None
        self._font_size = None
        self._rotation = None
        self._opacity = None
        self._blind_watermark = None
        self._file = None
        self._image_mark = None
        self._visible_type = None
        self.discriminator = None

        self.doc_type = doc_type
        if file_password is not None:
            self.file_password = file_password
        if marked_file_password is not None:
            self.marked_file_password = marked_file_password
        if readonly_password is not None:
            self.readonly_password = readonly_password
        if visible_watermark is not None:
            self.visible_watermark = visible_watermark
        if font_size is not None:
            self.font_size = font_size
        if rotation is not None:
            self.rotation = rotation
        if opacity is not None:
            self.opacity = opacity
        if blind_watermark is not None:
            self.blind_watermark = blind_watermark
        self.file = file
        if image_mark is not None:
            self.image_mark = image_mark
        if visible_type is not None:
            self.visible_type = visible_type

    @property
    def doc_type(self):
        """Gets the doc_type of this CreateDocWatermarkRequestBody.

        要嵌入水印的文档类型

        :return: The doc_type of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this CreateDocWatermarkRequestBody.

        要嵌入水印的文档类型

        :param doc_type: The doc_type of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._doc_type = doc_type

    @property
    def file_password(self):
        """Gets the file_password of this CreateDocWatermarkRequestBody.

        解密文件的密码， 最大支持长度256。添加水印后的文件不带密码。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :return: The file_password of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._file_password

    @file_password.setter
    def file_password(self, file_password):
        """Sets the file_password of this CreateDocWatermarkRequestBody.

        解密文件的密码， 最大支持长度256。添加水印后的文件不带密码。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :param file_password: The file_password of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._file_password = file_password

    @property
    def marked_file_password(self):
        """Gets the marked_file_password of this CreateDocWatermarkRequestBody.

        添加水印后给文件设置密码， 最大支持长度256。

        :return: The marked_file_password of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._marked_file_password

    @marked_file_password.setter
    def marked_file_password(self, marked_file_password):
        """Sets the marked_file_password of this CreateDocWatermarkRequestBody.

        添加水印后给文件设置密码， 最大支持长度256。

        :param marked_file_password: The marked_file_password of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._marked_file_password = marked_file_password

    @property
    def readonly_password(self):
        """Gets the readonly_password of this CreateDocWatermarkRequestBody.

        添加水印后给文件设置只读密码， 最大支持长度256。

        :return: The readonly_password of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._readonly_password

    @readonly_password.setter
    def readonly_password(self, readonly_password):
        """Sets the readonly_password of this CreateDocWatermarkRequestBody.

        添加水印后给文件设置只读密码， 最大支持长度256。

        :param readonly_password: The readonly_password of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._readonly_password = readonly_password

    @property
    def visible_watermark(self):
        """Gets the visible_watermark of this CreateDocWatermarkRequestBody.

        明水印内容，与“blind_watermark”字段至少有一个不为空

        :return: The visible_watermark of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._visible_watermark

    @visible_watermark.setter
    def visible_watermark(self, visible_watermark):
        """Sets the visible_watermark of this CreateDocWatermarkRequestBody.

        明水印内容，与“blind_watermark”字段至少有一个不为空

        :param visible_watermark: The visible_watermark of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._visible_watermark = visible_watermark

    @property
    def font_size(self):
        """Gets the font_size of this CreateDocWatermarkRequestBody.

        明水印字体大小，取值为[1,100]，默认值50

        :return: The font_size of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this CreateDocWatermarkRequestBody.

        明水印字体大小，取值为[1,100]，默认值50

        :param font_size: The font_size of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._font_size = font_size

    @property
    def rotation(self):
        """Gets the rotation of this CreateDocWatermarkRequestBody.

        明水印旋转角度，逆时针方向，取值为[0,90]，默认值45

        :return: The rotation of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this CreateDocWatermarkRequestBody.

        明水印旋转角度，逆时针方向，取值为[0,90]，默认值45

        :param rotation: The rotation of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._rotation = rotation

    @property
    def opacity(self):
        """Gets the opacity of this CreateDocWatermarkRequestBody.

        明水印的透明度，取值[0,1]，默认值为0.3；

        :return: The opacity of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this CreateDocWatermarkRequestBody.

        明水印的透明度，取值[0,1]，默认值为0.3；

        :param opacity: The opacity of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._opacity = opacity

    @property
    def blind_watermark(self):
        """Gets the blind_watermark of this CreateDocWatermarkRequestBody.

        暗水印内容，与“visible_watermark”字段至少有一个不为空

        :return: The blind_watermark of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._blind_watermark

    @blind_watermark.setter
    def blind_watermark(self, blind_watermark):
        """Sets the blind_watermark of this CreateDocWatermarkRequestBody.

        暗水印内容，与“visible_watermark”字段至少有一个不为空

        :param blind_watermark: The blind_watermark of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._blind_watermark = blind_watermark

    @property
    def file(self):
        """Gets the file of this CreateDocWatermarkRequestBody.

        要添加水印的文档

        :return: The file of this CreateDocWatermarkRequestBody.
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateDocWatermarkRequestBody.

        要添加水印的文档

        :param file: The file of this CreateDocWatermarkRequestBody.
        :type: file
        """
        self._file = file

    @property
    def image_mark(self):
        """Gets the image_mark of this CreateDocWatermarkRequestBody.

        图形水印的字节流。图形文件的格式必须为“png”或“jpg”，否则返回参数错误；图像文件大小不超过1MB；在分段的请求体“Content-Disposition”部分，参数“name”的值必须为“image_mark”。

        :return: The image_mark of this CreateDocWatermarkRequestBody.
        :rtype: file
        """
        return self._image_mark

    @image_mark.setter
    def image_mark(self, image_mark):
        """Sets the image_mark of this CreateDocWatermarkRequestBody.

        图形水印的字节流。图形文件的格式必须为“png”或“jpg”，否则返回参数错误；图像文件大小不超过1MB；在分段的请求体“Content-Disposition”部分，参数“name”的值必须为“image_mark”。

        :param image_mark: The image_mark of this CreateDocWatermarkRequestBody.
        :type: file
        """
        self._image_mark = image_mark

    @property
    def visible_type(self):
        """Gets the visible_type of this CreateDocWatermarkRequestBody.

        该字段为空时，默认为**TEXT**类型。  当该字段为**IMAGE**时: - 请求的表单中必须包含名为“image”的图像文件，图像格式必须为“png”或“jpg”，否则返回参数错误； - 图像文件大小不超过1MB； - “visible_watermark”，“font_size”，“rotation”和“opacity”字段无效。

        :return: The visible_type of this CreateDocWatermarkRequestBody.
        :rtype: str
        """
        return self._visible_type

    @visible_type.setter
    def visible_type(self, visible_type):
        """Sets the visible_type of this CreateDocWatermarkRequestBody.

        该字段为空时，默认为**TEXT**类型。  当该字段为**IMAGE**时: - 请求的表单中必须包含名为“image”的图像文件，图像格式必须为“png”或“jpg”，否则返回参数错误； - 图像文件大小不超过1MB； - “visible_watermark”，“font_size”，“rotation”和“opacity”字段无效。

        :param visible_type: The visible_type of this CreateDocWatermarkRequestBody.
        :type: str
        """
        self._visible_type = visible_type

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
        if not isinstance(other, CreateDocWatermarkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
