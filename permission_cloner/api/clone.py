
import frappe
from frappe import _

@frappe.whitelist()
def clone_permissions(source_role, target_role):
    if not frappe.has_role("System Manager"):
        frappe.throw(_("Not permitted"))

    perms = frappe.get_all("Custom DocPerm", filters={"role": source_role}, fields="*")
    if not perms:
        return f"No permissions found for role '{source_role}'"

    copied = 0
    for perm in perms:
        exists = frappe.get_all("Custom DocPerm", filters={
            "parent": perm.parent,
            "role": target_role,
            "permlevel": perm.permlevel
        })
        if exists:
            continue

        new_perm = perm.copy()
        new_perm["role"] = target_role
        del new_perm["name"]
        frappe.get_doc(new_perm).insert()
        copied += 1

    frappe.db.commit()
    return f"✅ Cloned {copied} permissions from '{source_role}' to '{target_role}'"
