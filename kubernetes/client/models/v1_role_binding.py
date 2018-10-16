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


class V1RoleBinding(object):
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
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'role_ref': 'V1RoleRef',
        'subjects': 'list[V1Subject]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'role_ref': 'roleRef',
        'subjects': 'subjects'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, role_ref=None, subjects=None):
        """
        V1RoleBinding - a model defined in Swagger
        """

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._role_ref = None
        self._subjects = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        self.role_ref = role_ref
        if subjects is not None:
          self.subjects = subjects

    @property
    def api_version(self):
        """
        Gets the api_version of this V1RoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1RoleBinding.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1RoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1RoleBinding.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1RoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1RoleBinding.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1RoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1RoleBinding.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1RoleBinding.
        Standard object's metadata.

        :return: The metadata of this V1RoleBinding.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1RoleBinding.
        Standard object's metadata.

        :param metadata: The metadata of this V1RoleBinding.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def role_ref(self):
        """
        Gets the role_ref of this V1RoleBinding.
        RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.

        :return: The role_ref of this V1RoleBinding.
        :rtype: V1RoleRef
        """
        return self._role_ref

    @role_ref.setter
    def role_ref(self, role_ref):
        """
        Sets the role_ref of this V1RoleBinding.
        RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.

        :param role_ref: The role_ref of this V1RoleBinding.
        :type: V1RoleRef
        """
        if role_ref is None:
            raise ValueError("Invalid value for `role_ref`, must not be `None`")

        self._role_ref = role_ref

    @property
    def subjects(self):
        """
        Gets the subjects of this V1RoleBinding.
        Subjects holds references to the objects the role applies to.

        :return: The subjects of this V1RoleBinding.
        :rtype: list[V1Subject]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """
        Sets the subjects of this V1RoleBinding.
        Subjects holds references to the objects the role applies to.

        :param subjects: The subjects of this V1RoleBinding.
        :type: list[V1Subject]
        """

        self._subjects = subjects

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
        if not isinstance(other, V1RoleBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
