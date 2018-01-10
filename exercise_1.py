# The complement function takes in the probability of an event, P(A).
def complement(p_A):
    
    ## TODO: Change the value of complement
    ## So that it calculates the complement of any variable p_A
    complement = 1 - p_A
    
    return complement

    
## TODO: Change this test value and test out your code!
p_test = 0.2

# Running your code with the p_test value
complement_test = complement(p_test)
print('Your function returned that the complement of '+str(p_test) +' is: '+str(complement_test))

# Test code - do not change
import solution

test_value = 0.4265

# This line calls your function and stores the output
comp = complement(test_value)
correct_comp = solution.complement(test_value)

# Assertion, comparison test
try:
    assert(abs(comp - correct_comp) < 0.0001)
    print('That\'s right!')
except:
    print ('Your code returned that the complement is: ' +str(comp) 
           + ', which does not match the correct value: ' +str(correct_comp))


# Test 2
comp2 = complement(solution.test_value)
correct_comp2 = solution.complement(solution.test_value)

# Assertion, comparison test
try:
    assert(abs(comp2 - correct_comp2) < 0.0001)
    print('That\'s right!')
except:
    print ('For test 2, your code returned that the complement is: ' +str(comp2) 
           + ', which does not match the correct value.')