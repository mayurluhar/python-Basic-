import string
import collections


#print(string.ascii_lowercase)



def main():
   myd = collections.deque(string.ascii_lowercase)
   #print(len(myd))
   # for i in myd:
   #      print(i, end=",")
   # myd.popleft()
   myd.rotate(7)
   print(myd)

if __name__ == '__main__':
    main()