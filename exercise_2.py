## Complete this joint function
def joint(p_A, p_B):
    
    ## TODO: Change the value of joint_p
    ## so that it calculates the joint probability of 
    ## any variables p_A, p_B, WHEN THOSE PROBABILITIES
    ## ARE INDEPENDENT (this code wouldn't work 
    ## for probabilities that depend on each other).
    joint = p_A * p_B
    
    return joint

    
## TODO: Test out your code
## Define test probabilities and write print statements to test 
## the output of your function!
p_a_test = 0.2
p_b_test = 0.4
j = joint(p_a_test, p_b_test)

print('Your function returned that the joint probability is: '+str(j))

# Test values
test_A = 0.15
test_B = 0.42

# This line calls your function and stores the output
j = joint(test_A, test_B)
correct_j = solution.joint(test_A, test_B)

# Assertion, comparison test
try:
    assert(abs(j - correct_j) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the joint probability is: ' +str(j) 
           + ', which does not match the correct value.')
