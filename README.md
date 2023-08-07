# Video-game-info-API
an api for gamers to learn more about thair favorite game

this is a restfull api with drf

all the things you need to know about a game is covered 

from how log does it take to finish it to users scores and comments

## How it Works
gamers can list games by category / rate / top 250 / or any order

Admins can do full crud on all games

#### Rate abd comment
Users can **comment** and **replay comments**

but for avoiding spam every user can post a comment up to 3 times on a single game

Users Can rate Games in range 0-10 and the Avg rate will be displayed on the game

#### BookMarking
users can bookmark thair favorite games 

and bookmark list is accessible 

#### Game detail
Game detail will show more options for every game

#### how long to beat
Users can add the time took to finish that game 

the timw showen is Avg of all submited times

for adding the time there is 3 modes (full game/ Story mode on normal/ story mode on hard)

#### Auth
JWT with 30 min lifetime (30 days refresh) has been used for login 

a custom user has been used 

user register is available

## How to run
first make sure you have docker installed

create a .env file

    touch .env

add your data base info to .env file and docker compose env

lastly run this command

    docker compose -f "docker-compose.yml" up -d --build 
