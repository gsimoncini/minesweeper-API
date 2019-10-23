# minesweeper-API
minesweeper-API implemented with Python using Flask and MongoDB to store game objects.

### Run Locally
minesweeper-API needs Python 3 to run. After cloning project from github and pull the master branch please do the following tasks

##### 1. Create venv with python 3
##### 2. Install dependencies
```
    > pip install -r requirements/requirements.txt 

```
##### 3. Run docker for MongoDB
```
    > docker-compose up

```
##### 4. Run project
```
    > python run.py

```


### API Documentation

##### 1. Create Game
######`POST /game`
* Creates a new game based on the level in the request body
* The level might be Easy, Medium, Hard. 
* If the level is Easy then the game will a have a board of 8X8 cells with 10 mines
* If the level is Medium then the game will a have a board of 16X16 cells with 40 mines
* If the level is Hard then the game will a have a board of 24X24 cells with 99 mines

##### Request Body
```json
{ 
    "level": "Easy"
}
``` 

##### Response
```json
{
    "board": {
        "cells": [
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 1
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 3
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                }
            ]
        ],
        "cols": 8,
        "numberOfMines": 10,
        "rows": 8
    },
    "createdAt": "2019-10-22T12:27:29.636534",
    "finishedAt": null,
    "gameId": "5daf1fe51cd7b3ce2af9796e",
    "level": "easy",
    "status": "Started",
    "timeElapsed": null
}
``` 



##### 2. Reveal Cell
######`POST /game/<game_id>/reveal`
* Reveal the cell based on the request body row and col values
* If the game_id parameter is not valid returns 400
* If the row or col are not valid integers returns 400
* If the row or col are not valid for the game returns 400
* If the cell(row,col) is a mine then the game ends with status Lose
* If the cell(row,col) is already reveled then returns a proper message.
* If the cell is not a mine and is not revealed then:
    * The cell is revelead
    * If the cell has not mines neighbors then reveal cells neighbors recursively
    * If all cells that are not mine are revealed the game ends with status Won
##### Request Body
```json
{
	"row":7,
	"col":2
}
``` 

##### Response
```json
{
    "board": {
        "cells": [
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 0
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 1
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 1
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 2
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 2
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 3
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 3
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 4
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 5
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 6
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 6
                }
            ],
            [
                {
                    "col": 0,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 1,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 2,
                    "flagged": false,
                    "isMine": true,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 3,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 4,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 0,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 5,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 6,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                },
                {
                    "col": 7,
                    "flagged": false,
                    "isMine": false,
                    "neighborsMines": 1,
                    "revealed": false,
                    "row": 7
                }
            ]
        ],
        "cols": 8,
        "numberOfMines": 10,
        "rows": 8
    },
    "createdAt": "2019-10-22T12:27:29.636534",
    "durarion": "0:3:17",
    "finishedAt": "2019-10-22T12:30:47.300528",
    "gameId": "5daf1fe51cd7b3ce2af9796e",
    "level": "easy",
    "message": "The cell (7,2) is a mine. GAME OVER.",
    "status": "Lose"
}
``` 