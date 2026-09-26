class Solution:
    def largestRectangleArea(self, histo):
        stack = []  # To store indices of histogram bars
        max_area = 0  # To keep track of the maximum rectangle area
        n = len(histo)  # Number of bars in the histogram
        
        for i in range(n + 1):  # Iterate through all bars and one extra iteration
            while stack and (i == n or histo[stack[-1]] >= histo[i]):  # Condition to pop from stack
                height = histo[stack.pop()]  # Height of the bar at the top of the stack
                # Calculate the width
                width = i if not stack else i - stack[-1] - 1
                # Update the maximum area
                max_area = max(max_area, width * height)
            
            stack.append(i)  # Push the current index into the stack
        
        return max_area
