# HeavyQueensProblem
AI Assignment 1

## Instructions

`Note: The function to use input file requires python3. So please make sure that you are running it in python3`

To run the program, arguments are as follows:
1. Name of csv file to be used
2. Algorithm to be used:

      Use 1 for A* algorithm
      
      Use 2 for Hill Climb algorithm

3. Heuristic to be implemented
  
    Currently H1 and H2 are the heuristics. For more details, please visit the [assignment page](https://docs.google.com/document/d/1rH2Cmk5KzQ7_EN9-3wJejrr8PcwbdFwpYUoCDd6_OPU/edit)

Example run:
```bash
python3 main.py heavy_queens_board.csv 2 H1
```

## Testing the code

#### Use Random Generated Board
To test the maximum number of board which can be solved, please un/comment following lines in the `def main(argv)` from main.py file
```python
    queens = createBoard(argv[0])     # Generates the random board of given length
    # queens = getDemoBoard(argv[0])  # Uses the board from csv file given
```

For this, you will also need to change the way you give the arguments to run the program. The first argument should be the number of rows in the board.
Example:
```bash
python3.5 main.py 11 2 H2

```

#### Use Simulated Annealing instead of Random Restarts
To use simulated Annealing, please un/comment fillowing lines in the `def main(argv)` from main.py file
```python
        # hill_solver.solve()                 # Uses Random Restarts to solve the board
        hill_solver.solveSimulatedAnnealing() # Uses Simulated Annealing to solve the board
```
