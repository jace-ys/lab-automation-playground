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


class SetRunOverridesBody(object):
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
        'run_ids': 'list[str]',
        'activity_id': 'str',
        'overrides': 'object'
    }

    attribute_map = {
        'run_ids': 'runIds',
        'activity_id': 'activityId',
        'overrides': 'overrides'
    }

    def __init__(self, run_ids=None, activity_id=None, overrides=None):  # noqa: E501
        """SetRunOverridesBody - a model defined in Swagger"""  # noqa: E501
        self._run_ids = None
        self._activity_id = None
        self._overrides = None
        self.discriminator = None
        if run_ids is not None:
            self.run_ids = run_ids
        if activity_id is not None:
            self.activity_id = activity_id
        self.overrides = overrides

    @property
    def run_ids(self):
        """Gets the run_ids of this SetRunOverridesBody.  # noqa: E501

        If specified, the overrides will be applied to all runs contained in the list of `runIds`. You may only specify either `runIds` or `activityId`, but not both. Any error will be returned if both are specified.   # noqa: E501

        :return: The run_ids of this SetRunOverridesBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._run_ids

    @run_ids.setter
    def run_ids(self, run_ids):
        """Sets the run_ids of this SetRunOverridesBody.

        If specified, the overrides will be applied to all runs contained in the list of `runIds`. You may only specify either `runIds` or `activityId`, but not both. Any error will be returned if both are specified.   # noqa: E501

        :param run_ids: The run_ids of this SetRunOverridesBody.  # noqa: E501
        :type: list[str]
        """

        self._run_ids = run_ids

    @property
    def activity_id(self):
        """Gets the activity_id of this SetRunOverridesBody.  # noqa: E501

        If specified, the overrides will be applied to all runs in the activity. You may only specify either `runIds` or `activityId`, but not both. Any error will be returned if both are specified. Refers to the Process level Activity `_id`.   # noqa: E501

        :return: The activity_id of this SetRunOverridesBody.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this SetRunOverridesBody.

        If specified, the overrides will be applied to all runs in the activity. You may only specify either `runIds` or `activityId`, but not both. Any error will be returned if both are specified. Refers to the Process level Activity `_id`.   # noqa: E501

        :param activity_id: The activity_id of this SetRunOverridesBody.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def overrides(self):
        """Gets the overrides of this SetRunOverridesBody.  # noqa: E501

        overrides keys must be in the format of `activityId | resourceDefId | componentId | propertyTypeId`. The value can be type specific or a string. The value will be parsed based on the data type of the property type of the override. If you are not specifying a componentId, use the string `null` in place of the `componentId`.  example:  ``` {   \"RS2vW87PNg33T4HTQ |EnGj979ADGJJZSPMF | null | concentration\": \"1\" } ```   # noqa: E501

        :return: The overrides of this SetRunOverridesBody.  # noqa: E501
        :rtype: object
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this SetRunOverridesBody.

        overrides keys must be in the format of `activityId | resourceDefId | componentId | propertyTypeId`. The value can be type specific or a string. The value will be parsed based on the data type of the property type of the override. If you are not specifying a componentId, use the string `null` in place of the `componentId`.  example:  ``` {   \"RS2vW87PNg33T4HTQ |EnGj979ADGJJZSPMF | null | concentration\": \"1\" } ```   # noqa: E501

        :param overrides: The overrides of this SetRunOverridesBody.  # noqa: E501
        :type: object
        """
        if overrides is None:
            raise ValueError("Invalid value for `overrides`, must not be `None`")  # noqa: E501

        self._overrides = overrides

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
        if issubclass(SetRunOverridesBody, dict):
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
        if not isinstance(other, SetRunOverridesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
