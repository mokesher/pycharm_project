#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rbac.settings')
    import django

    django.setup()
    from curd.models import *

    user = User.objects.filter(name="root").first()
    # per = user.roles.all().values("permissions__url")

    permissions = user.roles.values("permissions__url", "permissions__group_id", "permissions__action").distinct()
    permission_dict = {}
    for item in permissions:
        gid = item["permissions__group_id"]
        if gid in permission_dict:
            permission_dict[gid]["url"].append(item["permissions__url"])
            permission_dict[gid]["actions"].append(item["permissions__action"])
        else:
            permission_dict[gid] = {
                "url": [item["permissions__url"]],
                "actions": [item["permissions__action"], ],
            }
