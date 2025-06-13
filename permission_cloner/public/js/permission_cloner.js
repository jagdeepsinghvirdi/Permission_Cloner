
frappe.ui.form.on('Permission Cloner', {
  refresh(frm) {
    if (frappe.user.has_role('System Manager')) {
      frm.add_custom_button('Clone Permissions', () => {
        if (!frm.doc.source_role || !frm.doc.target_role) {
          frappe.msgprint("Please select both Source and Target roles.");
          return;
        }

        frappe.call({
          method: "permission_cloner.api.clone.clone_permissions",
          args: {
            source_role: frm.doc.source_role,
            target_role: frm.doc.target_role
          },
          callback(r) {
            if (!r.exc) {
              frappe.msgprint(r.message);
            }
          }
        });
      });
    }
  }
});
