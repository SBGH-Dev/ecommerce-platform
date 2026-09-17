# Ecommerce Database Design

Legend:

- [x] Implemented and migrated
- [ ] Planned
- [~] Partially implemented

## accounts

### [~] User

Purpose:
Customer and merchant authentication.

Current implementation:

- id — inherited primary key
- email — unique login identifier
- password — Django-managed password hash
- first_name — inherited
- last_name — inherited
- phone
- role — CUSTOMER / OWNER / ADMIN / STAFF
- is_email_verified
- is_active — inherited
- is_staff — inherited
- is_superuser — inherited
- last_login — inherited

Planned but not implemented:

- is_phone_verified
- created_at
- updated_at

Authentication:

- username removed
- USERNAME_FIELD = "email"
- CustomUserManager used

---

## store

### [~] StoreSettings

Purpose:
Configuration for the single store represented by this deployment/database.

Current implementation:

- id
- store_name
- email
- phone
- currency — default SAR
- address

Planned additions:

- description
- logo
- favicon
- primary_color
- secondary_color
- whatsapp
- social URLs
- tax_enabled
- tax_percentage
- delivery_enabled
- minimum_order_amount
- created_at
- updated_at

Important rule:
One deployment = one store.

---

## catalog

### [ ] Category

Planned:

- id
- name
- slug
- description
- image
- is_active
- sort_order
- created_at
- updated_at

### [ ] Product

Planned:

- id
- category_id -> Category
- name
- slug
- description
- base_price
- sku
- is_active
- is_featured
- created_at
- updated_at
