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
- date_joined — inherited creation timestamp

Planned but not implemented:

- is_phone_verified — revisit during phone OTP implementation
- updated_at — add later only if needed

Authentication:

- username removed
- USERNAME_FIELD = "email"
- CustomUserManager used
- create_user requires an email
- create_superuser enforces is_staff=True and is_superuser=True

Registration rule for later API:

Customer self-registration will require:
first_name, last_name, phone, email, and password.
This will be enforced by the registration serializer.

---

## store

### [x] StoreSettings

Purpose:

Configuration for the single store represented by this deployment/database.

Current implementation:

- id
- store_name
- email
- phone
- currency — default SAR
- address
- description
- whatsapp
- primary_color
- secondary_color
- tax_enabled
- tax_percentage
- delivery_enabled
- minimum_order_amount
- created_at
- updated_at

Planned for later:

- logo
- favicon
- social URLs

Important rule:

One deployment = one store.

Only one StoreSettings record may be created.
The model's save() method prevents creation of a second record while still allowing the existing record to be updated.

---

## catalog

### [X] Category

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

### [x] Product

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
