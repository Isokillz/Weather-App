from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if all(dish <= 0 for dish in satisfaction): return 0
        satisfaction[:] = sorted(satisfaction)
        
        while sum(satisfaction) < 0:
            satisfaction.remove(min(satisfaction))
        
        return sum((i+1) * satisfaction[i] for i in range(len(satisfaction)))

if __name__ == "__main__":
    # Create a Solution object
    sol = Solution()
    
    # Test the maxSatisfaction function with a list of satisfaction ratings
    satisfaction_list = [-1,3,4]
    max_satisfaction = sol.maxSatisfaction(satisfaction_list)
    
    print(f"Maximum Satisfaction: {max_satisfaction}")
