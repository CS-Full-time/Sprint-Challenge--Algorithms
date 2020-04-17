#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  linear complexity - denoted as O(n) because the operations increase with the increased size of n.
    every time n is change the value of a increases at a multiple of n and is constant.


b)  O(n*log n) - the amount of times this runs is directly dependant on the size of n. 
    every time n increases the entire block of code and j is always reset to 1, only sum continues to increase. 
    loops grow exponentially to meet n.


c)  also linear complexity - O(n) - only bunnies is able to increase in size.    
    bunnies is the only variable that will increase the number of operations

## Exercise II


    because it is eggs, starting on the lowest floor, therefore preventing any more 
    than 1 egg from breaking if it is true that there IS a floor from which an egg would not break if dropped 
    from. floor 'f' becomes the first floor where an egg breaks.

    If I didn't start on the first floor, like above naswer, then i would start from the middle floor and continue 
    to go down by the next middle floor (ex. 12 floor building - start at floor 6, go to floor 3, etc). once you find 
    the floor that an egg does not break, go up from there 1 floor at a time. the first floor that has an egg break 
    going up then becomes 'f'