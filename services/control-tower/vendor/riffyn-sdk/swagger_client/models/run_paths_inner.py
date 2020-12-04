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


class RunPathsInner(object):
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
        'activities_order': 'list[str]',
        'connections_traversed': 'list[ConnectionLine]',
        'groups_traversed': 'list[str]',
        'description': 'str',
        'upstream_name': 'str',
        'downstream_name': 'str',
        'via': 'str'
    }

    attribute_map = {
        'activities_order': 'activitiesOrder',
        'connections_traversed': 'connectionsTraversed',
        'groups_traversed': 'groupsTraversed',
        'description': 'description',
        'upstream_name': 'upstreamName',
        'downstream_name': 'downstreamName',
        'via': 'via'
    }

    def __init__(self, activities_order=None, connections_traversed=None, groups_traversed=None, description=None, upstream_name=None, downstream_name=None, via=None):  # noqa: E501
        """RunPathsInner - a model defined in Swagger"""  # noqa: E501
        self._activities_order = None
        self._connections_traversed = None
        self._groups_traversed = None
        self._description = None
        self._upstream_name = None
        self._downstream_name = None
        self._via = None
        self.discriminator = None
        if activities_order is not None:
            self.activities_order = activities_order
        if connections_traversed is not None:
            self.connections_traversed = connections_traversed
        if groups_traversed is not None:
            self.groups_traversed = groups_traversed
        if description is not None:
            self.description = description
        if upstream_name is not None:
            self.upstream_name = upstream_name
        if downstream_name is not None:
            self.downstream_name = downstream_name
        if via is not None:
            self.via = via

    @property
    def activities_order(self):
        """Gets the activities_order of this RunPathsInner.  # noqa: E501

        The \"path\" from a start activity (step) to an end activity (step), specified as an array of activity `_id`s.  # noqa: E501

        :return: The activities_order of this RunPathsInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._activities_order

    @activities_order.setter
    def activities_order(self, activities_order):
        """Sets the activities_order of this RunPathsInner.

        The \"path\" from a start activity (step) to an end activity (step), specified as an array of activity `_id`s.  # noqa: E501

        :param activities_order: The activities_order of this RunPathsInner.  # noqa: E501
        :type: list[str]
        """

        self._activities_order = activities_order

    @property
    def connections_traversed(self):
        """Gets the connections_traversed of this RunPathsInner.  # noqa: E501

        The list of connections between each activity (step) in the path, and the resource `_id` and resource type of each connection.  # noqa: E501

        :return: The connections_traversed of this RunPathsInner.  # noqa: E501
        :rtype: list[ConnectionLine]
        """
        return self._connections_traversed

    @connections_traversed.setter
    def connections_traversed(self, connections_traversed):
        """Sets the connections_traversed of this RunPathsInner.

        The list of connections between each activity (step) in the path, and the resource `_id` and resource type of each connection.  # noqa: E501

        :param connections_traversed: The connections_traversed of this RunPathsInner.  # noqa: E501
        :type: list[ConnectionLine]
        """

        self._connections_traversed = connections_traversed

    @property
    def groups_traversed(self):
        """Gets the groups_traversed of this RunPathsInner.  # noqa: E501


        :return: The groups_traversed of this RunPathsInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups_traversed

    @groups_traversed.setter
    def groups_traversed(self, groups_traversed):
        """Sets the groups_traversed of this RunPathsInner.


        :param groups_traversed: The groups_traversed of this RunPathsInner.  # noqa: E501
        :type: list[str]
        """

        self._groups_traversed = groups_traversed

    @property
    def description(self):
        """Gets the description of this RunPathsInner.  # noqa: E501

        A description of the path, from start to end, including each branch along the path.  # noqa: E501

        :return: The description of this RunPathsInner.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunPathsInner.

        A description of the path, from start to end, including each branch along the path.  # noqa: E501

        :param description: The description of this RunPathsInner.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def upstream_name(self):
        """Gets the upstream_name of this RunPathsInner.  # noqa: E501

        The name of the upstream activity (step).  # noqa: E501

        :return: The upstream_name of this RunPathsInner.  # noqa: E501
        :rtype: str
        """
        return self._upstream_name

    @upstream_name.setter
    def upstream_name(self, upstream_name):
        """Sets the upstream_name of this RunPathsInner.

        The name of the upstream activity (step).  # noqa: E501

        :param upstream_name: The upstream_name of this RunPathsInner.  # noqa: E501
        :type: str
        """

        self._upstream_name = upstream_name

    @property
    def downstream_name(self):
        """Gets the downstream_name of this RunPathsInner.  # noqa: E501

        The name of the downstream activity (step).  # noqa: E501

        :return: The downstream_name of this RunPathsInner.  # noqa: E501
        :rtype: str
        """
        return self._downstream_name

    @downstream_name.setter
    def downstream_name(self, downstream_name):
        """Sets the downstream_name of this RunPathsInner.

        The name of the downstream activity (step).  # noqa: E501

        :param downstream_name: The downstream_name of this RunPathsInner.  # noqa: E501
        :type: str
        """

        self._downstream_name = downstream_name

    @property
    def via(self):
        """Gets the via of this RunPathsInner.  # noqa: E501

        A string that describes the branch locations within the start and end points of the path  # noqa: E501

        :return: The via of this RunPathsInner.  # noqa: E501
        :rtype: str
        """
        return self._via

    @via.setter
    def via(self, via):
        """Sets the via of this RunPathsInner.

        A string that describes the branch locations within the start and end points of the path  # noqa: E501

        :param via: The via of this RunPathsInner.  # noqa: E501
        :type: str
        """

        self._via = via

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
        if issubclass(RunPathsInner, dict):
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
        if not isinstance(other, RunPathsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
