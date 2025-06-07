# Toy Robot Simulator

A simple toy robot that moves around on a configurable table. You can place it, move it around, turn it, and ask where it is.

## What it does

The robot sits on a square table and you can control it with basic commands. It won't fall off the table (it just ignores commands that would make it fall). By default the table is 5x5, but you can configure it to any size you want.

## Setup

Install dependencies (optional - only needed for .env file support):
```
pip install -r requirements.txt
```

## Running it

Interactive mode:
```
python run.py
```

Or run commands from a file:
```
python run.py command.txt
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

The program works out of the box with a 5x5 table. To customize the table size:

**Option 1: Environment variables**
```bash
TABLE_WIDTH=10 TABLE_HEIGHT=8 python3 run.py
```

**Option 2: .env file** (requires `pip install python-dotenv`)
Create a `.env` file:
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

- `run.py` - Easy way to run the program
- `src/main.py` - Main program
- `src/robot.py` - Robot class  
- `src/simulator.py` - Handles commands
- `src/table.py` - Table boundaries
- `src/config.py` - Configuration loading
- `tests/` - Test files
- `command.txt` - Example commands
- `requirements.txt` - Python dependencies