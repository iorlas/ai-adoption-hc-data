# Glossary — domain terms

> Terms Claude can't infer from the schema, and vocabulary it might "helpfully" flag as wrong. One line
> each. The cheapest, highest-leverage doc you own.

| Term | Means |
|---|---|
| **GMV** | Gross merchandise value — total order value before refunds and cancellations. |
| **net vs gross** | Gross = before refunds and discounts; net = after. Report both, never conflate them. |
| **fulfilment** | The pick/pack/ship step; an order is *fulfilled* once `fulfilled_at` is set. |
| **minor units** | The smallest currency unit (pence for GBP). Money is stored as integer minor units — see ADR 0001. |
