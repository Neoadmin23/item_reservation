doc_events = {
    "Sales Order": {
        "on_submit": "custom_app.item_reservation.reserve_items_from_sales_order",
        "on_cancel": "custom_app.item_reservation.cancel_reservation"
    },
    "Pick List": {
        "on_submit": "custom_app.item_reservation.release_reservation_from_pick_list"
    }
}