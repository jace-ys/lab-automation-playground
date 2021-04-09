# coding: utf-8

"""
    Riffyn Nexus REST API V1

    ## Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ## Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ## Authentication Begin with a call the [authenticate](#/authentication/authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn Nexus App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn Nexus API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your preferred token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](#/authentication/verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn Nexus App UI.  ## Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ## Postman endpoint examples There is a YAML file with the examples of the request on Riffyn Nexus API [Click here](/v1/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ## Client SDKs You may write your own API client, or you may use one of ours. [Click here](/v1/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 4.2.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResourceType(object):
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
        'id': 'str',
        'name': 'str',
        'definition': 'str',
        'parents': 'list[ResourceTypeParents]',
        'synonyms': 'list[str]',
        'source': 'str',
        'properties': 'list[PropertyDef]',
        'components': 'list[Component]',
        'sharable': 'bool',
        'public': 'bool',
        'deleted': 'bool',
        'creator': 'str',
        'created': 'Created'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'definition': 'definition',
        'parents': 'parents',
        'synonyms': 'synonyms',
        'source': 'source',
        'properties': 'properties',
        'components': 'components',
        'sharable': 'sharable',
        'public': 'public',
        'deleted': 'deleted',
        'creator': 'creator',
        'created': 'created'
    }

    def __init__(self, id=None, name=None, definition=None, parents=None, synonyms=None, source=None, properties=None, components=None, sharable=None, public=None, deleted=None, creator=None, created=None):  # noqa: E501
        """ResourceType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._definition = None
        self._parents = None
        self._synonyms = None
        self._source = None
        self._properties = None
        self._components = None
        self._sharable = None
        self._public = None
        self._deleted = None
        self._creator = None
        self._created = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if definition is not None:
            self.definition = definition
        if parents is not None:
            self.parents = parents
        if synonyms is not None:
            self.synonyms = synonyms
        if source is not None:
            self.source = source
        if properties is not None:
            self.properties = properties
        if components is not None:
            self.components = components
        if sharable is not None:
            self.sharable = sharable
        if public is not None:
            self.public = public
        if deleted is not None:
            self.deleted = deleted
        if creator is not None:
            self.creator = creator
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this ResourceType.  # noqa: E501

        The unique id of the resource type.  # noqa: E501

        :return: The id of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceType.

        The unique id of the resource type.  # noqa: E501

        :param id: The id of this ResourceType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceType.  # noqa: E501

        The name of the item.  # noqa: E501

        :return: The name of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceType.

        The name of the item.  # noqa: E501

        :param name: The name of this ResourceType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def definition(self):
        """Gets the definition of this ResourceType.  # noqa: E501

        A brief description of this resource type  # noqa: E501

        :return: The definition of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ResourceType.

        A brief description of this resource type  # noqa: E501

        :param definition: The definition of this ResourceType.  # noqa: E501
        :type: str
        """

        self._definition = definition

    @property
    def parents(self):
        """Gets the parents of this ResourceType.  # noqa: E501

        A list of parents for the resource type.  # noqa: E501

        :return: The parents of this ResourceType.  # noqa: E501
        :rtype: list[ResourceTypeParents]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this ResourceType.

        A list of parents for the resource type.  # noqa: E501

        :param parents: The parents of this ResourceType.  # noqa: E501
        :type: list[ResourceTypeParents]
        """

        self._parents = parents

    @property
    def synonyms(self):
        """Gets the synonyms of this ResourceType.  # noqa: E501

        A list of additional names that may be used to help identify this resource type.  # noqa: E501

        :return: The synonyms of this ResourceType.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this ResourceType.

        A list of additional names that may be used to help identify this resource type.  # noqa: E501

        :param synonyms: The synonyms of this ResourceType.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def source(self):
        """Gets the source of this ResourceType.  # noqa: E501

        Indicates whether the resource type was created by Riffyn, or by a user.  # noqa: E501

        :return: The source of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ResourceType.

        Indicates whether the resource type was created by Riffyn, or by a user.  # noqa: E501

        :param source: The source of this ResourceType.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER_DEFINED", "SYSTEM"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def properties(self):
        """Gets the properties of this ResourceType.  # noqa: E501


        :return: The properties of this ResourceType.  # noqa: E501
        :rtype: list[PropertyDef]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ResourceType.


        :param properties: The properties of this ResourceType.  # noqa: E501
        :type: list[PropertyDef]
        """

        self._properties = properties

    @property
    def components(self):
        """Gets the components of this ResourceType.  # noqa: E501


        :return: The components of this ResourceType.  # noqa: E501
        :rtype: list[Component]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ResourceType.


        :param components: The components of this ResourceType.  # noqa: E501
        :type: list[Component]
        """

        self._components = components

    @property
    def sharable(self):
        """Gets the sharable of this ResourceType.  # noqa: E501

        Indicates if the resource type can be shared with other users  # noqa: E501

        :return: The sharable of this ResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable):
        """Sets the sharable of this ResourceType.

        Indicates if the resource type can be shared with other users  # noqa: E501

        :param sharable: The sharable of this ResourceType.  # noqa: E501
        :type: bool
        """

        self._sharable = sharable

    @property
    def public(self):
        """Gets the public of this ResourceType.  # noqa: E501

        Indicates if the resource type is visible to all users  # noqa: E501

        :return: The public of this ResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ResourceType.

        Indicates if the resource type is visible to all users  # noqa: E501

        :param public: The public of this ResourceType.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def deleted(self):
        """Gets the deleted of this ResourceType.  # noqa: E501

        Indicates if the resource type has been soft deleted  # noqa: E501

        :return: The deleted of this ResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ResourceType.

        Indicates if the resource type has been soft deleted  # noqa: E501

        :param deleted: The deleted of this ResourceType.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def creator(self):
        """Gets the creator of this ResourceType.  # noqa: E501

        The username of the user that created this resource type  # noqa: E501

        :return: The creator of this ResourceType.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this ResourceType.

        The username of the user that created this resource type  # noqa: E501

        :param creator: The creator of this ResourceType.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """Gets the created of this ResourceType.  # noqa: E501


        :return: The created of this ResourceType.  # noqa: E501
        :rtype: Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResourceType.


        :param created: The created of this ResourceType.  # noqa: E501
        :type: Created
        """

        self._created = created

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
        if issubclass(ResourceType, dict):
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
        if not isinstance(other, ResourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other