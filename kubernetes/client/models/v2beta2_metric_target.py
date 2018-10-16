# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2beta2MetricTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'average_utilization': 'int',
        'average_value': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'average_utilization': 'averageUtilization',
        'average_value': 'averageValue',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, average_utilization=None, average_value=None, type=None, value=None):
        """
        V2beta2MetricTarget - a model defined in Swagger
        """

        self._average_utilization = None
        self._average_value = None
        self._type = None
        self._value = None
        self.discriminator = None

        if average_utilization is not None:
          self.average_utilization = average_utilization
        if average_value is not None:
          self.average_value = average_value
        self.type = type
        if value is not None:
          self.value = value

    @property
    def average_utilization(self):
        """
        Gets the average_utilization of this V2beta2MetricTarget.
        averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type

        :return: The average_utilization of this V2beta2MetricTarget.
        :rtype: int
        """
        return self._average_utilization

    @average_utilization.setter
    def average_utilization(self, average_utilization):
        """
        Sets the average_utilization of this V2beta2MetricTarget.
        averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type

        :param average_utilization: The average_utilization of this V2beta2MetricTarget.
        :type: int
        """

        self._average_utilization = average_utilization

    @property
    def average_value(self):
        """
        Gets the average_value of this V2beta2MetricTarget.
        averageValue is the target value of the average of the metric across all relevant pods (as a quantity)

        :return: The average_value of this V2beta2MetricTarget.
        :rtype: str
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        """
        Sets the average_value of this V2beta2MetricTarget.
        averageValue is the target value of the average of the metric across all relevant pods (as a quantity)

        :param average_value: The average_value of this V2beta2MetricTarget.
        :type: str
        """

        self._average_value = average_value

    @property
    def type(self):
        """
        Gets the type of this V2beta2MetricTarget.
        type represents whether the metric type is Utilization, Value, or AverageValue

        :return: The type of this V2beta2MetricTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V2beta2MetricTarget.
        type represents whether the metric type is Utilization, Value, or AverageValue

        :param type: The type of this V2beta2MetricTarget.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this V2beta2MetricTarget.
        value is the target value of the metric (as a quantity).

        :return: The value of this V2beta2MetricTarget.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this V2beta2MetricTarget.
        value is the target value of the metric (as a quantity).

        :param value: The value of this V2beta2MetricTarget.
        :type: str
        """

        self._value = value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V2beta2MetricTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
