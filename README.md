# Toy Robot Simulator

A simple toy robot that moves around on a configurable table. You can place it, move it around, turn it, and ask where it is.

## What it does

The robot sits on a square table and you can control it with basic commands. It won't fall off the table (it just ignores commands that would make it fall). By default the table is 5x5, but you can configure it to any size you want.

## Setup

Install dependencies:
```
pip install -r requirements.txt
```

Configure table size (optional):
1. Copy `.env.example` to `.env`
2. Edit the `TABLE_WIDTH` and `TABLE_HEIGHT` values
3. Default is 5x5 if no config file exists

## Running it

Interactive mode (type commands one by one):
```
python3 src/main.py
```

Or run commands from a file:
```
python3 src/main.py command.txt
```

## Commands

- `PLACE X,Y,DIRECTION` - Put the robot on the table at position X,Y facing DIRECTION
- `MOVE` - Move forward one space
- `LEFT` - Turn left 90 degrees  
- `RIGHT` - Turn right 90 degrees
- `REPORT` - Print current position and direction
- `EXIT` - Quit (interactive mode only)

Directions are NORTH, EAST, SOUTH, WEST.

## Example

```
PLACE 0,0,NORTH
MOVE
RIGHT  
MOVE
REPORT
```

This puts the robot at (0,0) facing north, moves it to (0,1), turns it to face east, moves it to (1,1), then prints "1,1,EAST".

## Rules

- You have to PLACE the robot first before other commands work
- Robot can't move outside the configured table boundaries
- Bad commands are just ignored
- Coordinates start from 0 and go up to (width-1, height-1)

## Configuration

Create a `.env` file to customize table size:
```
TABLE_WIDTH=10
TABLE_HEIGHT=8
```

This would create a 10x8 table with coordinates from (0,0) to (9,7).

## Testing

Run tests with:
```
pytest
```

## Files

- `src/main.py` - Main program
- `src/robot.py` - Robot class  
- `src/simulator.py` - Handles commands
- `src/table.py` - Table boundaries
- `src/config.py` - Configuration loading
- `tests/` - Test files
- `command.txt` - Example commands
- `requirements.txt` - Python dependencies