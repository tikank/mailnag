#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# i18n.py
#
# Copyright 2011, 2012, 2014 Patrick Ulbrich <zulu99@gmx.net>
# Copyright 2019 Timo Kankare <timo.kankare@iki.fi>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#

import locale
import gettext
from Mailnag.common.dist_cfg import PACKAGE_NAME, LOCALE_DIR

# bind textdomain for GTK Builder
locale.bindtextdomain(PACKAGE_NAME, LOCALE_DIR)

# add gettext shortcut "_" for string translations
try: 
	# Py2
	_ = gettext.translation(domain = PACKAGE_NAME, localedir = LOCALE_DIR, fallback = True).ugettext
except AttributeError:
	# Py3
	_ = gettext.translation(domain = PACKAGE_NAME, localedir = LOCALE_DIR, fallback = True).gettext

