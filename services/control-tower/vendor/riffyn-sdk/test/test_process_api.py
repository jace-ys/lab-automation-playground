# coding: utf-8

"""
    Riffyn REST API

    ### Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ### Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ### Authentication Begin with a call the [authenticate](/#api-Authentication-authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your prefered token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](/#api-Authentication-verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn App UI.  ### Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ### Postman endpoint examples There is a YAML file with the examples of the request on Riffyn API [Click here](/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ### Client SDKs You may write your own API client, or you may use one of ours. [Click here](/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.process_api import ProcessApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProcessApi(unittest.TestCase):
    """ProcessApi unit test stubs"""

    def setUp(self):
        self.api = api.process_api.ProcessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_connection(self):
        """Test case for add_connection

        """
        pass

    def test_add_process_comment(self):
        """Test case for add_process_comment

        """
        pass

    def test_add_tag_to_process(self):
        """Test case for add_tag_to_process

        """
        pass

    def test_create_group(self):
        """Test case for create_group

        """
        pass

    def test_create_process(self):
        """Test case for create_process

        """
        pass

    def test_delete_connection(self):
        """Test case for delete_connection

        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        """
        pass

    def test_delete_process(self):
        """Test case for delete_process

        """
        pass

    def test_delete_process_comment(self):
        """Test case for delete_process_comment

        """
        pass

    def test_delete_tag_from_process(self):
        """Test case for delete_tag_from_process

        """
        pass

    def test_duplicate_process(self):
        """Test case for duplicate_process

        """
        pass

    def test_export_to_enclosing_group(self):
        """Test case for export_to_enclosing_group

        """
        pass

    def test_get_group(self):
        """Test case for get_group

        """
        pass

    def test_get_process(self):
        """Test case for get_process

        """
        pass

    def test_get_process_comment(self):
        """Test case for get_process_comment

        """
        pass

    def test_get_process_version(self):
        """Test case for get_process_version

        """
        pass

    def test_get_role_for_process(self):
        """Test case for get_role_for_process

        """
        pass

    def test_get_upload_config(self):
        """Test case for get_upload_config

        """
        pass

    def test_get_upload_config_collection(self):
        """Test case for get_upload_config_collection

        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        """
        pass

    def test_list_process_comments(self):
        """Test case for list_process_comments

        """
        pass

    def test_list_process_tags(self):
        """Test case for list_process_tags

        """
        pass

    def test_list_process_versions(self):
        """Test case for list_process_versions

        """
        pass

    def test_list_processes(self):
        """Test case for list_processes

        """
        pass

    def test_list_replies_to_process_comment(self):
        """Test case for list_replies_to_process_comment

        """
        pass

    def test_list_upload_config_collections(self):
        """Test case for list_upload_config_collections

        """
        pass

    def test_list_upload_configs(self):
        """Test case for list_upload_configs

        """
        pass

    def test_reply_to_process_comment(self):
        """Test case for reply_to_process_comment

        """
        pass

    def test_share_process(self):
        """Test case for share_process

        """
        pass

    def test_unshare_process(self):
        """Test case for unshare_process

        """
        pass

    def test_update_group(self):
        """Test case for update_group

        """
        pass

    def test_update_process(self):
        """Test case for update_process

        """
        pass

    def test_update_process_comment(self):
        """Test case for update_process_comment

        """
        pass


if __name__ == '__main__':
    unittest.main()
