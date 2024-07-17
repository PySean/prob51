Some definitions are in order. This problem wants us to find a "family" of primes of
size 8. It defines a "family" thusly: a set of prime numbers that each differ in exactly n
digits, and each of those shared digits is equal to another. An example of a nonprime
family would be 191, 292, 393, 494. This family is of size 4, they only differ 
in the first and last digits, and those digits match. A "template" can be used to 
achieve this result. I define a template as a number comprised wholly of 0 and 1. 

Here, we could use the template 101, and, starting with 191, can "progress" 191
to 292, 393, and 494 with repeated additions. Now, it is worth mentioning
that it isn't necessarily the case that we wish to progress each matching number
simultaneously. Which is why I generate all possible templates for a given set
of matching digits within a given number, which is precisely what this following
code does. The size of the family does thankfully restrict us. Based on the size,
we limit the digits we look at, because for example, for a family of size 8, 
we would only be able to generate a family of at most size 5 if we begun with 5.

Now, armed with the ability to generate the templates, and a simple sieve of 
eratosthenes, we can put these together to solve the problem. In a nutshell,
we take a prime, use the templates to progress, and the sieve to check if
each newly generated number from a template is prime. If it isn't and we
have hit our threshold for missteps given the digit we are progressing 
and the family size, we quit and move on to progressing the number with
another set of templates. Once we're done with our templates, if we haven't
formed a family of 8 prime numbers, we move on to the next prime number and
do it all again.
