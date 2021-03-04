# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

#  10001000
#  1000100010001000

#  5 = (101)_2  
#  5 + 101 = 106 but 5 +(101)_2 = (10)_10
#  5.encode("_2") + (101)_2 or (101)_2.decode("_10") + 5

def main():
    # define some  starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])  # ASCII
    # print(b)
    # [65, 66, 67, 68]  # (Python 2), Decimal Numbers
    # b'ABCD'           # (Python 3), byte type string
    
    s = "This is a string"
    # print(s)
    
    # TODO: Try combining them.
    # print(s+b)
    # This is a string[65, 66, 67, 68]  # (Python 2)
    #! Error in Python3 
    #? TypeError: can only concatenate str (not "bytes") to str
    
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    # s2 = b.decode('utf-8')
    # print (s+s2)
    # This is a string[65, 66, 67, 68]  # Python2
    # This is a stringABCD              # Python3
    
    # b2 = s.encode('utf-8')
    # print(b+b2)
    # [65, 66, 67, 68]This is a string  # Python2
    # b'ABCDThis is a string'           # Python3
    
    # TODO: encode the string as UTF-32
    # b3 = s.encode('utf-32')
    # print(b3)
    
    # Python2
    # ��This is a string  
    
    # Python3
    # b'\xff\xfe\x00\x00T\x00\x00\x00h\x00\x00\x00i\x00\x00\x00s\x00\x00\x00 
    # \x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00a\x00\x00\x00 
    # \x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00n
    # \x00\x00\x00g\x00\x00\x00'  
    
    s = 'terfinx' 
    s = ''.join(sorted(list(s)[3:7])+list(s)[0:3]) 
    print(s)
if  __name__ == "__main__":
    main()