"""
    Greedy Regex -> finds the minimum match (?) here ? means 0 or 1 occurance of preceding group
    Non greedy Regex -> finds the maximum match (* | +) * means 0 or more occurance, + detects 1 or more occurances

    findall() returns all the matches as a list
"""
import re as regex


greedy1 = regex.compile(r'b.*n')
greedy2 = regex.compile(r'b.+n')
non_greedy = regex.compile(r'b.*?n')

sentence = "batman likes to fly and batman is a superhero"

print(greedy1.findall(sentence))
print(greedy2.findall(sentence))
print(non_greedy.findall(sentence))
