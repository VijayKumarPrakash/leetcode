class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        def sign(num):
            return "pos" if num > 0 else "neg"

        for rock in asteroids:
            stack.append(rock)

            # If sign difference exists, repeat until stability
            # It's okay if the left asteroid is moving left, and the right asteroid is moving right
            while len(stack) > 1 and sign(stack[-1]) == "neg" and sign(stack[-2]) == "pos":
                if abs(stack[-1]) > abs(stack[-2]):
                    stack[-2] = stack[-1]
                elif abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                stack.pop()                
        
        return stack

soln = Solution()
final_state = soln.asteroidCollision([5, 10, -5])
print(final_state) 
