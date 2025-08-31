
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0 # Stores the value of the Roman numeral character to the right

        # Iterate through the string from right to left
        for i in range(len(s) - 1, -1, -1):
            current_char = s[i]
            current_value = roman_map[current_char]

            # If the current value is less than the previous (right-side) value,
            # it's a subtractive case (e.g., IV, IX, XL, etc.)
            if current_value < prev_value:
                total -= current_value
            # Otherwise, it's an additive case
            else:
                total += current_value

            # Update prev_value for the next iteration (to the left)
            prev_value = current_value
            
        return total

# --- Example Usage ---
if __name__ == "__main__":
    solver = Solution()

    print(f"'III' -> {solver.romanToInt('III')}")       # Expected: 3
    print(f"'LVIII' -> {solver.romanToInt('LVIII')}")   # Expected: 58
    print(f"'IX' -> {solver.romanToInt('IX')}")         # Expected: 9
    print(f"'MCMXCIV' -> {solver.romanToInt('MCMXCIV')}") # Expected: 1994
    print(f"'CDXLIV' -> {solver.romanToInt('CDXLIV')}") # Expected: 444
    print(f"'MDCCCLXXXIV' -> {solver.romanToInt('MDCCCLXXXIV')}") # Expected: 1884
    print(f"'I' -> {solver.romanToInt('I')}") # Expected: 1
    print(f"'XL' -> {solver.romanToInt('XL')}") # Expected: 40
