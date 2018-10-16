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


class V1beta1CustomResourceDefinitionVersion(object):
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
        'name': 'str',
        'served': 'bool',
        'storage': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'served': 'served',
        'storage': 'storage'
    }

    def __init__(self, name=None, served=None, storage=None):
        """
        V1beta1CustomResourceDefinitionVersion - a model defined in Swagger
        """

        self._name = None
        self._served = None
        self._storage = None
        self.discriminator = None

        self.name = name
        self.served = served
        self.storage = storage

    @property
    def name(self):
        """
        Gets the name of this V1beta1CustomResourceDefinitionVersion.
        Name is the version name, e.g. “v1”, “v2beta1”, etc.

        :return: The name of this V1beta1CustomResourceDefinitionVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1CustomResourceDefinitionVersion.
        Name is the version name, e.g. “v1”, “v2beta1”, etc.

        :param name: The name of this V1beta1CustomResourceDefinitionVersion.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def served(self):
        """
        Gets the served of this V1beta1CustomResourceDefinitionVersion.
        Served is a flag enabling/disabling this version from being served via REST APIs

        :return: The served of this V1beta1CustomResourceDefinitionVersion.
        :rtype: bool
        """
        return self._served

    @served.setter
    def served(self, served):
        """
        Sets the served of this V1beta1CustomResourceDefinitionVersion.
        Served is a flag enabling/disabling this version from being served via REST APIs

        :param served: The served of this V1beta1CustomResourceDefinitionVersion.
        :type: bool
        """
        if served is None:
            raise ValueError("Invalid value for `served`, must not be `None`")

        self._served = served

    @property
    def storage(self):
        """
        Gets the storage of this V1beta1CustomResourceDefinitionVersion.
        Storage flags the version as storage version. There must be exactly one flagged as storage version.

        :return: The storage of this V1beta1CustomResourceDefinitionVersion.
        :rtype: bool
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this V1beta1CustomResourceDefinitionVersion.
        Storage flags the version as storage version. There must be exactly one flagged as storage version.

        :param storage: The storage of this V1beta1CustomResourceDefinitionVersion.
        :type: bool
        """
        if storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")

        self._storage = storage

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
        if not isinstance(other, V1beta1CustomResourceDefinitionVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
