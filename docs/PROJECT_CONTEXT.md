# Project Context

## Current state

Django backend is initialized and running successfully.

PostgreSQL is connected through environment variables loaded from `.env`.

The project uses a custom email-based User model instead of Django's default
username-based authentication.

The first store configuration model, StoreSettings, has been created.

Both User and StoreSettings are registered and visible in Django Admin.

## Completed

- [x] Product architecture chosen
- [x] Single-store-per-deployment model chosen
- [x] Backend target structure documented
- [x] Frontend target structure documented
- [x] Authentication/OTP/order-history scope documented
- [x] Django backend initialized
- [x] PostgreSQL connected
- [x] Environment variables configured for database connection
- [x] Custom User model created
- [x] Email configured as the User login identifier
- [x] User roles added: CUSTOMER, OWNER, ADMIN, STAFF
- [x] User phone field added
- [x] Email verification flag added
- [x] CustomUserManager created
- [x] AUTH_USER_MODEL configured as accounts.User
- [x] StoreSettings model created
- [x] User registered in Django Admin
- [x] StoreSettings registered in Django Admin
- [x] Migrations created and applied successfully
- [x] Superuser created
- [x] Django Admin login tested successfully

## Current models

### accounts.User

Extends Django AbstractUser.

Fields/customizations added:

- username removed
- email is unique and used as USERNAME_FIELD
- phone
- is_email_verified
- role

Available roles:

- CUSTOMER
- OWNER
- ADMIN
- STAFF

Uses CustomUserManager for user and superuser creation.

### store.StoreSettings

Current fields:

- store_name
- email
- phone
- currency
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

Default currency is SAR.

The model prevents creation of more than one StoreSettings record while allowing the existing record to be updated.

Logo, favicon, and social URLs are intentionally postponed.

## Current configuration

Database:

PostgreSQL using environment variables:

- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

Installed project apps currently:

- accounts
- store

Custom user setting:

AUTH_USER_MODEL = "accounts.User"

## Important implementation notes

The project uses one isolated deployment and PostgreSQL database per store.
There is no multi-tenancy in V1.

StoreSettings represents configuration for the single store belonging to the
deployment.

The Django SECRET_KEY is currently development-only and should be moved to an
environment variable before production.

Email/OTP functionality has not been implemented yet.

The current MAILERS setting should be reviewed when email functionality is
implemented because Django's standard email configuration uses EMAIL_BACKEND.

## Planned build order

1. [x] Project foundation
2. [x] Initial StoreSettings

- [x] StoreSettings description added
- [x] Store contact/WhatsApp settings added
- [x] Store primary and secondary colors added
- [x] Store tax settings added
- [x] Store delivery/minimum-order settings added
- [x] StoreSettings timestamps added
- [x] StoreSettings restricted to one record
- [x] StoreSettings migrations applied successfully
- [x] CustomUserManager validates required email
- [x] Superuser creation validates staff/superuser flags

3. [ ] Category + Product
4. [ ] Improve Django Admin for catalog management
5. [ ] Basic catalog API
6. [ ] Next.js storefront
7. [ ] Customer + merchant authentication
8. [ ] OTP + password reset
9. [ ] Images + options + variants + stock
10. [ ] Customer account + addresses
11. [ ] Cart
12. [ ] Checkout + orders + order history
13. [ ] Merchant dashboard
14. [ ] Payments + webhooks + refunds
15. [ ] Discounts + notifications
16. [ ] Testing/security
17. [ ] Production deployment

## Next task

Begin the catalog domain incrementally.

Create the Category model first, understand each field and relationship,
create/apply the migration, register it in Django Admin, and test it.

After Category is working, create Product and connect it to Category.

## Learning rule

Do not paste large unexplained implementations.

Build one small piece at a time, run it, understand what Django is doing,
fix errors before continuing, and update this context after meaningful
milestones.
