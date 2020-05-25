\pagenumbering{gobble} \LARGE \begin{center} HackerRank 
\end{center}

\vspace{150px} \Huge \begin{center} Project Euler 
\end{center}

\vspace{180px} \normalsize

\newcommand{\itab}[1]{\hspace{0em}\rlap{#1}}
\newcommand{\tab}[1]{\hspace{.2\textwidth}\rlap{#1}}

\itab{Author} \tab \tab: Avinash Sorab

\itab{Date Created} \tab \tab: 24th Aug 2019

\itab{Language Used} \tab \tab: Python 3

\itab{Platform} \tab \tab: HackerRank

\vspace{180px} \normalsize


\normalsize



\vspace{180px} \normalsize

\tableofcontents

\vspace{400px} \normalsize


\section{ 1. Multiples of 3 and 5 }

The task is to find sum of all the multiples of 3 and 5 below N.

Multiples of 3 and Multiples of 5 form an AP.

Adding them you will get the sum of multiples, but 15 is repeated once. So, the final equation is

$$S_3 + S_5 - S_{15}$$

and

$$S_n = n*(firstterm + lastterm)/2$$


\section{ 2. Even Fibonacci numbers }

The task is to find the sum of all the Fibanocci number below N.

$$F_m = F_{m-1} - F_{m-2}$$

First step is to generate the Fibonacci number and store in an array since we know the Fibonacci number limit can be reached in fewer iterations.

Every 3rd element in the list is even.

Reason: First 2 numbers (0th and 1st) in the series is 0 and 1.

|    N       | Even/Odd                  |
|------------|---------------------------|
| 0th Number | 0 which is \textbf{Even}  |
| 1st Number | 1 which is Odd            |
| 2nd Number | Even + Odd = Odd          |
| 3rd Number | Odd + Odd = \textbf{Even} |
| 4th Number | Odd + Even = Odd          |
| 5th Number | Even + Odd = Odd          |
| 6th Number | Odd + Odd = \textbf{Even} |

and so on

So, you don't have to check if every number is even by dividing it by 2 and checking the reminder.
 
Instead, use a loop that iterates over every 3rd element starting from 0th element and add it to a sum variable.


\section{ 3. Largest prime factor }




\section{ 4. Largest palindrome product }




\section{ 5. Smallest multiple }

The task is to find the smallest multiple or (LCM) of all the numbers till N where N ranges till 40.

The root concept behind this is iterative calculation of LCM done easy.

$$LCM (a, b, c, d) = LCM (LCM (LCM (a, b), c), d)$$

and

$$LCM (a, b) = (a*b)/GCD (a, b)$$


\section{ 6. Sum square difference }

The task is to find the absolute difference between the sum of the squares of the first natural numbers N and the square of the sum.

If N is 3 then 

$$(1+2+3)^2 - (1^2 + 2^2 + 3^2) = 22$$

is the answer, absolute difference

The first sequence follows the order
$$(\Sigma n)^2$$
The second sequence follows the order
$$\Sigma n^2$$

Store the result of both and print the absolute difference, either that or
Solve them to get a final equation

$$Answer = n*(n+1)*(n-1)*(3n-2)/12$$

and print the same



\section{ 7. \boldmath$10001^{st}$ prime }

The task is to print the Nth prime number where N is less than or equal to 10000.

Since we need to do this process for 1000 more times, storing all the first ten thousand times and printing the nth prime would be more efficient time wise.

To store 10000 prime numbers. Find out 10000th prime number, by fact it is 104730.

Sieve of Eratosthenes method of finding out all the prime numbers below N is very much efficient than any other method. It basically takes a number N below which it must find out primes, declares an array of True values of length N. 

Then it initializes a counter, whose square should always be less than N.

Till then the counter keeps incrementing, and multiples of that counter is considered, this number is the index of the list whose value is made False since multiples are not primes.

Ex. If 3 is prime, then 6,9,12,15 are not. So those numbers are used as indices whose values are made False.

We get an array of Boolean values which are False at prime indices.

To find out Nth prime number we need to find Nth False value in the list and that’s the solution.


\section{ 8. Largest product in a series }
\section{ 9. Special Pythagorean triplet }
\section{ 10. Summation of primes }
\section{ 11. Largest product in a grid }
\section{ 12. Highly divisible triangular number }
\section{ 13. Large sum }
\section{ 14. Longest Collatz sequence }
\section{ 15. Lattice paths }

The task is to find the number of ways there can be to travel from top left to the bottom right of a given lattice structure, only being able to travel right or down.

Since there are different combinations of routes that we can draw from top left to the bottom right of the lattice. We can identify that it is a problem dealing with the combination.

If it was all possible routes among $M x N$ lattice, then the number of possible routes would be calculated as 
$$(m+1)*(n+1)$$

Since it was only bottom or right traversal route, the number of possible routes follow the pattern 

$$^{(m+n)}C_m$$

or

$$^{(m+n)}C_n$$


Combination Table

\begin{center}
\begin{tabular}{ c c c c c }
 M and N & 1 & 2 & 3 & 4 \\ 
 1 & 2 & 3 & 4 & 5 \\  
 2 & 3 & 6 & 10 & 15 \\ 
 3 & 4 & 10 & 20 & 35 \\
 4 & 5 & 15 & 35 & 70
\end{tabular}
\end{center}


Final answer needs to be $^{(m+n)}C_n \% (10^9 + 7)$

Got to make the combination calculations efficient


\section{ 16. Power digit sum }
\section{ 17. Number to words }
\section{ 18. Maximum path sum I }
\section{ 19. Counting Sundays }
\section{ 20. Factorial digit sum }
\section{ 21. Amicable numbers }
\section{ 22. Names scores }
\section{ 23. Non-abundant sums }
\section{ 24. Lexicographic permutations }

The task is to find the Nth lexicographic permutation of the string ‘abcdefghijkl’.

Example: if ‘abcde’ is the string and if we are required to calculate $14^{th}$ lexicographical permutation, 
i.e., ‘adcbe’

This problem requires the knowledge of \textbf{factorial number system}.

If we observe closely, 


\begin{tabular}{ c c c } 
abcde & 1! & That is 1st lexicographic permutation \\
abced & 2! & That is 2nd and abdce is 3rd \\
abedc & 3! & That is 6th and acbde is 7th \\
aedcb & 4! & That is 24th and bacde is 25th \\
edcba & 5! & That is 120th and last lexicographic permutation
\end{tabular}



The pattern here is that 


\begin{tabular}{ c c c } 
 abcde & 1! & The fifth letter changes after 0! = every 1 permutation \\  
 abced & 2! & The fourth letter changes after 1! = every 1 permutation \\ 
 abedc & 3! & The third letter changes after 2! = every 2 permutations \\
 aedcb & 4! & The second letter changes after 3! = every 6 permutations \\
 edcba & 5! & The first letter changes after 4! = every 24 permutations
\end{tabular}


If we can find the factoradic representation of the number N, that helps us to find the order of Nth permutation of the string.

Factorial Number System uses factorials instead of powers of 10 as in decimal or powers of binary as in binary number systems

First few numbers represented as factoradics

\begin{center}
\begin{tabular}{ c c c } 
Number & Factoradic & Expansion \\
0 & 0   & 	0 * 0! \\
1 & 10  & 	1 * 1! + 0 * 0! \\
2 & 100 & 	1 * 2! + 0 * 1! + 0 * 0! \\
3 & 110 &	1 * 2! + 1 * 1! + 0 * 0! \\
4 & 200 &	2 * 2! + 0 * 1! + 0 * 0!
\end{tabular}
\end{center}


And so on… there is always a unique factoradic for each integer

To calculate factoradic of an integer, keep dividing the integer from an incrementing counter until the quotient is 0, keep reverse track of the reminder and that will be your factoradic of that integer.



Example to find the factoradic of 349, 

-	349/1 -> 349 quotient with 0 remainder

-	349/2 -> 174 quotient with 1 remainder

-	174/3 -> 58 quotient with 0 remainder

-	58/4   -> 16 quotient with 2 remainder

-	14/5   -> 3 quotient with 4 remainder

-	2/6     -> 0 quotient with 2 remainder

Factoradic of 349(10) => 242010

Similarly factoradic of 14 is 2100

So to find 14th lexicographic permutation of ‘abcde’, since the string has 5 characters

Prepend ‘0’ to make factoradic a 5 character number 02100

Now loop through the factoradic number, the ith character serves as an index to fetch characters from the string and delete it from the string.

Ex: 0th character is a in abcde, delete a

2nd character is d in bcde, delete d

1st character is c in bce, delete c

0th character is b in be, delete b

0th character is e in e, delete e

Final string will be adcbe, the 14th lexicographic permutation in ‘abcde’.


Special care must be taken to calculate factoradic number, as the number gets bigger, say to calculate factoradic of 13! => 1211109876543210, the factoradic number actually should be treated as an array of 13 elements [‘12’, ‘11’, ‘10’, ‘9’, ‘8’, ‘7’, ‘6’, ‘5’, ‘4’, ‘3’, ‘2’, ’1’, ‘0’], so that reversal operations won’t hurt the actual elements and also calculating number of elements is easier because 0123456789101112 when reversed actually becomes 2111019876543210 and also contains 16 characters which are undesirable for our calculations, use list in place of strings to avoid this.


\section{ 25. N-digit Fibonacci number }

Task is to find the first Fibonacci number whose length is N.

This technique requires the knowledge of memoization, if we can memoize efficiently, this can be solved. 

We calculate all the Fibonacci number in an order, check its length, if the length of the current fibo number is greater than previous fibo number then store in a dictionary the length as key and the Fibonacci number’s occurrence number as the value. 

Ex: If 12th Fibonacci number is the first Fibonacci number to have 3 digits
Then fibo_dict[3] = 12.

Python can handle really long integer addition so carry out this process till you have
dict[5000] = 23922 or somewhere.

The next steps are to just access the value whose key is user input, can be written in a single line.




\section{ 26. Reciprocal cycles }
\section{ 27. Quadratic primes }
\section{ 28. Number spiral diagonals }
\section{ 29. Distinct powers }
\section{ 30. Digit Nth powers }
\section{ 31: Coin sums }
\section{ 32: Pandigital products }
\section{ 33: Digit canceling fractions }
\section{ 34. Digit factorials }
\section{ 35. Circular primes }
\section{ 36. Double-base palindromes }
\section{ 37. Truncatable primes }
\section{ 38. Pandigital multiples }
\section{ 39. Integer right triangles }
\section{ 40. Champernowne's constant }
\section{ 41. Pandigital prime }
\section{ 42. Coded triangle numbers }
\section{ 43. Sub-string divisibility }
\section{ 44. Pentagon numbers }
\section{ 45. Triangular, pentagonal, and hexagonal }
\section{ 46. Goldbach's other conjecture }
\section{ 47. Distinct primes factors }
\section{ 48. Self powers }
\section{ 49. Prime permutations }
\section{ 50. Consecutive prime sum }
\section{ 51. Prime digit replacements }
\section{ 52. Permuted multiples }
\section{ 53. Combinatoric selections }
\section{ 54. Poker hands }
\section{ 55. Lychrel numbers }
\section{ 56. Powerful digit sum }
\section{ 57. Square root convergents }
\section{ 58. Spiral primes }
\section{ 59. XOR decryption }
\section{ 60. Prime pair sets }
\section{ 61. Cyclical figurate numbers }
\section{ 62. Cubic permutations }
\section{ 63. Powerful digit counts }
\section{ 64. Odd period square roots }
\section{ 65. Convergents of e }
\section{ 66. Diophantine equation }
\section{ 67. Maximum path sum II }
\section{ 68. Magic N-gon ring }
\section{ 69. Totient maximum }
\section{ 70. Totient permutation }
\section{ 71. Ordered fractions }
\section{ 72. Counting fractions }
\section{ 73. Counting fractions in a range }
\section{ 74. Digit factorial chains }
\section{ 75. Singular integer right triangles }
\section{ 76. Counting summations }
\section{ 77. Prime summations }
\section{ 78. Coin partitions }
\section{ 79. Passcode derivation }
\section{ 80. Square root digital expansion }
\section{ 81. Path sum: two ways }
\section{ 82. Path sum: three ways }
\section{ 83. Path sum: four ways }
\section{ 84. Monopoly odds }
\section{ 85. Counting rectangles }
\section{ 86. Cuboid route }
\section{ 87. Prime power triples }
\section{ 88. Product-sum numbers }
\section{ 89. Roman numerals }
\section{ 90. Cube digit pairs }
\section{ 91. Right triangles with integer coordinates }
\section{ 92. Square digit chains }
\section{ 93. Arithmetic expressions }
\section{ 94. Almost equilateral triangles }
\section{ 95. Amicable chains }
\section{ 96. Su Doku }
\section{ 97. Large non-Mersenne prime }
\section{ 98. Anagramic squares }
\section{ 99. Largest exponential }
\section{ 100. Arranged probability }
\section{ 101. Optimum polynomial }
\section{ 102. Triangle containment }
\section{ 103. Special subset sums: optimum }
\section{ 104. Pandigital Fibonacci ends }
\section{ 105. Special subset sums: testing }
\section{ 106. Special subset sums: meta-testing }
\section{ 107. Minimal network }
\section{ 108. Diophantine reciprocals I }
\section{ 109. Darts }
\section{ 110. Diophantine reciprocals II }
\section{ 111. Primes with runs }
\section{ 112. Bouncy numbers }
\section{ 113. Non-bouncy numbers }
\section{ 114. Counting block combinations I }
\section{ 115. Counting block combinations II }
\section{ 116. Red, green or blue tiles }
\section{ 117. Red, green, and blue tiles }
\section{ 118. Pandigital prime sets }
\section{ 119. Digit power sum }
\section{ 120. Square remainders }
\section{ 121. Disc game prize fund }
\section{ 122. Efficient exponentiation }
\section{ 123. Prime square remainders }
\section{ 124. Ordered radicals }
\section{ 125. Palindromic sums }
\section{ 126. Cuboid layers }
\section{ 127. abc-hits }
\section{ 128. Hexagonal tile differences }
\section{ 129. Repunit divisibility }
\section{ 130. Composites with prime repunit property }
\section{ 131. Prime cube partnership }
\section{ 132. Large repunit factors }
\section{ 133. Repunit nonfactors }
\section{ 134. Prime pair connection }
\section{ 135. Same differences }
\section{ 136. Singleton difference }
\section{ 137. Fibonacci golden nuggets }
\section{ 138. Special isosceles triangles }
\section{ 139. Pythagorean tiles }
\section{ 140. Modified Fibonacci golden nuggets }
\section{ 141. Investigating progressive numbers, n, which are also square. }
\section{ 142. Perfect Square Collection }
\section{ 143. Investigating the Torricelli point of a triangle }
\section{ 144. Investigating multiple reflections of a laser beam. }
\section{ 145. How many reversible numbers are there below one-billion? }
\section{ 146. Investigating a Prime Pattern }
\section{ 147. Rectangles in cross-hatched grids }
\section{ 148. Exploring Pascal's triangle. }
\section{ 149. Searching for a maximum-sum subsequence. }
\section{ 150. Searching a triangular array for a sub-triangle having minimum-sum. }
\section{ 151. Paper sheets of standard sizes: an expected-value problem. }
\section{ 152. Writing 1/2 as a sum of inverse squares }
\section{ 153. Investigating Gaussian Integers }
\section{ 154. Exploring Pascal's pyramid. }
\section{ 155. Counting Capacitor Circuits. }
\section{ 156. Counting Digits }
\section{ 157. Solving the diophantine equation \boldmath$1/a +1/b = p/10^n$ }
\section{ 158. Exploring strings }
\section{ 159. Digital root sums of factorisations. }
\section{ 160. Factorial trailing digits }
\section{ 161. Triominoes }
\section{ 162. Hexadecimal numbers }
\section{ 163. Cross-hatched triangles }
\section{ 164. Numbers for which no three consecutive digits have a sum greater than a given value. }
\section{ 165. Intersections }
\section{ 166. Criss Cross }
\section{ 167. Investigating Ulam sequences }
\section{ 168. Number Rotations }
\section{ 169. Exploring the number of different ways a number can be expressed as a sum of powers of 2. }
\section{ 170. Find the largest 0 to 9 pandigital that can be formed by concatenating products. }
\section{ 171. Finding numbers for which the sum of the squares of the digits is a square }
\section{ 172. Investigating numbers with few repeated digits }
\section{ 173. Using up to one million tiles how many different "hollow" square laminae can be formed? }
\section{ 174. Counting the number of "hollow" square laminae that can form one, two, three, ... distinct arrangements. }
\section{ 175. Fractions involving the number of different ways a number can be expressed as a sum of powers of 2. }
\section{ 176. Rectangular triangles that share a cathetus. }
\section{ 177. Integer angled Quadrilaterals. }
\section{ 178. Step Numbers }
\section{ 179. Consecutive positive divisors }
\section{ 180. Rational zeros of a function of three variables. }
\section{ 181. Investigating in how many ways objects of two different colours can be  }
\section{ 182. RSA Encryption }
\section{ 183. Maximum product of parts }
\section{ 184. Triangles containing the origin. }
\section{ 185. Number Mind }
\section{ 186. Connectedness of a network. }
\section{ 187. Semiprimes }
\section{ 188. The hyperexponentiation of a number }
\section{ 189. Tri-colouring a triangular grid }
\section{ 190. Maximising a weighted product }
\section{ 191. Prize Strings }
\section{ 192. Best Approximations }
\section{ 193. Squarefree Numbers }
\section{ 194. Coloured Configurations }
\section{ 195. Inscribed circles of triangles with one angle of 60 degrees }
\section{ 196. Prime triplets }
\section{ 197. Investigating the behaviour of a recursively defined sequence }
\section{ 198. Ambiguous Numbers }
\section{ 199. Iterative Circle Packing }
\section{ 200. Find the 200th prime-proof sqube containing the contiguous sub-string "200" }
\section{ 201. Subsets with a unique sum }
\section{ 202. Laserbeam }
\section{ 203. Squarefree Binomial Coefficients }
\section{ 204. Generalised Hamming Numbers }
\section{ 205. Dice Game }
\section{ 206. Concealed Square }
\section{ 207. Integer partition equations }
\section{ 208. Robot Walks }
\section{ 209. Circular Logic }
\section{ 210. Obtuse Angled Triangles }
\section{ 211. Divisor Square Sum }
\section{ 212. Combined Volume of Cuboids }
\section{ 213. Flea Circus }
\section{ 214. Totient Chains }
\section{ 215. Crack-free Walls }
\section{ 216. Investigating the primality of numbers of the form \boldmath$2n^2 - 1$ }
\section{ 217. Balanced Numbers }
\section{ 218. Perfect right-angled triangles }
\section{ 219. Skew-cost coding }
\section{ 220. Heighway Dragon }
\section{ 221. Alexandrian Integers }
\section{ 222. Sphere Packing }
\section{ 223. Almost right-angled triangles I }
\section{ 224. Almost right-angled triangles II }
\section{ 225. Tribonacci non-divisors }
\section{ 226. A Scoop of Blancmange }
\section{ 227. The Chase }
\section{ 228. Minkowski Sums }
\section{ 229. Four Representations using Squares }
\section{ 230. Fibonacci Words }
\section{ 231. The prime factorisation of binomial coefficients }
\section{ 232. The Race }
\section{ 233. Lattice points on a circle }
\section{ 234. Semidivisible numbers }
\section{ 235. An Arithmetic Geometric sequence }
\section{ 236. Luxury Hampers }
\section{ 237. Tours on a 4 x n playing board }
\section{ 238. Infinite string tour }
\section{ 239. Twenty-two Foolish Primes }
\section{ 240. Top Dice }
\section{ 241. Perfection Quotients }
\section{ 242. Odd Triplets }
\section{ 243. Resilience }
\section{ 244. Sliders }
\section{ 245. Coresilience }
\section{ 246. Tangents to an ellipse }
\section{ 247. Squares under a hyperbola }
\section{ 248. Numbers for which Euler’s totient function equals 13! }
\section{ 249. Prime Subset Sums }
\section{ 250. 250250 }
\section{ 251. Cardano Triplets }
\section{ 252. Convex Holes }
\section{ 253. Tidying up }
\section{ 254. Sums of Digit Factorials }