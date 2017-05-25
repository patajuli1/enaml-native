'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''
from atom.api import (
    Typed, ForwardTyped, Int, Bool, Enum, observe
)

from enaml.core.declarative import d_

from .frame_layout import FrameLayout, ProxyFrameLayout

class ProxyScrollView(ProxyFrameLayout):
    """ The abstract definition of a proxy Label object.

    """
    #: A reference to the Label declaration.
    declaration = ForwardTyped(lambda: ScrollView)


class ScrollView(FrameLayout):
    """ A simple control for displaying read-only text.

    """
    #: A reference to the ProxyLabel object.
    proxy = Typed(ProxyScrollView)