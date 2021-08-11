# Adventureland

![App page screenshot](assets/images/app_screenshot.png)
[View the app in Heroku here](https://adventureland-ana.herokuapp.com/)

## Table of Contents

1. [How to Play](#How-to_play)
2. [Features](#Features)
3. [UX/UI](#UX/UI)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)

## How to Play

Adventureland starts with the player been asked their name and then they get introduced to the story. They are the main character and do not remember what happened. The last memory is of them being in the street with some friends and then everything became blurry. The player wakes up in an empty room and straight away gets asked what actions s/he wants to take to get out of there. The player will go from room to room and will get to choose what items to pick, what items to use and what doors to go through in order to survive and get out of the place.

#### Solutions to Riddles
- Firebird riddle: the solution is "name" or "your name";
- Sorcerer riddle: the solution is "rainbow";

## Features
#### Existing Features
- The voice of the game guides the player throught the different rooms;
- The player plays against him/herself;
- If the player dies they can choose to restart the game or not;
- Riddles: the player needs to provide the correct answers to keep playing;
- Objects: the player needs to collect objects in order to get out of the house;

#### Future Features
- Introduce new levels to increment the level of difficulty;
- Add a map for the player to know where they are;
- Add a score tab;
- Be able to freely move back and forth inside the house;

[Back to Top ⇧](#Adventureland) 


## UX/UI

Before starting coding the game I did have a look to written adventure games like the classic [The Dreamhold](https://eblong.com/zarf/zweb/dreamhold/) and decided that I wwanted to inlcude in mine. The final decision for Adventureland was as per below:

[Adventureland Flowchart](assets/images/game-flowchart.png)

## Testing

The game is been manually tested by doing the following:
- Tested the game in Gitpod by providing incorrect data (i.e. answering other than 'yes' or 'no' when those were the only accepted answers) to check the game flow could be followed;
- The game is also tested in Heroku to check all the expected behaviours described below were also true;

#### Bugs

While coding the game there was a few issues with the if loop to get the expected answer from the player, an infinite loop was created. This was corrected by using an 'input' statement rather than a 'print' so the player could modify their answer rather than repeting the whole function again.



#### Remaining Bugs

#### Validator Testing

- Used [PEP8online.com](http://pep8online.com/) and no errors were returned


## Deployment

The project is been deployed to Heroku.

Steps for deployment:
- Install dependencies in the requirements.txt file
- Check the Procfile to ensure a correct deployment to Heroku
- Create a new app in Heroku: choose a unique name and region
- No sensitive data needed to be kept secret so nothing was added in the config Var tab
- Add necessary buildpacks: Python and NodeJS in this order
- For deployment method, GitHub was selected and confirmed we want to connect to GitHub
- Connect Heroku to the repository for Advertureland
- Set "Enable Automatic Deploys" to allow automatic deployments every time the code is pushed
- Click on Deploy

[Back to Top ⇧](#Adventureland) 


## Credits
- [Adventurelib](https://adventurelib.readthedocs.io/en/stable/index.html#) for the imported library
- [Stackoverflow](https://stackoverflow.com/) and [GeeksforGeeks](https://www.geeksforgeeks.org/) for debugging

[Back to Top ⇧](#Adventureland) 