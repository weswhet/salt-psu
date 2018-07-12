# -*- coding: utf-8 -*-

import salt.utils.platform
import logging
import sys

log = logging.getLogger(__name__)

__virtualname__ = 'foo'


def __virtual__():
    if salt.utils.platform.is_darwin():
        return __virtualname__

    return (False, 'module.foo only available on macOS.')


def bar(baz):
    return __salt__['cmd.run'](baz)