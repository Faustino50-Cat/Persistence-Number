"""
Proof: https://en.wikipedia.org/wiki/Persistence_of_a_number
Record: 277777788888899 -> 11 Total Steps
"""

def persistence(n,steps=0):
    # If remain 1 digit, it prints total steps
    if len(str(n)) == 1:
        print("Total Steps:",steps)
        return None
    

    steps += 1

    # A string is treated like an array, it can obtain number in this way
    numbers = [int(i) for i in str(n)]
    result = 1

    # For each digit, it take result and multiply for digit
    # For Example: 327 -> 3*2*7 --> 42 -> 4*2 --> 8 [stop]
    
    for j in numbers:
        result *= j
    print(result)
    
    # Recursive: persistence(327) --> persistence(42) --> persistence(8)
    persistence(result,steps)

def request():
    n = input("Number:\n")
    persistence(n)

request()
