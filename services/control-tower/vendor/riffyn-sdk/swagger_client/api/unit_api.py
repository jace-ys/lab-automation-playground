# coding: utf-8

"""
    Riffyn REST API

    ### Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ### Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ### Authentication Begin with a call the [authenticate](/#api-Authentication-authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your prefered token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](/#api-Authentication-verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn App UI.  ### Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ### Postman endpoint examples There is a YAML file with the examples of the request on Riffyn API [Click here](/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ### Client SDKs You may write your own API client, or you may use one of ours. [Click here](/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UnitApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_unit(self, body, **kwargs):  # noqa: E501
        """create_unit  # noqa: E501

        Create a new unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_unit(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewUnitBody body: A JSON object containing the necessary properties to create a new unit. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_unit_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_unit_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_unit_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_unit  # noqa: E501

        Create a new unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_unit_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NewUnitBody body: A JSON object containing the necessary properties to create a new unit. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Unit',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_role_for_unit(self, id, user_id, **kwargs):  # noqa: E501
        """get_role_for_unit  # noqa: E501

        Returns the highest role for the specified user for the specific unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_for_unit(id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The `_id` of the unit. (required)
        :param str user_id: The `_id` of the user. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_role_for_unit_with_http_info(id, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_role_for_unit_with_http_info(id, user_id, **kwargs)  # noqa: E501
            return data

    def get_role_for_unit_with_http_info(self, id, user_id, **kwargs):  # noqa: E501
        """get_role_for_unit  # noqa: E501

        Returns the highest role for the specified user for the specific unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_role_for_unit_with_http_info(id, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The `_id` of the unit. (required)
        :param str user_id: The `_id` of the user. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_role_for_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_role_for_unit`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_role_for_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit/{id}/role/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_unit(self, id, **kwargs):  # noqa: E501
        """get_unit  # noqa: E501

        Returns the detail for the specified unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unit(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The `_id` of the unit. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_unit_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_unit_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_unit_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_unit  # noqa: E501

        Returns the detail for the specified unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_unit_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The `_id` of the unit. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Unit',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_units(self, **kwargs):  # noqa: E501
        """list_units  # noqa: E501

        List or search the user's units.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_units(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sort: The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-creator`). 
        :param int limit: Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100` 
        :param int offset: The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned. 
        :param str before: Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded. 
        :param str after: Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). 
        :param str fields: Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query. 
        :param str name: Limits the result set to items with this exact name (case insensitive).
        :param str creator: Limits the result set to items created by the user with this username.
        :param bool deleted: Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items. 
        :param bool public: Toggles the result set between public and private data. Default value is `false`
        :return: Units
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_units_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_units_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_units_with_http_info(self, **kwargs):  # noqa: E501
        """list_units  # noqa: E501

        List or search the user's units.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_units_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sort: The sort order to use for the result set. To sort in descending order, prefix the field name with a dash(`-`). A comma separated list may be used to sort by more than one field (e.g. `name,-creator`). 
        :param int limit: Limits the number of records returned to the given value. Maximum value is `1000`. Default value is `100` 
        :param int offset: The number of records to skip from the beginning of the result set. If the offset value provided is greater than the number of available records, an empty result set will be returned. 
        :param str before: Limits the result set to items created on, or before, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). Used to prevent subsequent pages of results from including records that were created       since the first page of results was loaded. 
        :param str after: Limits the result set to items created on, or after, the specified timestamp (for example ISO, `2017-10-10T15:53:48.998Z`). 
        :param str fields: Modifies the result set to exclude or include the specified fields. E.g: To return only the the name and created fields use `fields=name,created`. To exclude the name and created fields from the results use `fields=-name,-created`. Inclusion and exclusion options can not be set in the same query. 
        :param str name: Limits the result set to items with this exact name (case insensitive).
        :param str creator: Limits the result set to items created by the user with this username.
        :param bool deleted: Toggles the result set between deleted and non-deleted items. Default value is `false`, to only show non-deleted items. 
        :param bool public: Toggles the result set between public and private data. Default value is `false`
        :return: Units
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'limit', 'offset', 'before', 'after', 'fields', 'name', 'creator', 'deleted', 'public']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_units" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'creator' in params:
            query_params.append(('creator', params['creator']))  # noqa: E501
        if 'deleted' in params:
            query_params.append(('deleted', params['deleted']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/units', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Units',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def share_unit(self, body, id, **kwargs):  # noqa: E501
        """share_unit  # noqa: E501

        Share an existing unit with a user, team, or organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.share_unit(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShareUnitBody body: A JSON object containing the necessary properties to share the unit. (required)
        :param str id: The `_id` of the unit to share. (required)
        :return: SuccessfullyShare
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.share_unit_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.share_unit_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def share_unit_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """share_unit  # noqa: E501

        Share an existing unit with a user, team, or organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.share_unit_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ShareUnitBody body: A JSON object containing the necessary properties to share the unit. (required)
        :param str id: The `_id` of the unit to share. (required)
        :return: SuccessfullyShare
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method share_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `share_unit`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `share_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit/{id}/accessible-to', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessfullyShare',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unshare_unit(self, body, id, principal_id, **kwargs):  # noqa: E501
        """unshare_unit  # noqa: E501

        Revoke access to an existing unit from a user, team, or organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unshare_unit(body, id, principal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnshareUnitBody body: A JSON object containing the necessary properties to revoke access to the unit. (required)
        :param str id: The `_id` of the unit to be revoked access to. (required)
        :param str principal_id: The `_id` of the entity being revoked access to the unit. (required)
        :return: SuccessfullyUnshared
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unshare_unit_with_http_info(body, id, principal_id, **kwargs)  # noqa: E501
        else:
            (data) = self.unshare_unit_with_http_info(body, id, principal_id, **kwargs)  # noqa: E501
            return data

    def unshare_unit_with_http_info(self, body, id, principal_id, **kwargs):  # noqa: E501
        """unshare_unit  # noqa: E501

        Revoke access to an existing unit from a user, team, or organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unshare_unit_with_http_info(body, id, principal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnshareUnitBody body: A JSON object containing the necessary properties to revoke access to the unit. (required)
        :param str id: The `_id` of the unit to be revoked access to. (required)
        :param str principal_id: The `_id` of the entity being revoked access to the unit. (required)
        :return: SuccessfullyUnshared
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id', 'principal_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unshare_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `unshare_unit`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `unshare_unit`")  # noqa: E501
        # verify the required parameter 'principal_id' is set
        if ('principal_id' not in params or
                params['principal_id'] is None):
            raise ValueError("Missing the required parameter `principal_id` when calling `unshare_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'principal_id' in params:
            path_params['principalId'] = params['principal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit/{id}/accessible-to/{principalId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessfullyUnshared',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_unit(self, body, id, **kwargs):  # noqa: E501
        """update_unit  # noqa: E501

        Update an existing unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_unit(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUnitBody body: A JSON object containing the necessary properties to update the unit. (required)
        :param str id: The `_id` of the unit to update. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_unit_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_unit_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_unit_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """update_unit  # noqa: E501

        Update an existing unit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_unit_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUnitBody body: A JSON object containing the necessary properties to update the unit. (required)
        :param str id: The `_id` of the unit to update. (required)
        :return: Unit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_unit`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/unit/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Unit',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
