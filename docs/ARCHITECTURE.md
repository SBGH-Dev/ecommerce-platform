# Ecommerce Project — Starter Architecture

## Product decision
One reusable codebase. Each client/business receives an isolated deployment and PostgreSQL database.
No multi-tenancy for V1. The database itself represents one store.

## Stack
- Backend: Python, Django, Django REST Framework
- Database: PostgreSQL
- Frontend: Next.js + TypeScript
- Styling/UI: chosen when we initialize the frontend
- External services later: email/SMS OTP provider and payment provider

## How to read the backend
- `models.py` — database/data structure
- `serializers.py` — API input validation and output conversion
- `views.py` — receives HTTP requests and returns responses
- `services.py` — important business rules/workflows
- `urls.py` — API routes
- `permissions.py` — who may do what
- `admin.py` — Django Admin configuration
- `tests.py` — proves behavior works

## How to read the frontend
- `app/` — actual pages/routes
- `components/` — reusable visual pieces
- `features/` — feature-specific frontend behavior
- `lib/api.ts` — connection to Django
- `lib/auth.ts` — auth/session helpers
- `types/` — TypeScript descriptions of API/domain data
- `public/` — static assets

## Main customer features
Storefront, categories, product details, search, variants, cart, guest checkout,
register, login/logout, OTP verification, forgot/reset password, profile,
saved addresses, order history, order details/tracking and payments.

## Main merchant features
Merchant login, dashboard, products, categories, variants/stock, orders,
customers, discounts, staff/roles, appearance and store settings.

## Backend modules
- `accounts` — users, roles, registration/login/password flows
- `otp` — OTP challenge and verification mechanisms
- `store` — one store's configuration
- `catalog` — products/categories/variants/images/stock
- `customers` — saved customer data such as addresses
- `carts` — guest/customer carts
- `orders` — checkout results, orders, items and status history
- `payments` — payments, webhooks and refunds
- `discounts` — coupons and usage
- `notifications` — email/SMS delivery
- `common` — genuinely shared backend utilities

## Planned build order
1. Project foundation
2. StoreSettings
3. Category + Product
4. Django Admin
5. Basic catalog API
6. Next.js storefront
7. Customer + merchant authentication
8. OTP + password reset
9. Images + options + variants + stock
10. Customer account + addresses
11. Cart
12. Checkout + orders + order history
13. Merchant dashboard
14. Payments + webhooks + refunds
15. Discounts + notifications
16. Testing/security
17. Production deployment

## Rule for this repository
The starter files intentionally contain NO implementation.
We add code only when we reach that feature, and the developer should understand
what each added line does before moving on.
