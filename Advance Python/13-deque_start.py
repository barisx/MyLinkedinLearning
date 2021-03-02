# deque objects are like double-ended queues
# Tip: Memory efficient and operating in ends

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    # print "Item count:", str(len(d))
    # Item count: 26
    # TODO: deques can be iterated over
    # for elem in d:
    #     print elem.upper(),
    # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    # TODO: manipulate items from either end 
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)
    # deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
    
    # TODO: rotate the deque
    print(d)
    d.rotate(10)
    print(d)
    #! deque([1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2])
    #?  deque(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 2, 1, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    
if __name__ == "__main__":
    main() 