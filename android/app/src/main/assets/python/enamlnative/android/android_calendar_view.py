'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on May 20, 2017

@author: jrm
'''
from atom.api import Typed, set_default

from datetime import datetime
from enamlnative.widgets.calendar_view import ProxyCalendarView

from .android_frame_layout import AndroidFrameLayout, FrameLayout
from .bridge import JavaMethod, JavaCallback


class CalendarView(FrameLayout):
    __javaclass__ = set_default('android.widget.CalendarView')
    setDate = JavaMethod('long')
    setMinDate = JavaMethod('long')
    setMaxDate = JavaMethod('long')
    setFirstDayOfWeek = JavaMethod('int')
    setOnDateChangeListener = JavaMethod('android.widget.CalendarView$OnDateChangeListener')

    #: This is not actually a CalendarView method, but still works
    onSelectedDayChange = JavaCallback('android.widget.CalendarView', 'int', 'int', 'int')


class AndroidCalendarView(AndroidFrameLayout, ProxyCalendarView):
    """ An Android implementation of an Enaml ProxyCalendarView.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(CalendarView)

    # --------------------------------------------------------------------------
    # Initialization API
    # --------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying widget.

        """
        self.widget = CalendarView(self.get_context())

    def init_widget(self):
        """ Initialize the underlying widget.

        """
        super(AndroidCalendarView, self).init_widget()
        d = self.declaration
        self.set_date(d.date)
        if d.min_date:
            self.set_min_date(d.min_date)
        if d.max_date:
            self.set_max_date(d.max_date)
        self.set_first_day_of_week(d.first_day_of_week)

        #: Setup listener
        self.widget.setOnDateChangeListener(self.widget.getid())
        self.widget.onSelectedDayChange.connect(self.on_selected_day_change)

    # --------------------------------------------------------------------------
    # OnDateChangeListener API
    # --------------------------------------------------------------------------
    def on_selected_day_change(self, view, year, month, day):
        d = self.declaration
        dt = datetime(year, month+1, day)
        with self.widget.setDate.suppressed():
            d.date = (dt - datetime(1970, 1, 1)).total_seconds()

    # --------------------------------------------------------------------------
    # ProxyCalendarView API
    # --------------------------------------------------------------------------
    def set_date(self, date):
        self.widget.setDate(date)

    def set_min_date(self, date):
        self.widget.setMinDate(date)

    def set_max_date(self, date):
        self.widget.setMaxDate(date)

    def set_first_day_of_week(self, day):
        self.widget.setFirstDayOfWeek(day)
