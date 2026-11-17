#!/usr/bin/python

import os

def booted_openrc():
    try:
        root = os.stat("/")
        init_root = os.stat("/proc/1/root")
    except OSError:
        return False
    same = (root.st_dev, root.st_ino) == (init_root.st_dev, init_root.st_ino)
    return same and os.path.isdir("/run/openrc")

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
    os.system("rc-update add mkinitcpio default >/dev/null 2>&1")
    if booted_openrc():
        os.system("rc-service mkinitcpio start >/dev/null 2>&1")

def preRemove():
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
    os.system("rc-update del mkinitcpio default >/dev/null 2>&1")
