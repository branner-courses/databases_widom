## Notes on relational databases

### Relational Algebra (RA) equivalents to SQL

 * RA select σ(Expr) = SQL where; eliminates rows
 * RA project π(Expr) = SQL select; eliminates columns
 * RA rename ρ(Expr) = SQL ~as; unifies schemas and disambiguates in self-joins
 * RA relation = SQL table
 * RA attribute = SQL column, field
 * RA tuple = SQL row, record

### Definitions

 * The operators are closed over relations; their input and output are relations.
 * π and σ are idempotent: there is no need to compose the same type of operator.
 * natural join ⨝ requires: attributes to be the same; is meaningful
only when the notation by name is used
 * R ∩ S = R - (R - S)

[end]