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


class PropertyType(object):
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
        'synonyms': 'list[str]',
        'source': 'str',
        'parents': 'list[str]',
        'specs': 'Spec',
        'immutable': 'bool',
        'data_type': 'str',
        'has_units': 'bool',
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
        'synonyms': 'synonyms',
        'source': 'source',
        'parents': 'parents',
        'specs': 'specs',
        'immutable': 'immutable',
        'data_type': 'dataType',
        'has_units': 'hasUnits',
        'sharable': 'sharable',
        'public': 'public',
        'deleted': 'deleted',
        'creator': 'creator',
        'created': 'created'
    }

    def __init__(self, id=None, name=None, definition=None, synonyms=None, source=None, parents=None, specs=None, immutable=None, data_type=None, has_units=None, sharable=None, public=None, deleted=None, creator=None, created=None):  # noqa: E501
        """PropertyType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._definition = None
        self._synonyms = None
        self._source = None
        self._parents = None
        self._specs = None
        self._immutable = None
        self._data_type = None
        self._has_units = None
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
        if synonyms is not None:
            self.synonyms = synonyms
        if source is not None:
            self.source = source
        if parents is not None:
            self.parents = parents
        if specs is not None:
            self.specs = specs
        if immutable is not None:
            self.immutable = immutable
        if data_type is not None:
            self.data_type = data_type
        if has_units is not None:
            self.has_units = has_units
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
        """Gets the id of this PropertyType.  # noqa: E501

        The unique id of the property type.  # noqa: E501

        :return: The id of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PropertyType.

        The unique id of the property type.  # noqa: E501

        :param id: The id of this PropertyType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PropertyType.  # noqa: E501

        The name of the item.  # noqa: E501

        :return: The name of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyType.

        The name of the item.  # noqa: E501

        :param name: The name of this PropertyType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def definition(self):
        """Gets the definition of this PropertyType.  # noqa: E501

        A brief description of this property type.  # noqa: E501

        :return: The definition of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this PropertyType.

        A brief description of this property type.  # noqa: E501

        :param definition: The definition of this PropertyType.  # noqa: E501
        :type: str
        """

        self._definition = definition

    @property
    def synonyms(self):
        """Gets the synonyms of this PropertyType.  # noqa: E501


        :return: The synonyms of this PropertyType.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this PropertyType.


        :param synonyms: The synonyms of this PropertyType.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def source(self):
        """Gets the source of this PropertyType.  # noqa: E501


        :return: The source of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PropertyType.


        :param source: The source of this PropertyType.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def parents(self):
        """Gets the parents of this PropertyType.  # noqa: E501


        :return: The parents of this PropertyType.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this PropertyType.


        :param parents: The parents of this PropertyType.  # noqa: E501
        :type: list[str]
        """

        self._parents = parents

    @property
    def specs(self):
        """Gets the specs of this PropertyType.  # noqa: E501


        :return: The specs of this PropertyType.  # noqa: E501
        :rtype: Spec
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this PropertyType.


        :param specs: The specs of this PropertyType.  # noqa: E501
        :type: Spec
        """

        self._specs = specs

    @property
    def immutable(self):
        """Gets the immutable of this PropertyType.  # noqa: E501

        Indicates if values for this property type should be editable, once they've been set, in an experiment.  # noqa: E501

        :return: The immutable of this PropertyType.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this PropertyType.

        Indicates if values for this property type should be editable, once they've been set, in an experiment.  # noqa: E501

        :param immutable: The immutable of this PropertyType.  # noqa: E501
        :type: bool
        """

        self._immutable = immutable

    @property
    def data_type(self):
        """Gets the data_type of this PropertyType.  # noqa: E501


        :return: The data_type of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PropertyType.


        :param data_type: The data_type of this PropertyType.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def has_units(self):
        """Gets the has_units of this PropertyType.  # noqa: E501


        :return: The has_units of this PropertyType.  # noqa: E501
        :rtype: bool
        """
        return self._has_units

    @has_units.setter
    def has_units(self, has_units):
        """Sets the has_units of this PropertyType.


        :param has_units: The has_units of this PropertyType.  # noqa: E501
        :type: bool
        """

        self._has_units = has_units

    @property
    def sharable(self):
        """Gets the sharable of this PropertyType.  # noqa: E501

        Indicates if the property type can be shared with other users.  # noqa: E501

        :return: The sharable of this PropertyType.  # noqa: E501
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable):
        """Sets the sharable of this PropertyType.

        Indicates if the property type can be shared with other users.  # noqa: E501

        :param sharable: The sharable of this PropertyType.  # noqa: E501
        :type: bool
        """

        self._sharable = sharable

    @property
    def public(self):
        """Gets the public of this PropertyType.  # noqa: E501

        Indicates if the property type is visible to all users.  # noqa: E501

        :return: The public of this PropertyType.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this PropertyType.

        Indicates if the property type is visible to all users.  # noqa: E501

        :param public: The public of this PropertyType.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def deleted(self):
        """Gets the deleted of this PropertyType.  # noqa: E501

        Indicates if the property type has been soft deleted.  # noqa: E501

        :return: The deleted of this PropertyType.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this PropertyType.

        Indicates if the property type has been soft deleted.  # noqa: E501

        :param deleted: The deleted of this PropertyType.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def creator(self):
        """Gets the creator of this PropertyType.  # noqa: E501

        The `username` of the user that created this property type.  # noqa: E501

        :return: The creator of this PropertyType.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PropertyType.

        The `username` of the user that created this property type.  # noqa: E501

        :param creator: The creator of this PropertyType.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """Gets the created of this PropertyType.  # noqa: E501


        :return: The created of this PropertyType.  # noqa: E501
        :rtype: Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PropertyType.


        :param created: The created of this PropertyType.  # noqa: E501
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
        if issubclass(PropertyType, dict):
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
        if not isinstance(other, PropertyType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
