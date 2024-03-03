# Simple Battleships

Simple Battleships is a classic strategy game where players attempt to sink each other's fleet by guessing coordinates on a grid. This version of the game features a board generated using Python lists and incorporates a logic engine to allow the computer to fire back at the user.

(Developer: Florin Pinta alias xttrust)

![Start screen](docs/simple_battleships_start.png)

[Live game](https://simple-battleships-7f5685aaac43.herokuapp.com/)

## Table of Content

1. [Introduction](#introduction)
2. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
4. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Modeling](#data-modeling)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks--tools)
6. [Features](#features)
7. [Testing](#testing)
    1. [Tested Features](#tested-features)
    2. [Test Cases](#test-cases)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Introduction

Welcome to Simple Battleships! This classic strategy game challenges players to sink their opponent's fleet by guessing the coordinates of their ships on a grid. Whether you're a seasoned player or new to the game, Simple Battleships offers an engaging and entertaining experience for all.

## Project Goals 

### User Goals

The primary goal of Simple Battleships is to provide users with an enjoyable gaming experience. Key user goals include:

- Engaging gameplay that challenges the mind.
- Clear instructions and user interface.
- Ability to play against a computer opponent.

### Site Owner Goals

As the developer of Simple Battleships, the main objectives are:

- Create a polished and functional game.
- Provide a seamless user experience.

## User Experience

### Target Audience

Simple Battleships targets a diverse audience, including:

- Game enthusiasts of all ages.
- Casual gamers looking for a fun pastime.
- Individuals seeking a mental challenge.

### User Requirements and Expectations

Users of Simple Battleships expect:

- Intuitive game controls.
- Responsive feedback during gameplay.
- Enjoyable and immersive gaming experience.

### User Stories

1. As a player, I want to easily understand the rules of the game.
2. As a user, I want to be able to start a new game quickly.
3. As a gamer, I want the game to provide a challenging experience.
4. As a player, I want clear feedback on my progress and results.

## Technical Design

### Flowchart

```
st=>start: Start
e=>end: End
op1=>operation: Initialize Game
op2=>operation: User Inputs Guess
op3=>operation: Check Guess
cond=>condition: Guess Hits Ship?
op4=>operation: Update Board
cond2=>condition: All Ships Sunk?
op5=>operation: Display Victory Message

st->op1->op2->op3->cond
cond(yes)->op4->cond2
cond(no)->op2
cond2(yes)->op5->e
cond2(no)->op2
```

### Data Modeling

- User data is stored in a Google Spreadsheet

## Technologies Used

### Languages

- Python 3

### Frameworks & Tools

- Heroku
- Google Drive (for hosting the spreadsheet)
- Google Spreadsheet (for storing user data)
- pycodestyle (for code validation)
- GitHub
- Gitpod

## Features

### Welcome Message

- Displays a welcome message to the user upon login.

### Username/Password Input

- Prompts the user to input their credentials for login.

### Battleships Screen

- Features an ASCII art warship and logo for the main screen.

### Game Board

- Generates game boards for both the user and the computer.

### Game Inputs

- Allows the user to input their guesses and provides feedback on the result.

### Game Over

- Displays the end-of-game state to the user and allows them to retry or quit.

## Testing

### Tested Features

- Username Creation
- Game Initialization
- User Input Handling
- Computer Opponent Logic
- Game Over Conditions
- Replay Functionality


## Test Cases

### Username Creation

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| New User   | Enter a new username | Username is accepted and stored | Passed |
| Existing User | Enter an existing username | Username is recognized | Passed |

### Game Initialization

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| New Game  | Start a new game | Game board is generated | Passed |
| Game Board | Check game board layout | Game board matches expected layout | Passed |

### User Input Handling

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Valid Input | Enter valid coordinates | Coordinate is accepted and processed | Passed |
| Invalid Input | Enter invalid coordinates | Error message displayed | Passed |

### Computer Opponent Logic

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Random Guess | Computer makes a random guess | Guess is within game board boundaries | Passed |
| Smart Guess | Computer makes an educated guess | Guess is based on previous hits | Passed |

### Game Over Conditions

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Player Wins | Player destroys all computer ships | Victory message displayed | Passed |
| Computer Wins | Computer destroys all player ships | Defeat message displayed | Passed |

### Replay Functionality

| Test Case | Description | Expected Result | Actual Result |
|-----------|-------------|-----------------|---------------|
| Replay Game | Choose to replay the game | New game is initialized | Passed |
| Exit Game | Choose to exit the game | Game closes | Passed |

## Test Results

All test cases passed successfully, indicating that the game functions as intended and meets the expected requirements.

## Bugs Identified
While testing the game I encountered a bug on the deployed version on heroku where gspread was not found. I had to manualy add it to requirements.txt

## Conclusion

The testing process for **Simple Battleships** confirmed that all features operate correctly and meet user expectations. The game provides an engaging and enjoyable experience for players.


## Bugs

There are no bugs with the final version.

## Deployment

To deploy Simple Battleships on Heroku:

1. Clone the repository to your local machine or https://app.codeanywhere.com/
2. Set up your Heroku app and push the code to your Heroku remote.
3. Configure any necessary environment variables.
4. Deploy the app and ensure it's running correctly.

## Credits

### Code

- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- Dylan Israel [YouTube](https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=81s)

## Acknowledgments

Special thanks to:

- My mentor for their guidance and support.
- Code Institute's community for their valuable insights.