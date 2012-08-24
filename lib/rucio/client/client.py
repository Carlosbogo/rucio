# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Thomas Beermann, <thomas.beermann@cern.ch>, 2012
# - Vincent Garonne,  <vincent.garonne@cern.ch> , 2011

"""
Client class for callers of the Rucio system
"""

from rucio.client.accountclient import AccountClient
from rucio.client.rseclient import RSEClient
from rucio.client.scopeclient import ScopeClient
from rucio.client.pingclient import PingClient


class Client(AccountClient, RSEClient, ScopeClient, PingClient):

    """Main client class for accessing Rucio resources. Handles the authentication."""

    def __init__(self, rucio_host=None, auth_host=None, account=None, ca_cert=None, auth_type=None, creds=None, timeout=None):
        """
        Constructor for the Rucio main client class.

        :param rucio_host: the host of the rucio system.
        :param auth_host: the host of the rucio authentication server.
        :param account: the rucio account that should be used to interact with the rucio system.
        :param ca_cert: the certificate to verify the server.
        :param auth_type: the type of authentication to use (e.g. userpass, x509 ...)
        :param creds: credentials needed for authentication.
        :param timeout: Float describes the timeout of the request (in seconds).
        """
        super(Client, self).__init__(rucio_host=rucio_host, auth_host=auth_host, account=account, ca_cert=ca_cert, auth_type=auth_type, creds=creds, timeout=timeout)
