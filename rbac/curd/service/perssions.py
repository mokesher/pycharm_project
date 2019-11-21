



def initial_session(user,request):
    # 方案1
    # permissions = user.roles.all().values("permissions__url").distinct()
    #
    # permission_list = []
    #
    # for item in permissions:
    #     permission_list.append(item["permissions__url"])
    # print(permission_list)
    # request.session["permission_list"] = permission_list

    # 方案2
    permissions = user.roles.values("permissions__url","permissions__group_id","permissions__action").distinct()
    permission_dict = {}
    for item in permissions:
        gid = item["permissions__group_id"]
        if gid in permission_dict:
            permission_dict[gid]["urls"].append(item["permissions__url"])
            permission_dict[gid]["actions"].append(item["permissions__action"])
        else:
            permission_dict[gid] = {
                "urls": [item["permissions__url"]],
                "actions": [item["permissions__action"],],
            }

    request.session["permission_dict"] = permission_dict

    menu_permission_list = []
    permissions = user.roles.values("permissions__url", "permissions__action", "permissions__group__title").distinct()
    for item in permissions:
        if item["permissions__action"] == "list":
            menu_permission_list.append((item["permissions__url"], item["permissions__group__title"]))

        print(menu_permission_list)

    request.session["menu_permission_list"] = menu_permission_list
