'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''
import enaml
from enamlnative.android.app import AndroidApplication


app = AndroidApplication()

with enaml.imports():
    from view import ContentView
    app.content_view = ContentView()

app.start()
