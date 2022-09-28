# GeneticOptimization

Repository for the optimization of a prestablished problem using Genetic Algorithms from scratch.

The genetic optimization algorithm exposed here is composed by 6 files:
- functions.py : Contains all the functions required for the genetic algorithm
- genes.py : Is used for the definition of the genes, here you can define the gene's name, the limits and the gene resolution
- InitPob.py : Is used for the randon generation of the initial poblation
- main.py : Used to implement the genetic algorithm. In this case a simple optimization problem is handled.
- ObjectiveFunction.py : Is used to define the objective function
- Restrictions.py : Is used to define the restrictions of the optimization problem.

For the test of the algorithm on the main.py file is define the problem to maximize the volume of a box given certatin conditions.

3 genes are defined, $a$ $b$ and $c$, each variable is between $[5, 42]$, the objective function wants to maximize the volume,
in the restrictions the variables must be greater than zero and $x+2 * y+2 *z = 72$.

In functions.py the functions for codification, selection, elitism, crossover, mutation and decodification are defined.
