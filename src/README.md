# MissionED Bot:

<br>
<p align="center">
<img src=https://cdn-images-1.medium.com/max/1200/0*oz2e-hQtsHOWzoB4. alt="abalone" width="500" height="300">    
</p>
<br>

---

## Steps to install RASA:

1. Install the Python development environment

```
C:\> pip3 install -U pip
```

2. Create a virtual environment

```
C:\> python3 -m venv ./venv
```

3. Activating the environment

```
C:\> .\venv\Scripts\activate
```

4. Install Rasa Open Source

```
$ pip install rasa
```

5. Installing rasa sdk for actions server:

```
pip install rasa-sdk
```
---
## Installing dependencies for spacy:

```
$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en
```

## To use the current pipeline:

```
pip install rasa[transformers]
```
---
## Steps to train and run the model:

1. For training the model go to the directory where all the files are saved and type:

```
rasa train
```

2. For testing the model in your local IDE, use the command:
``` 
rasa shell
```

3. For testing the bot after it is attached to the web interface use:
```
rasa run --enable-api --cors "*" --debug
``` 
After entering the above command, open index.html file in the web browser.

4. To activate the action server:
```
- Open a new terminal
- Specify the path where the files are saved
- Use the command: rasa run actions
```
5. The chatbot is live for testing.

