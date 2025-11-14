#Convert int to decima
import decimal
integer=20
a=decimal.Decimal(integer)
print(type(a))

#convert str into decimal
string="1223455"
print(decimal.Decimal(string))
#reverse the string
def stringRev(word):
    return word[::-1]
print(stringRev("sivaprassdadasd"))
#count volwels in word
def count_Vowels(words):
    vow="aeiou"
    count=0
    word=words
    for i in word:
        if i in vow:
            count+=1
    print(f"Vowels in word {word} : ",count)
count_Vowels("hello sivarprasds")
#count Consonants in word
def consonantWord(words):
    vow="aeiou"
    count=0
    for i in words:
        if i not in vow:
            count+=1
    print(f"Consonants in word {words} : ",count)
consonantWord("sivaprassdsdsd")


# count the number of occurence of a charater in a string

def count_char(strings,char):
    hashmap={}
    word=list(strings)
    for i,val in enumerate(word):
        hashmap[val]=hashmap.get(val,0)+1
    return hashmap[char]
print(count_char("sivaprakssasssssss","s"))

#fibonaci series
def fib(n):
    prev1=1
    prev2=0
    print(0)
    for _ in range(n):
        print(prev1)
        prev1,prev2=prev1+prev2,prev1
fib(5)

#find max number in List
def max_number(n):
    findmax=n[0]
    for i in n:
        if i>findmax:
            findmax=i
    return findmax
print(max_number([7,9,5,40,3,34,223]))     
# a=[2,4,64,343,34,223,0]
# print(max(a))
#find the min in list
def min_number(n):
    findmin=n[0]
    for i in n:
        if i<findmin:
            findmin=i
    return findmin
print(min_number([7,9,5,40,3,34,223])) 

#find the mid element in list
def find_mid(n):
    mid=round(len(n)/2)
    print("sss",mid)
    return n[mid]
print(find_mid([3,5,2,6,4,8]))
#convert list to str
p=["p","y","t","h","o","n"]
k="".join(p)
print(k)

#comparing 2 string anagram or not
str1 = "listen"
str2 = "Slient"

def check_Anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    hashmap1 = {}
    hashmap2 = {}

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        hashmap1[str1[i]] = hashmap1.get(str1[i], 0) + 1
        hashmap2[str2[i]] = hashmap2.get(str2[i], 0) + 1

    return hashmap1 == hashmap2

print(check_Anagram(str1, str2))




































