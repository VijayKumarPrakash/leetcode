class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for rock in asteroids:
            # If sign difference exists, repeat until stability
            # It's okay if the left asteroid is moving left, and the right asteroid is moving right
            while stack and rock < 0 < stack[-1]:
                if abs(stack[-1]) > abs(rock):
                    break
                elif abs(stack[-1]) < abs(rock):
                    stack.pop()
                else:
                    # They are equal
                    stack.pop()
                    break
            else:
                stack.append(rock)
        
        return stack

soln = Solution()
# input_asteroids = [10, 2, -5]
# input_asteroids = [8,-8]
# input_asteroids = [8,-3,4,6,8,-4,-2,6,-12,12,6,-6]
input_asteroids = [-100, -12, -13, -5, -7, -10, 5, 17, -6, 3, -8, 2, -10, 4, -9]
final_state = soln.asteroidCollision(input_asteroids)
print(final_state) 
