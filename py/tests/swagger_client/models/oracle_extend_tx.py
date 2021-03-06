# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 0.7.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.encoded_hash import EncodedHash  # noqa: F401,E501
from swagger_client.models.ttl import TTL  # noqa: F401,E501


class OracleExtendTx(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'fee': 'int',
        'ttl': 'TTL',
        'oracle': 'EncodedHash',
        'nonce': 'int'
    }

    attribute_map = {
        'fee': 'fee',
        'ttl': 'ttl',
        'oracle': 'oracle',
        'nonce': 'nonce'
    }

    def __init__(self, fee=None, ttl=None, oracle=None, nonce=None):  # noqa: E501
        """OracleExtendTx - a model defined in Swagger"""  # noqa: E501

        self._fee = None
        self._ttl = None
        self._oracle = None
        self._nonce = None
        self.discriminator = None

        self.fee = fee
        self.ttl = ttl
        if oracle is not None:
            self.oracle = oracle
        if nonce is not None:
            self.nonce = nonce

    @property
    def fee(self):
        """Gets the fee of this OracleExtendTx.  # noqa: E501


        :return: The fee of this OracleExtendTx.  # noqa: E501
        :rtype: int
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this OracleExtendTx.


        :param fee: The fee of this OracleExtendTx.  # noqa: E501
        :type: int
        """
        if fee is None:
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def ttl(self):
        """Gets the ttl of this OracleExtendTx.  # noqa: E501


        :return: The ttl of this OracleExtendTx.  # noqa: E501
        :rtype: TTL
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this OracleExtendTx.


        :param ttl: The ttl of this OracleExtendTx.  # noqa: E501
        :type: TTL
        """
        if ttl is None:
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def oracle(self):
        """Gets the oracle of this OracleExtendTx.  # noqa: E501


        :return: The oracle of this OracleExtendTx.  # noqa: E501
        :rtype: EncodedHash
        """
        return self._oracle

    @oracle.setter
    def oracle(self, oracle):
        """Sets the oracle of this OracleExtendTx.


        :param oracle: The oracle of this OracleExtendTx.  # noqa: E501
        :type: EncodedHash
        """

        self._oracle = oracle

    @property
    def nonce(self):
        """Gets the nonce of this OracleExtendTx.  # noqa: E501


        :return: The nonce of this OracleExtendTx.  # noqa: E501
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this OracleExtendTx.


        :param nonce: The nonce of this OracleExtendTx.  # noqa: E501
        :type: int
        """

        self._nonce = nonce

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OracleExtendTx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
