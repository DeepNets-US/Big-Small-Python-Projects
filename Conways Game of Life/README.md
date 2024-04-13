# Conway's Game of Life

## Overview

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. Despite its simple rules, the Game of Life exhibits complex behavior and is Turing complete.

## Rules

The game is played on a grid, where each cell can either be alive or dead. The game evolves in steps according to the following rules:

1. Any live cell with two or three live neighbors survives.
2. Any dead cell with exactly three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Implementation

This Python implementation of Conway's Game of Life simulates the evolution of the game on a grid of specified dimensions. The grid consists of cells, each represented by either "0" (alive) or " " (dead). The program initializes the grid with random alive or dead states and iterates through each generation, updating the state of each cell according to the game rules.

## How to Run

To run the simulation, execute the Python script `conways_game_of_life.py`. The simulation will display the evolving grid on the console, with each generation separated by a delay. You can interrupt the simulation by pressing Ctrl-C.

## File Descriptions

- `conways_game_of_life.py`: The Python script containing the implementation of Conway's Game of Life.
- `README.md`: This file, provides an overview of the game, its rules, implementation details, and instructions for running the simulation.

## Acknowledgments

This implementation is inspired by the work of John Horton Conway and his contributions to the field of recreational mathematics. The code is authored by Utkarsh Saxena (or DeepNets), based on the original concept by Conway.

## Example
![Conways game of life](https://github.com/DeepNets-US/Big-Small-Python-Projects/assets/118154709/32f5f84d-63ef-433d-b5d9-e1be09b1ee59)
