# Mutation Testing for Source Code

## Source Code used for Testing

Source Code Link: https://github.com/samuelabidemi/Python-Scientific-Calculator.git

The Source Code used for this project is of a Scientific Calculator written in Python. The Calculator implements 23 functions for various calculations including Permutations, Combinations, Ciel, Floor, GCD, Fmod, Factorial, Sqrt, LCM, Roots, etc. The other methods like Sine, Cosine, Tan, Logarithm, etc were also implemented using the inbuilt math library in Python.

To run the project, we can use the command 
```
python Calculator_2.py
```
## Test Case Strategies and Testing Tools

For this project, we have used the strategy of Mutation Testing for Source Code. We have used unittest - a unit testing framework for Python for the test cases and the open source testing tool used for this project was MutPy (version 0.6.1).

### Installations
The following installations need to be done before running the test cases and implementing mutation testing.

```
pip install unittest mutpy numpy mock sympy
```

### Run Command

To run all the unit test cases (enclosed in the Python file named test.py), the following command can be used:

```
python -m unittest test.py
```

To implement mutation testing using MutPy, the following command is to be used:

```
mut.py --target Calculator_2.py --unit-test test.py -m --runner unittest [--report-html DIR_NAME] //Optional command to generate an HTML file consisting of a detailed report
```

### Test Cases
A total of 24 test cases were written for unit testing.

### Mutation Operators used

The following mutation operators were used:

1.ROR (Relational Operator Replacement)
2.CRP (Constant Replacement)
3.COI (Conditional Operator Insertion)
4.ASR (Assignment Operator Replacement)
5.AOR (Arithmetic Operator Replacement)
6.AOD (Arithmetic Operator Deletion)

### Results
A total of 203 mutants were generated out of which 42 mutants were strongly killed with a Mutation Score of 22.2%. We were able to target 4 different classes of mutation operators, namely Relational, Conditional, Arithmetic, Assignment Operators, and Constants. The detailed report for the same can be viewed in the HTML file namely "index.html" in the Mutation_Documentation folder.

### Individual Contribution
Each of the team member was responsible to create unit test cases for the 14 functions keeping in mind which operator could be used for mutation testing, and on the basis of that, the 14 functions were chosen for testing. Following is the contribution of each of the team member:
- Jyotsna Tata (MT2020020): LCM, Permutation, Floor, Ceil
- Simran Basu (MT2020145): Factorial, Combination, Sin, Cos, Tan, Sqrt
- Md. Jawed Aqueeb (MT2020110): Roots, GCD, Log, Fmod
