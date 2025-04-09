# SocketMapper
## Prerequsites
### you need to install the following dependencies before the real installation
- Python
- Git
## Installation
1. To download the repository on your pc using git run the following command:
```
cd {DESIRED PATH}
git clone https://github.com/Amrloksha151/SocketMapper
```
2. To install required libraries run the following command:
```
pip install -r requirements.txt
```
**If you are using mac or linux use pip3 instead of pip**

## Usage
1. Run the program using this command
```
python main.py
```
2. It will open up and will show to options
### The Scanner
<ins>You will be asked for several info. about your target</ins>
1. The first entry askes about your target's ip or domain (***host***)
2. Then you'll be asked about the ***port range*** that you want to ensure its connectivity
3. You'll also be asked about the ***protocol*** you want to use
4. Lastly, you'll consider the way you want to ***save*** the results or to just print it out to the screen

_It will go over every port and check wheter it is open or not_
### The Grabber
<ins>You will be asked for several info. about your target</ins>
1. The first entry askes about your target's ip or domain (***host***)
2. Then you'll be asked about the ***port*** that you want to grab its banner
3. You'll also be asked about the ***protocol*** you want to use
4. Lastly, you'll consider if you want to ***save*** the results or to just print it out to the screen

_It will grab this target's port banner_