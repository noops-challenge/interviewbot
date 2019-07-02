![interviewbot](https://user-images.githubusercontent.com/212941/60543285-c55c5400-9cca-11e9-990c-eb0dbfaac9c5.png)

# 👋 Meet Interviewbot

Interviewbot is [Fizzbot's](https://github.com/noops-challenge/fizzbot) cousin. After job applicants pass the Fizzbot exam, they are invited to meet Interviewbot and solve some coding puzzles.

Like Fizzbot, Interviewbot has a number of questions for you. Interviewbot's questions are more difficult, so you might want to try your hand at Fizzbot first.

## 📖 How does it work?

To start your interview, access:

`https://api.noopschallenge.com/interviewbot/start`

The first question is easy—enter your GitHub username.

`POST` to `interviewbot/start` a JSON object with your username: `{ 'login': 'noops-challenge' }`

Interviewbot will respond with the `nextQuestion`.

Answering each question correctly will grant you access to the next question, in the `nextQuestion` field of the response.

Complete API documentation: [API.md](./API.md)

## 🎉 Interview Success!

If you can answer all of the questions, Interviewbot will grant you a certificate proving that you passed the interview.

The interview is timed, so be quick.

## ⛏️ Starter Kit: Ruby

Not sure where to begin? Try our [Ruby Starter Kit](./starters/interviewbot.rb) to get a headstart on your interview. It shows how to interact with the Interviewbot API.

## ✨ A few ideas
- **Try a new language**: Write a solver in a new-to-you language that accesses the API and answers the interview questions.
- **More like this**: One of the questions involves prime factorization. If you liked that question, you might be interested in [Project Euler](https://projecteuler.net), compendium of questions of varying difficulty. Have fun!
- **Suggest a question**: Do you have ideas for other questions Interviewbot should ask? Send us a pull request with your ideas. If we like them, we'll add them to interviewbot's list.


More about Interviewbot here: https://noopschallenge.com/challenges/interviewbot
