# CSCE-2120.001 Project
## Ben Nelson

This repository explores fundamental Linear Algebra. It covers vectors and geometric representations, matrices, linear systems, vector spaces, and determinants. Each module demonstrates a Python-coded implementation of the concepts of that chapter. 

| Module | Topic                                      | Example Implementation |
|--------|--------------------------------------------|-------|
| 1      | Vectors and Linear Models                  | `add_vectors(u, v)`      |
| 2      | Geometry of Vectors in 2D and 3D           | `dot_product(u, v)`      |
| 3      | Row Operations and Solution Sets            | `gauss_jordan_elimination(augmented)`      |
| 4      | Matrix Algebra                              | `matrix_multiply(A, B)`      |
| 5      | Inverses, Elementary, and Block Matrices    | `inverse_via_gauss_jordan(matrix)`      |
| 6      | Matrix Factorization and Applications       | `elimination_multiplier`      |
| 7      | Vector Spaces and Bases                     | `is_linearly_independent(vectors)`      |
| 8      | Structure of Linear Systems                 | `four_subspace_bases(matrix)`      |
| 9      | Determinants and Invertibility              | `determinant_cofactor(matrix)`      |

To run these programs, first be in their folder. Then, compile with `python3 -m py_compile main.py`. Lastly, run it with `python3 main.py`.

This project was one of my first projects to investigate "theoretical" mathematics. Many concepts, like span and invertibility, exist differently than in previous CS mathematics. Even compared to things like discrete math (which is much easier to implement in my opinion), the topics here were harder to wrap my head around at times. Having it operate in code helped my understanding very much.

AI assistance was only used for clarification and debugging (sometimes with Zybook's slightly janky labs software...), with no write permissions.
