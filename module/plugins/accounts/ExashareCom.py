# -*- coding: utf-8 -*-

from module.plugins.internal.XFSAccount import XFSAccount


class ExashareCom(XFSAccount):
    __name__    = "ExashareCom"
    __type__    = "account"
    __version__ = "0.01"

    __description__ = """Exashare.com account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Walter Purcaro", "vuolter@gmail.com")]


    HOSTER_DOMAIN = "exashare.com"
