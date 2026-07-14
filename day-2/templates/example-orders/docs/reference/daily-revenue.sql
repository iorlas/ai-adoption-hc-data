-- Reference implementation: daily net revenue.
-- Copy this pattern for any orders reporting query.
-- Demonstrates the two decisions in code: integer money (ADR 0001) and status via the lookup FK (ADR 0002),
-- computed set-based (no row-by-row).

SELECT
    CAST(o.placed_at AS date)                       AS order_date,
    COUNT(*)                                        AS orders,
    SUM(o.total_minor)                              AS gross_minor,   -- pence; divide by 100 for display
    SUM(CASE WHEN s.is_refunded = 0
             THEN o.total_minor ELSE 0 END)         AS net_minor
FROM dbo.[order]      AS o
JOIN dbo.order_status AS s
      ON s.code = o.status            -- ADR 0002: join the lookup, never compare status strings
WHERE o.placed_at >= @from
  AND o.placed_at <  @to
GROUP BY CAST(o.placed_at AS date)
ORDER BY order_date;
