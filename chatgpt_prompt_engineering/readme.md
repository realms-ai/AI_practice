# OpenAI

## Team
1. Andrew Mayne
2. Joe Palermo
3. Boris Power
4. Ted Sanders
5. Lilian Weng
6. Geoff Ladwig
7. Eddy Shyu
8. Tommy Nelson

## GUIDELINES: Principle of Prompting
1. Principle 1: Write clear and specific instructions
   - clear not = short
   - longer prompts provide better answers
   - Tactic 1: Use delimiters
     - Triple Quotes: """
     - Triple Backticks: ```
     - Triple Dashes: ---
     - Angle Brackets: < >
     - XML tags: <tag></tag>
   - Tactic 2: Asked for structured output like HTML, JSON
   - Tactic 3: Check whether conditions are satisfied. Check assumptions required to do the task.
   - Tactic 4: Few shot prompting
     - provides successful examples of completing the tasks. Then ask model to perform the task
2. principle 2: Give the model time to **think**
   - Tactic 1: Specify the steps required to complete a task
   - Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.
3. Model Limitations: Hallucinations
   - Follow the above tactics to bring the best from the AI

## ITERATION: Iterative Prompt Development
- Idea => Implementation (Code/Data) => Experimental result => Error Analysis

### Process
1. Try something
2. Analyze where the result does not give what you want
3. Clarify instructions, give more time to think
4. Refine the prompts with a batch of examples. 
5. Repeat


