# Test Cases

| Test | Expected |
|---|---:|
| Bronze source count | 30 |
| Exact duplicates removed | 1 |
| After deduplication | 29 |
| Silver valid records | 22 |
| Quarantine records | 7 |
| Silver unique order IDs | 22 |
| Missing customers | 0 |
| Missing products | 0 |
| Quantity <= 0 | 0 |
| Unit price <= 0 | 0 |
| Invalid/null dates | 0 |

Reconciliation: 30 Bronze = 1 duplicate + 7 quarantined + 22 clean.

Known quarantine orders: 1010 negative quantity; 1011 missing customer; 1012 missing price; 1013 negative price; 1014 invalid date; 1028 zero quantity; 1029 missing product.
