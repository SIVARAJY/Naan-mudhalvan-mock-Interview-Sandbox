# Multi-language challenges and execution engine for Coding Sandbox

CODING_CHALLENGES = {
    "find_max": {
        "id": "find_max",
        "title": "Find the Maximum Element",
        "difficulty": "Easy",
        "description": "Write a function/method that returns the largest number in a non-empty array/list of integers.",
        "example": "Input: [3, 9, 2] -> Output: 9",
        "constraints": "1 <= array.length <= 10^5, -10^9 <= array[i] <= 10^9",
        "starters": {
            "python": "def find_max(numbers):\n    # Write your solution here\n    pass",
            "javascript": "function findMax(numbers) {\n    // Write your solution here\n    \n}",
            "java": "public class Solution {\n    public static int findMax(int[] numbers) {\n        // Write your solution here\n        return 0;\n    }\n}",
            "cpp": "int findMax(const std::vector<int>& numbers) {\n    // Write your solution here\n    return 0;\n}"
        },
        "hints": "Consider iterating through the elements while keeping track of the largest seen so far, or using built-in methods.",
        "test_cases": [
            {"input": [3, 9, 2], "expected": 9, "display": "[3, 9, 2]"},
            {"input": [-10, -5, -20, -1], "expected": -1, "display": "[-10, -5, -20, -1]"},
            {"input": [42], "expected": 42, "display": "[42]"},
            {"input": [100, 20, 500, 300, 50], "expected": 500, "display": "[100, 20, 500, 300, 50]"}
        ]
    },
    "reverse_string": {
        "id": "reverse_string",
        "title": "Reverse a String",
        "difficulty": "Easy",
        "description": "Write a function that reverses an input string and returns the inverted sequence.",
        "example": "Input: 'hello' -> Output: 'olleh'",
        "constraints": "0 <= s.length <= 10^4",
        "starters": {
            "python": "def reverse_string(s):\n    # Write your solution here\n    pass",
            "javascript": "function reverseString(s) {\n    // Write your solution here\n    \n}",
            "java": "public class Solution {\n    public static String reverseString(String s) {\n        // Write your solution here\n        return \"\";\n    }\n}",
            "cpp": "std::string reverseString(const std::string& s) {\n    // Write your solution here\n    return \"\";\n}"
        },
        "hints": "You can use two-pointer swapping, backward traversal, or built-in reverse utilities.",
        "test_cases": [
            {"input": "hello", "expected": "olleh", "display": "\"hello\""},
            {"input": "NaanMudhalvan", "expected": "navlahduMnaaN", "display": "\"NaanMudhalvan\""},
            {"input": "radar", "expected": "radar", "display": "\"radar\""},
            {"input": "12345", "expected": "54321", "display": "\"12345\""}
        ]
    },
    "two_sum": {
        "id": "two_sum",
        "title": "Two Sum Target",
        "difficulty": "Medium",
        "description": "Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target` (in ascending order).",
        "example": "Input: nums = [2, 7, 11, 15], target = 9 -> Output: [0, 1]",
        "constraints": "2 <= nums.length <= 10^4, Each input has exactly one solution.",
        "starters": {
            "python": "def two_sum(nums, target):\n    # Write your solution here (return list of 2 indices)\n    pass",
            "javascript": "function twoSum(nums, target) {\n    // Write your solution here (return array of 2 indices)\n    \n}",
            "java": "public class Solution {\n    public static int[] twoSum(int[] nums, int target) {\n        // Write your solution here\n        return new int[]{};\n    }\n}",
            "cpp": "std::vector<int> twoSum(const std::vector<int>& nums, int target) {\n    // Write your solution here\n    return {};\n}"
        },
        "hints": "A hash map / dictionary allows lookups of (target - current_num) in O(1) average time.",
        "test_cases": [
            {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": [0, 1], "display": "nums = [2, 7, 11, 15], target = 9"},
            {"input": {"nums": [3, 2, 4], "target": 6}, "expected": [1, 2], "display": "nums = [3, 2, 4], target = 6"},
            {"input": {"nums": [3, 3], "target": 6}, "expected": [0, 1], "display": "nums = [3, 3], target = 6"}
        ]
    }
}
