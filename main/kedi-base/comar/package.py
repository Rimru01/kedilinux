#!/usr/bin/python

import os
import re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    path = "/etc/default/grub"
    if not os.path.isfile(path):
        return
    with open(path) as f:
        old = f.read()
    new = re.sub(r'(?m)^GRUB_DISTRIBUTOR=.*$', 'GRUB_DISTRIBUTOR="Kedi"', old)
    new = re.sub(r'(?m)^GRUB_THEME=', '#GRUB_THEME=', new)
    if new != old:
        with open(path, "w") as f:
            f.write(new)
        os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
        os.system("grub2-mkconfig -o /boot/grub2/grub.cfg >/dev/null 2>&1")
