# window.py
#
# Copyright 2024 Claire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, GLib, Gio, Gdk, GObject
from .utils.online import check_for_updates
from .pages.firefox_page import FirefoxPage
from .pages.thunderbird_page import ThunderbirdPage

@Gtk.Template(resource_path='/dev/qwery/AddWater/gtk/window.ui')
class AddwaterWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'AddwaterWindow'

    toast_overlay = Gtk.Template.Child()
    change_confirm_bar = Gtk.Template.Child()

    firefox_page = Gtk.Template.Child()
    thunderbird_page = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO How to store user changes into a transaction that are only applied after they confirm?





