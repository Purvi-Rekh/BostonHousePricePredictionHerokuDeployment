# BostonHousePricePredictionHerokuDeployment

### software and code Requirements

1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VScodeIDE](https://code.visualstudio.com/)
4. [GitCLi](https://git-scm.com/book/en/v2)

Create a new environment for project
---
conda create -p venv python==3.7 -y 
---

Activate environment

---
conda activate venv/
---

create requirements.txt, add all library names to it and run

---

pip install -r requirements.txt is not working directly so,
go inside venv/bin and then run pip install with path of requiremnets.txt
cd venv
cd bin
now in bin run
pip install -r ../../requirements.txt


---

git config --global user.name

git add filename - to add perticular file
git add . - to add all the files
git commit -m "message"


To run Flask app

cd venv
cd bin
now in bin run
python ../../app.py


SAMPLE JSON TO TEST FROM POSTMAN

IN POST MAN, SELECT POST METHOD AND GIVE http://127.0.0.1:5000/predict_api AS URL AND IN BODY select row and json and paste following json

{
    "data":{
        "CRIM":0.00632,
        "ZN":18.0,
        "INDUS":2.31,
        "CHAS":0.0,
        "NOX":0.538,
        "RM":6.575,
        "AGE":65.2,
        "DIS":4.0900,
        "RAD":1.0,
        "TAX":296,
        "PTRATIO":15.3,
        "B":396.90,
        "LTAT":4.98
    }
}