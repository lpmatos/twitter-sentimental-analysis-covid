# -*- coding: utf-8 -*-

"""Documentation file twitter.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from client.twitter import TwitterClient
from typing import NoReturn, Text, Callable
from settings.configuration import Configuration

# =============================================================================
# CLASS - FUNCTIONS
# =============================================================================

class Functions(object):

    def __init__(self, logger: Callable) -> NoReturn:
        self._config = Configuration()
        self._logger = logger
        self.twitter = TwitterClient(self.config.get_env("TWITTER_CONSUMER_KEY"),
                                self.config.get_env("TWITTER_CONSUMER_SECRET"), 
                                self.config.get_env("TWITTER_ACCESS_TOKEN"), 
                                self.config.get_env("TWITTER_ACCESS_TOKEN_SECRET"), self.logger).twitter_client
    
    def search(self, **query):
        return [elemento for elemento in self.twitter.search(**query)]

    @property
    def config(self) -> Text:
        return self._config

    @property
    def logger(self) -> Text:
        return self._logger
