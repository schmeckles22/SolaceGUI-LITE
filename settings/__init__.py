#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017-2018, The Sumokoin Project (www.sumokoin.org)
'''
App top-level settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging
import socket

from utils.common import getHomeDir, makeDir

USER_AGENT = "Solace Remote Wallet"
APP_NAME = "Solace Remote Wallet"
VERSION = [0, 0, 1]


_data_dir = makeDir(os.path.join(getHomeDir(), 'SolaceRemote'))
DATA_DIR = _data_dir






log_file  = os.path.join(DATA_DIR, 'logs', 'app.log') # default logging file
log_level = logging.DEBUG # logging level

seed_languages = [("0", "English"), 
                  ("1", "Spanish"), 
                  ("2", "German"), 
                  ("3", "Italian"), 
                  ("4", "Portuguese"),
                  ("5", "Russian"),
                  ("6", "Japanese"),
                ]

# COIN - number of smallest units in one coin
COIN = 10000000.0

WALLET_RPC_PORT = 19999
WALLET_RPC_PORT_SSL = 20000
# DNS Resolve , Fixes a few issues for us
nodeserver = socket.gethostbyname('remote-node.solace-coin.com')
REMOTE_DAEMON_HOST = nodeserver
REMOTE_DAEMON_PORT = 22222
REMOTE_DAEMON_SSL_PORT = 22226
REMOTE_DAEMON_ADDRESS = "%s:%s" % (REMOTE_DAEMON_HOST, REMOTE_DAEMON_PORT)
REMOTE_DAEMON_SSL_ADDRESS = "%s:%s" % (REMOTE_DAEMON_HOST, REMOTE_DAEMON_SSL_PORT)

RESOURCES_PATH = "../Resources" if sys.platform == 'darwin' and hasattr(sys, 'frozen') else "./Resources"
CA_CERTS_PATH = RESOURCES_PATH + "/certs/cacert-2018-03-07.pem"