# Data dictionary — `donor`

> One row per column: what it means, its type, the rule that makes a value *valid*, and a **masked**
> sample. The valid-range column is what turns "check the data" into a checkable task. **Never put a
> real NHS number / name / DOB here — mask every sample.**

| Column | Type | Meaning | Valid range / rule | Sample (masked) |
|---|---|---|---|---|
| `nhs_number` | CHAR(10) | UK NHS identifier (PII) | 10 digits, passes Modulus-11 checksum | `999••••••3` |
| `status` | VARCHAR(20) | Registration state | one of: Active, Suspended, Withdrawn, Deferred | `Active` |
| `date_of_birth` | DATE | DOB (PII) | age at `registered_date` in **16–30** | `19••-••-••` |
| `registered_date` | DATE | Date joined the registry | not in the future; ≥ 2016 | `20••-••-••` |
| `email` | NVARCHAR(120) | Contact (PII) | present; valid email shape | `a•••@example.com` |
| ... | | *(fill the remaining columns the same way)* | | |

<!--
FILL ME: complete every column of the donor table. Ask Claude:
  "@day-1/data/donor.csv describe each column, its likely type, and the rule that would make a value
   valid. Give me a masked sample for any PII column — never a real value."
Then verify against the CSV yourself before committing. The valid-range column is the payoff: it is
what a data-quality check reads.
-->
