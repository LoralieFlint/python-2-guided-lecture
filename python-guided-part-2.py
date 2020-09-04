""" UPER """
# U ------ Understand
# P ------ Plan
# E ------ Execute
# R ------ Reflect

""" UNDERSTAND """
# Understand what the problem is

""" Questions """
# What are the inputs your code receives?
# What is the range of input?
# How big can the input be (how much data)?
# What are the outputs your code produces?
# What is the range of output?
# How big can the output be (how much data)?
# How performant must the code be?
# What is missing from the task description?
# Are there third-party stakeholders who we should consult?
# What assumptions are you making?
#    Does anyone else on the team need to validate these assumptions?

""" Actions """
# The most important thing you can do during this stage of the process is to ask questions!
#    Be as specific as you can when you are asking questions.
#    Be clear and concise with your questions by using unambiguous language and only including necessary details.
# Do not fear this part of the process—enjoy it!
#    Try to have a mindset where you see the problem as a curiosity to be explored, not something there to antagonize you.
#    Feeling antagonized and afraid won’t help you at work or in an interview. Remember, problem solving is the fun part so enjoy it!
# Identify the smaller components that make up the larger problem.
#    If you get stuck in understanding, break the larger problem into smaller sub-problems.
#    Then, apply this framework against each of the smaller sub-problems until you solve the larger problem.
# Try to digest the problem and comprehend it by rewriting the problem in your own words.
#    If you had to describe the problem to someone else, how would you do so?
# Diagram how the data flows through the problem.
#    Think about each stage of the journey for the data and what will happen to it as it travels through your program.
# Think like a villain.
#    What inputs would break your program?
# Where is the description of the problem incomplete?
#    If you aren’t able to get answers on something that’s unclear in the specifications, make an educated guess and document your assumptions and your decision.

""" PLAN """
# This is where you will ask what steps will I take to solve the problem? 
# You will take your description of the problem and transform it into a complete, actionable plan to solve that problem. 
# If you find shortcomings in your understanding of the problem while you’re planning, drop back to Step 1 until you resolve the ambiguity. 
# If you have not yet completed Step 1, you will end up planning to solve the wrong problem! When interviewing, 
# it’s very important that you do this step aloud!
 
""" Questions """
# Do you know the answer to a similar problem that has similar inputs and outputs?
#    What does this problem remind you of?
#    Can you bring that knowledge to bear here?
# Does my plan meet the performance requirements?
#    What’s the time complexity?
#    What’s the space complexity?
#    How big can my input data be?
# Can sorting the input data ahead of time lead to any improvements in time complexity?
#    Does recursion help?
#    Is the problem made up of identical subproblems?
#    Can you state the problem with itself in its own definition?
#Think like a villain. Does your plan cover the edge cases?

""" Actions """
# Solve the problem like a human.
#    If you’re sorting something, imagine your task as a pile of blocks in front of you that need to be sorted.
# Break down the steps you take into small enough pieces for a computer to understand.
# Approach the problem from many angles.
# Get a brute-force solution as quickly as possible, even if it’s not performant enough.
#    It can lead you toward better solutions.
# Come up with as many plans of attack as you can.
#    Choose the best one that satisfies performance needs.
# Try to solve a simpler version of the problem.
#    If the input is a 2D array, can you solve it for a 1D array?
#    If you need to count the number of ways to eat cookies 1, 2, or 3 at a time, first try to solve it for the number of ways you could eat two at a time or even one at a time.
#    The solution to the simpler problem can lead to insights on the more complex problem.
# List the nouns and verbs in the problem description.
#    Map each one to an algorithm, process, data structure, object, method, function, etc.
# Perfect can be the enemy of good.
#    Even if your initial workable solution isn’t performant enough, you can iterate later.
#    “Premature optimization is the root of all evil.”


""" EXECUTE """
#This is where you take your plan and convert it to actual, working code. 
# This step isn’t easy, but it’s much easier if you’ve done a good job with Steps 1 and 2 above. 
# If you find shortcomings in your plan while you’re implementing the solution, drop back to Step 2 until you resolve the ambiguity. 
# If you have not yet completed Step 2, you will spend far longer on this step than you have to.

""" Questions """
# Think like a villain. Does your implementation handle all inputs?
# What language is best to solve this problem?
#    Best technically?
#    Best for the company?
# What is the best way to split this code into functional modules?
# Are any of the modules reusable for later projects?
# Does this functionality already exist?
#    Are there built-in libraries I can leverage?
#    Are there third-party libraries I can leverage?
#        Are the licenses on those third-party libraries compatible with our needs?

""" Actions """
# Start a source code control repo (e.g. a git repo) if one doesn’t already exist.
# Convert your pseudocode and outlines into actual code.
# Don’t Repeat Yourself (DRY): Remove redundant code as you write it.
# Document code as you write it.
#    Header blocks that contain usage information.
#    Comments where necessary.
# Write code clearly enough that comments aren’t necessary.
#    If comments help clarify or summarize a piece of code to a reader, definitely add comments.
# If you write code that’s hackish or kludgy, fix it.
#    If you don’t have time to fix it, comment it with:
#        Why you couldn’t do it the Right Way (time constraints, etc.)
#        What do you need to do to make it Right.
# Follow the style guide for the company.
#    If no style guide is available, follow the style of the existing codebase.
#    If there is no existing style guide or codebase, choose the best one you can find.
# Write unit tests as required.
# Write end-to-end tests as required.

""" REFLECT """
# Is this implementation as good as I can make it? Would I be proud to show my code to another programmer?

""" Questions """
# Does your solution work in all cases?
#    Main case?
#    Edge cases?
# Is the solution performant enough?
# Is the code documented?
# In retrospect, what would you do differently? What will you do differently next time?
#    What went right?
#    What went wrong?

""" Actions """
# Document or implement any changes that you still need to make to the code.
# Document or remove any redundant code that you should refactor.
# Remove unused code.
# Document future shortcomings that you will need to address in the medium or long term.
# Identify and document algorithms that you should replace with algorithms with better time complexity.
# Identify and document or remove redundant computation.
# Document any embarrassing code that you need to fix.
#    Why you couldn’t do it the Right Way (time constraints, etc.)
#    What you need to do to make it Right.