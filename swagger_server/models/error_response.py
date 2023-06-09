# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ErrorResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, details: str=None):  # noqa: E501
        """ErrorResponse - a model defined in Swagger

        :param details: The details of this ErrorResponse.  # noqa: E501
        :type details: str
        """
        self.swagger_types = {
            'details': str
        }

        self.attribute_map = {
            'details': 'details'
        }
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse of this ErrorResponse.  # noqa: E501
        :rtype: ErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def details(self) -> str:
        """Gets the details of this ErrorResponse.

        Error description  # noqa: E501

        :return: The details of this ErrorResponse.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details: str):
        """Sets the details of this ErrorResponse.

        Error description  # noqa: E501

        :param details: The details of this ErrorResponse.
        :type details: str
        """

        self._details = details
