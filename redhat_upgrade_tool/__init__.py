# __init__.py for the system upgrade python package
#
# Copyright (C) 2012 Red Hat Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Will Woods <wwoods@redhat.com>

'''
NOTE WELL, DEAR READER: None of this is intended as a public API!  I reserve
the right to change anything and everything about how this library works at the
merest whim.

If you're actually trying to write something that uses this library, please
contact me (or whatever people/constructs are maintaining this after I quit
computers forever) to discuss how we could best design a sensible API that
would actually work for you.

Your pal,
-w
'''

import logging
log = logging.getLogger(__package__)
log.addHandler(logging.NullHandler())

import gettext
t = gettext.translation(__package__, "/usr/share/locale", fallback=True)
_ = t.lgettext

kernel_id = "redhat-upgrade-tool"
# NOTE: new-kernel-pkg requires this kernel name/path
kernelpath = '/boot/vmlinuz-%s' % kernel_id
initrdpath = '/boot/initramfs-%s.img' % kernel_id

cachedir = '/var/tmp/system-upgrade'
packagedir = '/var/lib/system-upgrade'
packagelist = packagedir + '/package.list'
upgradeconf = packagedir + '/upgrade.conf'
upgradelink = '/system-upgrade'
upgraderoot = '/system-upgrade-root'

mirrormanager = ''
defaultkey = ''

update_img_dir = '/etc/' + __package__ + '/update.img.d'

# FIXME: there is probably a better way to do this than hardcoding it
# This key id is used with RHEL-7.0 GA
rhel_gpgkey_id = 'fd431d51-4ae0493b'
rhel_gpgkey_path = 'file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release'
