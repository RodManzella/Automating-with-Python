import json

# for more complex data structures, you can use json data.
# data which are made of lists and dictionaries, and they are put in these .json files
# these data can be interpreted by Python using json module

with open("questions.json", 'r') as file:
      content = file.read()

data = json.loads(content)  # converts content string to list

# The json module gets the data from this file as simple text and converts then to a ds, in this case, a list.

print(data)

for question in data:
      print(question["question_text"])
      for index, alternative in enumerate(question["alternatives"]):
            print(index + 1, "-", alternative)
      user_choice = int(input("Enter your answer: "))
      question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
      if question["user_choice"] == question["correct_answer"]:
            score = score + 1
            result = "Correct answer"
      else:
            result = "Wrong answer"
      message = f"{result} {index + 1}Your answer is: {question['user_choice']}," \
                f" Correct answer: {question['correct_answer']}"
      print(message)

print(score, "/", len(data))




