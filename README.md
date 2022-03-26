# totalFoobar

brilleTranslation.py:
Pretty straightforward, nothing to really think about here.

pleasePssThCdedMssages.py:
This was a fucking mess. What the fuck. So the key here is the divisibility rule; the sum of the digits of any valid combination must be divisible by three. My initial solution (so elegant, so perfect) used itertools to calculate combinations that were divisible by three, but it failed on several hidden test cases that I couldn't figure out. After many, many hours and iterative tweaks and refactors I came to this solution, which is a jumbled fucking mess and I don't even know how I got here or why this works and my original solution doesn't.

hyILreadyDdTht.py:
Piece of cake. I make sure to convert values back and forth between decimal and the appropriate base, and tracked all outcomes in an array. If the same number pops up more than once, I just need to find the difference between the last occurrence of the value and the current length of the list.

bmbBby.py:
I initially tried going for a DFS with backtracking, but as input values approached the maximum of 10^5 things quickly got out of hand. I then considered implementing A* for solving this, but I realized that I could find the solution faster by working backwards; instead of adding up to the input, I subtracted back from the input. To make this faster, I tried iteratively dividing the larger value by the smaller one and using the sum of the quotients as the number of generations required, and then adjusted for the smaller number eventually reaching 1 by adding the final divisor minus 1. I started by using an implementation of the extended Euclidean algorithm I originally wrote for an RSA encryption implementation (as seen in the PyStuff repo), and then simplified and made further adjustments as necessary.
