Complete details to build a Rasa Weather-Telecasting Chatbot on Macos(Can be done in every os with little bit change in installations)

all files uploaded are the files which i wrote the code.
#weather.py is the python script to integrate our chatbot with api.
#actions.py is python script to communicate withstories.md
#nlu.md is file which has intents
#domain.yml is the file which has chatbots output
#stories.md is the file which has basic conversations for training
#endpoints.yml is to connect to the server
#config.yml is the configurations of the rasa.


FIRST OF ALL

.IN VISUAL STUDIO CODE  create a virtual environment(can watch youtube video-simple process) in a separate directory
.Create an another Directory to install Rasa in it
.Get into VScode terminal Command-"pip install rasa" with activating environment by "(virtual environment name)/bin/activate" 
.Another Command "pip install rasa-x --extra -i http://pypi.rasa.com/simple"
.Run "rasa init" in the terminal and proceed with Yes and Yes
.There u get many files Downloaded namely domain.yml,nlu.md,stories.md,actions.py and several other files



> Now look at my all codes and Analyze them.
> Now open 2nd terminal in vscode and run "rasa run actions"
> Now in the 1st terminal run "rasa train" and proceed with yes
> Now run "rasa shell"
                                               THERE YOU GO YOUR BOT IS COMPLETED........XD
