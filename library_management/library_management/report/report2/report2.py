# Copyright (c) 2025, Nivedita and con 
import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

# Columns to show in the report
def get_columns():
    return [
        {"label": "Article Name", "fieldname": "article_name", "fieldtype": "Data", "width": 250},
        {"label": "Author", "fieldname": "author", "fieldtype": "Data", "width": 150},
        {"label": "ISBN", "fieldname": "isbn", "fieldtype": "Data", "width": 150},
       {"label": "Status", "fieldname": "status", "fieldtype": "Select", "options": "Available\nIssued", "width": 120},
        {"label": "Publisher", "fieldname": "publisher", "fieldtype": "Data", "width": 150}
    ]

# Fetch data based on filter
def get_data(filters):
    conditions = {}

    # Apply filter if selected
    if filters.get("status"):
        conditions["status"] = filters["status"]

    # Fetch articles with filter
    articles = frappe.get_all(
        "Article",
        fields=["article_name", "author", "isbn", "status", "publisher"],
        filters=conditions
    )

    return articles  # Return data directly

