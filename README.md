# SAT

A simple Python module for the 3SAT problem.

## Usage
This module implements two classes:
* Boolean clauses
* Boolean CNF formulas

In order to load the module simple import it:
```python
from sat import *
```

### Clause

The general syntax for creating a clause is:

```python
cl = Clause(pos_mask, neg_mask, n)
```

Where `n` is the number of variables in the clause, and `pos_mask, neg_mask` represent the positive (resp. negative) variables in the clause using a length `n` bit mask.

For example, say `n = 5` and we want to represent the clause `x_1 v !x_0 v x_4`, then we represent the positive variables via `pos_mask = 2**1 + 2**4` and the negative mask via `neg_mask = 2**0`.

So we would initialize the clause as follows:
```python
cl = Clause(18, 1, 5)
```

### Formula

A formula is simply the conjunction of one or more clause. Given a sequence `clauses = {cl_1, ..., cl_k}` of clauses, we initialize the formula `cl_1 ^ cl_2 ^ ... ^ cl_k` as follows:

```python
F = Formula(clauses)
```

### Full example
The following snippet constructs the formula `F = (x_1 v x_2 v x_3) ^ (!x_2 v x_3 v x_4)` over `5` variables:
```python
cl1 = (7, 0, 5)
cl2 = (24, 4, 5)
F = Formula([cl1, cl2])
```

## Functionality
In what follows, let `F` be a formula and `cl` be a clause. Things you can do with this module include:

### Assignment testing a clause:

```python
assignment = (pos_mask, neg_mask) # Same representation as for the clause
cl(assignment) # Evaluate clause over assignment
F(assignment) # Evaluate formula over assignment
```

### Random elements:
```python
cl = Clause.random(n) # Random 3-variable clause over n variables
F = Formula.random(n, k) # Random 3CNF formula with k clauses over n variables
ass = Formula.random_assignment(n) # Random assignment of n variables
ass_hash = Formula.random_hashed(n) # Random 2-wise indpendent assignment
```

### Brute force solutions:
```python
sol = F.brute_force() # Return solution for a formula F usign brute force search in (pos_mask, neg_mask) format
count = F.brute_force(count=True) # Count number of solutions to a formula F
```

### Approximations:
```python
apx_cnt = F.approximate_count() # Count probability of acceptance for random assignment
apx_sat = F.approximate_sat() # Count avg. number of accepted clause in random assignment
max_sat = F.approximate_sat(avg=False) # Count max number of accepted clause in random assignment
```

## License
This project is distributed under the Apache license version 2.0 (see the LICENSE file in the project root).
