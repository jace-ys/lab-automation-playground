# coding: utf-8

"""
    Riffyn Nexus REST API V1

    ## Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ## Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ## Authentication Begin with a call the [authenticate](#/authentication/authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn Nexus App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn Nexus API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your preferred token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](#/authentication/verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn Nexus App UI.  ## Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ## Postman endpoint examples There is a YAML file with the examples of the request on Riffyn Nexus API [Click here](/v1/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ## Client SDKs You may write your own API client, or you may use one of ours. [Click here](/v1/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 4.2.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import riffyn_nexus_sdk_v1
from riffyn_nexus_sdk_v1.models.upload_configs import UploadConfigs  # noqa: E501
from riffyn_nexus_sdk_v1.rest import ApiException


class TestUploadConfigs(unittest.TestCase):
    """UploadConfigs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUploadConfigs(self):
        """Test UploadConfigs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = riffyn_nexus_sdk_v1.models.upload_configs.UploadConfigs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
