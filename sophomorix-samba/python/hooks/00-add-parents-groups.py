#! /usr/bin/env python3

# This script is part of the sophomorix project and intended to add
# CN group of parents for new students
# DO NOT EDIT OR REMOVE IT !

import sys
from linuxmusterTools.common import *
from linuxmusterTools.ldapconnector import LMNLdapReader as lr, LMNUserWriter


epoch = sys.argv[1]
school = sys.argv[2]

uw = LMNUserWriter()

if epoch is None:
    updates = parse_update_log(today=True)
    timestamps = list(updates.keys())
    timestamps.sort()
    epoch = timestamps[-1]
    entries = updates[epoch]
else:
    entries = parse_add_log(epoch=epoch)

for entry in entries:
    user = entry["user"]
    role = entry["role"]
    lprint.info(f"Checkng user {user}")
    if role == 'student':
        uw.add_parent_group(user)


