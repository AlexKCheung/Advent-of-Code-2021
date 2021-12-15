'''
--- Day 3: Binary Diagnostic ---
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, 
when decoded properly, can tell you many useful things about the conditions of the submarine. 
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers 
(called the gamma rate and the epsilon rate). 
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit 
in the corresponding position of all numbers in the diagnostic report. 
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
Considering only the first bit of each number, there are five 0 bits and seven 1 bits. 
Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, 
and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, 
the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. 
Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? 
(Be sure to represent your answer in decimal, not binary.)
'''

# do we scan file each line by len(a single line) times?



# gamma and epsilon are opposites
# so we can first find gamma, then flip all bits to get epsilon
# lastly multiply G and E to get power consumption answer

# open file
file = open('3-input.txt', 'r')
lines = file.readlines()

# len gave me one more than digits, probably endl counts as one
line_length = len(lines[0]) - 1 

output_array = [0] * line_length

# for each bit in number: scan lines to get count of 0s and 1s

for i in range(0, line_length):
    zero = 0
    one = 0
    for line in lines: 
        if line[i] == '0':
            zero += 1
        # else
        if line[i] == '1':
            one += 1

    if zero > one: 
        output_array[i] = 0
    # else 
    elif one > zero:
        output_array[i] = 1
    # else equal? not sure what to do for this test case 
    else: 
        print("zero and one equal")
        output_array[i] = 0
    
    # restart read to beginning
    file.seek(0)

# close file
file.close()


# output_array is gamma rate 

# reverse output_array / gamma rate to get epsilon rate
epsilon_array = [0] * line_length
for i in range(len(output_array)):
    if output_array[i] == 0:
        epsilon_array[i] = 1
    else: 
        epsilon_array[i] = 0

print(output_array)
print(epsilon_array)

# binary bits multiply by two for each position
gamma_rate = 0
epsilon_rate = 0
multiplier = 1

for i in range(len(output_array) - 1, -1, -1):
    gamma_rate += output_array[i] * multiplier
    multiplier *= 2

multiplier = 1
for i in range(len(epsilon_array) - 1, -1, -1):
    epsilon_rate += epsilon_array[i] * multiplier
    multiplier *= 2

print(gamma_rate, epsilon_rate)
output = gamma_rate * epsilon_rate
print(output)
# answer: 1540244
