#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/etc", "etc/calamares")
    pisitools.insinto("/etc", "etc/conf.d")
    pisitools.insinto("/etc", "etc/profile.d")
    pisitools.insinto("/usr/share/applications", "usr/share/applications/kedi-install.desktop")
    pisitools.insinto("/usr/share/polkit-1/rules.d", "usr/share/polkit-1/rules.d/49-kedi-live.rules")
