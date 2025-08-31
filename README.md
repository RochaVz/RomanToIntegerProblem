# RomanToIntegerProblem
This approach naturally handles the subtractive principle
Here's the logic:
Map Symbols to Values: Create a dictionary (or hash map) to store the integer value for each Roman symbol.
Initialize Result: Start with a total result of 0.
Iterate from Right to Left:
Get the value of the current Roman symbol.
Compare with Previous (to its right):
If the current symbol's value is less than the value of the symbol immediately to its right (the "previous" symbol in our right-to-left scan), it means we have a subtractive case. Subtract the current symbol's value from the result.
Otherwise (if the current symbol's value is greater than or equal to the value of the symbol to its right), it's an additive case. Add the current symbol's value to the result.
Keep Track of Previous Value: To make the comparison in step 3 possible, you need a variable to remember the value of the symbol you processed in the previous iteration (the one to the right of the current one). Initialize this "previous value" to 0 or the value of the last character.
Python Implementation Details
Dictionary for mapping: Python's dict is perfect for symbol: value.
Looping backwards: You can loop using range(len(s) - 1, -1, -1) or iterate over reversed(s) and manage an index. The range approach is often clearer for getting both the character and its position for comparison.
Variable to track previous value: prev_value = 0 (or similar) will be used.
Example Walkthrough: MCMXCIV
Let's use the algorithm for s = "MCMXCIV":
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0
prev_value = 0 (or last_value = 0)
Iterate i from len(s) - 1 down to 0
i = 4 (char V):
current_value = roman_map['V'] = 5
current_value (5) is >= prev_value (0)? Yes.
result = 0 + 5 = 5
prev_value = 5
i = 3 (char I):
current_value = roman_map['I'] = 1
current_value (1) is < prev_value (5)? Yes (this is IV).
result = 5 - 1 = 4
prev_value = 1
i = 2 (char C):
current_value = roman_map['C'] = 100
current_value (100) is >= prev_value (1)? Yes.
result = 4 + 100 = 104
prev_value = 100
i = 1 (char X):
current_value = roman_map['X'] = 10
current_value (10) is < prev_value (100)? Yes (this is XC).
result = 104 - 10 = 94
prev_value = 10
i = 0 (char M):
current_value = roman_map['M'] = 1000
current_value (1000) is >= prev_value (10)? Yes.
result = 94 + 1000 = 1094
prev_value = 1000
Wait, my example calculation for MCMXCIV was 1994. What went wrong in the trace?
Ah, the example MCMXCIV is 1000 + 900 + 90 + 4 = 1994. My trace results in 1094. This means I skipped a character or got the length wrong. Let's restart the trace with the full string for clarity.
String: M C M X C I V
Indices: 0 1 2 3 4 5 6
Length: 7
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0
prev_value = 0
i = 6 (char V):
current_value = 5
current_value (5) >= prev_value (0)? Yes.
result = 0 + 5 = 5
prev_value = 5
i = 5 (char I):
current_value = 1
current_value (1) < prev_value (5)? Yes (IV).
result = 5 - 1 = 4
prev_value = 1
i = 4 (char C):
current_value = 100
current_value (100) >= prev_value (1)? Yes.
result = 4 + 100 = 104
prev_value = 100
i = 3 (char X):
current_value = 10
current_value (10) < prev_value (100)? Yes (XC).
result = 104 - 10 = 94
prev_value = 10
i = 2 (char M):
current_value = 1000
current_value (1000) >= prev_value (10)? Yes.
result = 94 + 1000 = 1094
prev_value = 1000
i = 1 (char C):
current_value = 100
current_value (100) < prev_value (1000)? Yes (CM).
result = 1094 - 100 = 994
prev_value = 100
i = 0 (char M):
current_value = 1000
current_value (1000) >= prev_value (100)? Yes.
result = 994 + 1000 = 1994
prev_value = 1000
Loop ends. Final result = 1994. This matches!
