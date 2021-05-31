A Basic example of using Fast API to host a AI endpoint

All you need is fast api and sklearn to work the example

It uses a random forest model to make a region prediction on three floats given to the model in list form

The endpoint is stood up by fast api and can be accessed with the swagger UI by typing docs next to the starting url 

The service is fully dockerized use from the root terminal folder the command

docker-compose build

And then 

docker-compose up 

To build it out fully as a container 