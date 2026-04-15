# sudoku_csp_solver
Backtracking Performance Analysis
1. Easy Board
Backtrack Calls: 1
Failures: 0
The easy board was solved almost instantly with only one backtrack call and no failures. Since many values were already filled in, the AC-3 algorithm quickly reduced the possible options for the remaining cells. Because of this, the solver did not need to guess or backtrack — it directly reached the correct solution.

2. Medium Board
Backtrack Calls: 26
Failures: 0
The medium board also performed efficiently. Although it required more steps than the easy board, there were still no failures. This shows that AC-3 along with forward checking and the MRV heuristic worked well to guide the solver. The algorithm was able to choose the right values without going down incorrect paths.

3. Hard Board
Backtrack Calls: 62
Failures: 8
For the hard board, the number of backtrack calls increased and some failures occurred. This is because the puzzle had fewer initial values, so constraint propagation alone was not enough. The solver had to try different possibilities, and some of these led to wrong paths, which caused backtracking before finding the correct solution.

4. Very Hard Board
Backtrack Calls: 153
Failures: 97
The very hard board required the most effort to solve. With very few given numbers, AC-3 could not simplify the problem much at the start. As a result, the backtracking algorithm had to explore many possibilities. It made several wrong choices, hit dead ends, and then backtracked multiple times before reaching the final correct solution.

As the difficulty of the Sudoku increases, both backtrack calls and failures also increase because the solver has fewer constraints to guide it and must rely more on trial and error.
