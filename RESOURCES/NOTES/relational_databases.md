## Notes on relational databases

 * Relational Algebra select σ(Expr) = SQL where; eliminates rows
 * Relational Algebra project π(Expr) = SQL select; eliminates columns
 * Relational Algebra rename ρ(Expr) = SQL ~as; unifies schemas and disambiguates in self-joins
 * Relational Algebra relation = SQL table
 * Relational Algebra attribute = SQL column, field
 * Relational Algebra row = SQL row, record
 * Relational Algebra composing: π(σ); there is no need to compose the same type of operator
 * natural join ⨝ requires: attributes to be the same

[end]