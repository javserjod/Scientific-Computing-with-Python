# The Tower of Hanoi puzzle can be solved in 2**n - 1 moves, where n is the number of disks
# The allowed disk movements between the rods exhibit a repetitive pattern occurring every three moves. 
# For example, movements between rod A and rod C are allowed on the first, the fourth and the seventh move, where the remainder of the division between the move number and 3 is equal to 1.


# Although recursion can sometimes be less easy to understand, it gives you the power to create more concise code. 
# In this case, you don't even need to differentiate between even and odd numbers of disks.



NUMBER_OF_DISKS = 4
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)  
    
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)