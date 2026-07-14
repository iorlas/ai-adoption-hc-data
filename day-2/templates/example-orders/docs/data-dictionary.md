# Data dictionary — `order`

> One row per column: what it means, its type, the rule that makes a value *valid*, and a **masked**
> sample. The valid-range column is what turns "check the data" into a checkable task. Never put real
> PII here — mask every sample.

| Column | Type | Meaning | Valid range / rule | Sample (masked) |
|---|---|---|---|---|
| `order_id` | INT | Surrogate key | positive, unique | `100428` |
| `customer_email` | NVARCHAR(120) | Customer contact (PII) | present; valid email shape | `a•••@example.com` |
| `status` | TINYINT | FK to `order_status` | one of the codes in `order_status` (see ADR 0002) | `3` |
| `total_minor` | INT | Order total in **pence** | integer minor units, `>= 0`, never float (see ADR 0001) | `1299` (= £12.99) |
| `currency` | CHAR(3) | ISO 4217 code | 3 letters; a supported currency | `GBP` |
| `placed_at` | DATETIME2 | When the order was placed | not in the future | `20••-••-••` |
| `fulfilled_at` | DATETIME2 | When shipped (nullable) | `>= placed_at`, or NULL if unfulfilled | `NULL` |
