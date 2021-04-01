# Scripting-Assignment---Coding
## Short description
The idea of this script is to parse https://macaddress.io/ api output to stdout in format company_name;macaddres
Assumption was that company does not contain ";" (that have to be verified, so the action items is in to do). That makes as able to easily parse/split the out via cmd(using ; as delimiter). 
## How to run
### Script
1. Install dependecies pip install -r requiremnets.txt
2. put your api key in scrpit API_KEY = 'YOU_API_KEY'
3. python lookup.py MAC_ADDRESS
Please ensure replacing MAC_ADDRESS with format as in expample 
Example: 
python lookup.py 44:38:39:ff:ef:57
### Docker 
In to do short desc in to do as i do not have access to linux machine at the moment and setting up docker on Windows was way thou hell.
##TODO
### Secret managment 
So ideally in dockerized version i'd put api key on .env file to be replaced there
### Docker run
I'd will prepare some linux based docker image 
sth like this:
FROM python:3.8
WORKDIR /script
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "./lookup.py", $SEARCHED_MAC ]

also will store api key in .env
and the eg. run would look like 
docker run -e SEARCHED_MAC="44:38:39:ff:ef:57"

### input valdation/error handling
There would be a need to improve error handling and input validation, and put some easy to ready error messages.

### Delimiter 
I've put the ";" as delimiter between name and mac to easier spliting on singleline piped cmds but it has to be investigated what the best delimiter might be.

### Extending documentation
Ideally it would be great to add some more code examples and some one liners with usage of that script. but its nice to have.
