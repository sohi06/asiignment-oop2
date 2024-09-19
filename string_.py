sentence = "Learning Python is fun and rewarding."

start = sentence.find("Python")
end = sentence.find("rewarding")
substring = sentence[start:end].strip() 

print("Extracted substring:", substring)

# replacing "rewarding" with "exciting"
modified_sentence = sentence.replace("rewarding", "exciting")

print("Modified sentence:", modified_sentence)

# c. Insert the phrase " Keep practicing!" after "exciting" programmatically
# Find the position to insert the phrase
insert_position = modified_sentence.find("exciting") + len("exciting")
final_sentence = modified_sentence[:insert_position] + " Keep practicing!" + modified_sentence[insert_position:]

print("Sentence after insertion:", final_sentence)

# d. Capitalize the first letter of each word in the final output
capitalized_sentence = final_sentence.title()

print("Final capitalized sentence:", capitalized_sentence)