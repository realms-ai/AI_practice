get_completion = __import__("00_initializing")

# TACTIC 1: Use delimiters to clearly indicate distinct parts of the input
text1 = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""

prompt1 = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text1}```
"""

print("Prompt1: ", prompt1)

# response1 = get_completion(prompt1)
# print(response1)


# TACTIC 3: Ask the model to check whether conditions are satisfied
text_2 = f"""
Making a cup of tea is easy! First, you need to get some \ 
water boiling. While that's happening, \ 
grab a cup and put a tea bag in it. Once the water is \ 
hot enough, just pour it over the tea bag. \ 
Let it sit for a bit so the tea can steep. After a \ 
few minutes, take out the tea bag. If you \ 
like, you can add some sugar or milk to taste. \ 
And that's it! You've got yourself a delicious \ 
cup of tea to enjoy.
"""
prompt_2 = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{text_2}\"\"\"
"""

print("Text 2: ", prompt_2)

# response_2 = get_completion(prompt_2)
# print("Completion for Text 2:")
# print(response_2)

text_3 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the \ 
trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. \ 
Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a \ 
perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""
prompt_3 = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{text_3}\"\"\"
"""

print("Text 3: ", prompt_3)

# response_3 = get_completion(prompt_3)
# print("Completion for Text 3:")
# print(response_3)

# TACTIC 2: Asking for a structured output
text_4 = f"""
  Generate a list of three made-up book titles along /
  with their authors and genres.
  Provide them in JSON format with the following keys:
  book_id, title, author, genre.
"""

# response_4 = get_completion(text4)
# print("Completion for Text 4:")
# print(response_4)

# TACTIC 4: Few-shot prompting

prompt_5 = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \ 
valley flows from a modest spring; the \ 
grandest symphony originates from a single note; \ 
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""

# response_5 = get_completion(prompt_5)
# print(response_5)

# PRINCIPAL 2
# Tactic 1: Specify the steps required to complete a task

text_6 = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""
# example 1
prompt_6 = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text_6}```
"""
print("Prompt 6: ", prompt_6)
# response_6 = get_completion(prompt_6)
# print("Completion for prompt 6:")
# print(response_6)


# Ask for output in a specified format
prompt_7 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text_6}>
"""
print("Prompt 7: ", prompt_7)
# response_7 = get_completion(prompt_7)
# print("\nCompletion for prompt 7:")
# print(response_7)


# Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.

prompt_8 = f"""
Determine if the student's solution is correct or not.

Question:
I'm building a solar power installation and I need \
 help working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \ 
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations 
as a function of the number of square feet.

Student's Solution:
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""
print("Prompt 8: ", prompt_8)

# response_8 = get_completion(prompt_8)
# print(response_8)

# ChatGPT shows solution as correct. To fix this by instructing model to work out its own solution first
prompt_9 = f"""
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem including the final total. 
- Then compare your solution to the student's solution \ 
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
``` 
Student's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:
"""
print("Prompt 9: ", prompt_9)
# response_9 = get_completion(prompt_9)
# print(response_9)


# Your answer is in-correct, Correct answer to above problem is delimited by """ as below
# """
# Costs:
# 1. Land cost: $100x
# 2. Solar panel cost: $250x
# 3. Maintenance cost: $100,000 + $10x
# Total cost: $100x + $250x + ($100,000 + $10x) = $360x + $100,000
# """

# Compare student solution with above answer and evaluate it

# Model Limitations: Hallucinations

# prompt_10 = f"""
# Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
# """

# Provide a better prompt to get relevant information rather than model being hallucinating
prompt_10 = f"""
Your task is to search about the toothbrush of the company in a text delimited by <tag></tag>
To solve the problem do the following
- Search about the company and it's products
- Find the product asked in the text from the company
- Tell about the product in detail. If product not found, just simply answer "Product not found" and list few products of the company in same category to choose from
<tag>Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie</tag>
"""
print("Prompt 10: ", prompt_10)
# response_10 = get_completion(prompt_10)
# print(response_10)