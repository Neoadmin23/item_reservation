import frappe

def reserve_items_from_sales_order(doc, method):
    for item in doc.items:
        if item.delivered_by_supplier:
            continue

        reservation = frappe.new_doc("Item Reservation")
        reservation.sales_order = doc.name
        reservation.item = item.item_code
        reservation.warehouse = item.warehouse
        reservation.qty_reserved = item.qty
        reservation.status = "Reserved"
        reservation.insert()

def cancel_reservation(doc, method):
    reservations = frappe.get_all("Item Reservation", filters={"sales_order": doc.name})
    for res in reservations:
        res_doc = frappe.get_doc("Item Reservation", res.name)
        res_doc.status = "Cancelled"
        res_doc.save()

def release_reservation_from_pick_list(doc, method):
    for loc in doc.locations:
        filters = {
            "sales_order": loc.sales_order,
            "item": loc.item_code,
            "warehouse": loc.warehouse,
            "status": "Reserved"
        }
        reservations = frappe.get_all("Item Reservation", filters=filters, fields=["name", "qty_reserved"])

        for r in reservations:
            res_doc = frappe.get_doc("Item Reservation", r.name)
            if loc.qty >= res_doc.qty_reserved:
                res_doc.status = "Released"
            else:
                res_doc.qty_reserved -= loc.qty
            res_doc.save()