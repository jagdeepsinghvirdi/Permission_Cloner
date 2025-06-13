import frappe
from frappe import _

@frappe.whitelist()
def clone_role_permissions(source_role, target_role):
    """
    Clone all Custom DocPerm permissions from source_role to target_role.
    Skips permissions that already exist for the target role.
    """
    source_perms = frappe.get_all(
        "Custom DocPerm",
        filters={"role": source_role},
        fields=["*"]
    )

    cloned_count = 0
    skipped_count = 0

    for perm in source_perms:
        exists = frappe.db.exists(
            "Custom DocPerm",
            {
                "parent": perm["parent"],
                "role": target_role,
                "permlevel": perm["permlevel"]
            }
        )

        if exists:
            skipped_count += 1
            continue

        new_perm = perm.copy()
        new_perm.pop("name")
        new_perm["role"] = target_role

        frappe.get_doc({
            "doctype": "Custom DocPerm",
            **new_perm
        }).insert(ignore_permissions=True)
        cloned_count += 1

    return {
        "message": _("Cloned {0} permissions. Skipped {1} (already existed).").format(cloned_count, skipped_count)
    }
