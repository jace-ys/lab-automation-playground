# coding: utf-8

"""
    Riffyn REST API

    ### Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ### Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ### Authentication Begin with a call the [authenticate](/#api-Authentication-authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your prefered token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](/#api-Authentication-verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn App UI.  ### Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ### Postman endpoint examples There is a YAML file with the examples of the request on Riffyn API [Click here](/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ### Client SDKs You may write your own API client, or you may use one of ours. [Click here](/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UpdateResourceBody(object):
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
        'name': 'str',
        'description': 'str',
        'properties': 'list[UpdateResourceBodyProperties]',
        'components': 'list[UpdateResourceBodyComponents]',
        'is_instrument': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'properties': 'properties',
        'components': 'components',
        'is_instrument': 'isInstrument'
    }

    def __init__(self, name=None, description=None, properties=None, components=None, is_instrument=None):  # noqa: E501
        """UpdateResourceBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._properties = None
        self._components = None
        self._is_instrument = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if components is not None:
            self.components = components
        if is_instrument is not None:
            self.is_instrument = is_instrument

    @property
    def name(self):
        """Gets the name of this UpdateResourceBody.  # noqa: E501

        The name of resource. If you do not provide this value, the existing name will be deleted  # noqa: E501

        :return: The name of this UpdateResourceBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateResourceBody.

        The name of resource. If you do not provide this value, the existing name will be deleted  # noqa: E501

        :param name: The name of this UpdateResourceBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateResourceBody.  # noqa: E501

        A brief description of the new resource. If you do not provide this value, the existing description will be deleted  # noqa: E501

        :return: The description of this UpdateResourceBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateResourceBody.

        A brief description of the new resource. If you do not provide this value, the existing description will be deleted  # noqa: E501

        :param description: The description of this UpdateResourceBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this UpdateResourceBody.  # noqa: E501

        The full list of immutable property types and values you would like to assign to the resource. Existing immutable values will be deleted and replaced with these values  # noqa: E501

        :return: The properties of this UpdateResourceBody.  # noqa: E501
        :rtype: list[UpdateResourceBodyProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateResourceBody.

        The full list of immutable property types and values you would like to assign to the resource. Existing immutable values will be deleted and replaced with these values  # noqa: E501

        :param properties: The properties of this UpdateResourceBody.  # noqa: E501
        :type: list[UpdateResourceBodyProperties]
        """

        self._properties = properties

    @property
    def components(self):
        """Gets the components of this UpdateResourceBody.  # noqa: E501

        Defines the components of this resource. E.g. The components of coffee are water and coffee grounds.  # noqa: E501

        :return: The components of this UpdateResourceBody.  # noqa: E501
        :rtype: list[UpdateResourceBodyComponents]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this UpdateResourceBody.

        Defines the components of this resource. E.g. The components of coffee are water and coffee grounds.  # noqa: E501

        :param components: The components of this UpdateResourceBody.  # noqa: E501
        :type: list[UpdateResourceBodyComponents]
        """

        self._components = components

    @property
    def is_instrument(self):
        """Gets the is_instrument of this UpdateResourceBody.  # noqa: E501

        Deprecated - Indicated if the new resource is an instrument.  # noqa: E501

        :return: The is_instrument of this UpdateResourceBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_instrument

    @is_instrument.setter
    def is_instrument(self, is_instrument):
        """Sets the is_instrument of this UpdateResourceBody.

        Deprecated - Indicated if the new resource is an instrument.  # noqa: E501

        :param is_instrument: The is_instrument of this UpdateResourceBody.  # noqa: E501
        :type: bool
        """

        self._is_instrument = is_instrument

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
        if issubclass(UpdateResourceBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateResourceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other