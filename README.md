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