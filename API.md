
## interviewbot API


### GET /interviewbot/start to get started

`GET https://api.noopschallenge.com/interviewbot/start`

`HTTP 200`

```
{
  "message": "Welcome to your interview. Please POST your GitHub login to this URL to get started. See the exampleResponse for more information.",
  "exampleResponse": { "login": "noops-challenger" }
}
```


### POST your GitHub login to start the interview

`POST https://api.noopschallenge.com/interviewbot/start`


```
{
 "login": "noops-challenger"
}
```

`HTTP 200`

```
{
  "message": "Hello noops-challenger, get ready for your interview. Your first question is at /interviewbot/questions/izZhyS2sCY7kZtZJf8yjizYuMo7zLE0m4Ucom4NeJYc",
  "nextQuestion": "/interviewbot/questions/izZhyS2sCY7kZtZJf8yjizYuMo7zLE0m4Ucom4NeJYc"
}
```


### GET first question

`GET https://api.noopschallenge.com/interviewbot/questions/izZhyS2sCY7kZtZJf8yjizYuMo7zLE0m4Ucom4NeJYc`

`HTTP 200`

```
{
  "questionPath": "/interviewbot/questions/izZhyS2sCY7kZtZJf8yjizYuMo7zLE0m4Ucom4NeJYc",
  "question": 12111900247,
  "message": "Find the prime factors of the number 12111900247. The prime factors of a number are the prime numbers that result in the number when multiplied together. The prime factors of 12 would be [2,2,3] because 2 * 2 * 3 = 12.",
  "exampleResponse": {
    "answer": [ 2, 3, 5, 7 ]
  }
}
```

