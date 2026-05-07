# %%
from numpy.ma.core import diff
from soupsieve.util import lower

firstname = "Soran"
lastname = "Mahmoudi"

sent = firstname + " " + lastname +" continue The Sentence"
print(sent)
# %%
languages = ['Python', 'Java', 'C++']
print (f"Objective Language: {languages[0]}")
print (f"Objective Lang :{languages[1]}")
print (f'Objective Language: {languages[2]}')
# %%
jobs = ['programer' , 'driver' , 'seller' , 'doctor']
position = jobs.index('seller')
print (f"The index of 'seller' is {position}")
if 'programer' in jobs:
    print("yes 'programer' is in the list")
jobs.append('boz')
jobs.insert(3 , 'engineer')
print("\n--- Job List---")
for job in jobs:
    print(job)
print("\n--- Alphabetical Order ---")
print(sorted(jobs))
print("\n--- Original Order ---")
print(jobs)
print ("\n---- Reverse Alphabet---")
xjobs = sorted(jobs)
xjobs.reverse()
print(xjobs)
# %%
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print ("first three letters : " , alphabet[:3])

print ("three letter from middle" , alphabet[3:6])
print("from middle to the end" , alphabet[7:])
# %%
ad = [x * 10 for x in range(1,11)]
print(ad)
# %%
scores = (1,2,3,4,5,6,7,8,9,10)
print ("the lowest score is %d , and the highest score is %d "  % (scores[0], scores[-1]))
for score in scores:
    label= "point" if score == 1 else "points"
print("A judge can give a gymnast %d %s." %(score, label))
# %%
sentence = input(" Enter Ur Text : ")
words = sentence.replace("." , "").lower().split()


for i in range(len(words)):
    for j in range(len(words)):
        if i != j and words[i] in words[j]:
            print("the words %s appears in the word %s" %(words[i], words[j]))

# %%
target = "silent"
word_list = ["listen", "hello", "enlist", "world", "tinsel"]
target_sorted = sorted(target)
print (f" anagrams for {target} : ")
for word in word_list:
    if sorted(word) == target_sorted:
        print(word)


# %%
entry = input(" Enter Time : ")
t1, t2 = map(int, entry.split())
diff = abs(t2 - t1)
hours = diff // 3600
minutes = (diff % 3600) // 60
print(f"{hours} hours {minutes} minutes")
# %%
def is_valid_email(email):
    try:
        if "@" in email and "." not in email:
            return False
        if len(email) < 4:
            return False
        return True
    except:
        return False
userinput = input(" Enter Email : ")
print(is_valid_email(userinput))

# %%
def validatepass(password):
    has_low = False
    has_upper = False
    has_digit = False
    has_symbol = False
    symbols = "!@#$%^&*"
    for char in password:
        if char.islower() : has_low = True
        elif char.isupper() : has_upper = True
        elif char.isdigit() : has_digit = True
        elif char in symbols : has_symbol = True
        else :
            raise Exception(f"Character '{char}' is invalid")
    if has_low and has_upper and has_digit and has_digit and has_symbol:
        return "Password is Valid"
    else:
        raise Exception("Password is Invalid")
try:
    print(validatepass(" Like That : AB1$"))
    print(validatepass("12345"))
except Exception as e :
    print (e)
userinput = input(" Enter Password : ")
try :
    result = validatepass(userinput)
    print(result)
except Exception as e :
    print (e)

# %%
assadsdfsdgd

# %%
import random

name = input("Hello! What is your name?\n")

secret_number = random.randint(1, 20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

guesses_taken = 0
guess = 0

while guess != secret_number:
    print("Take a guess.")
    guess = int(input())
    guesses_taken += 1

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")

print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
# %%
dna = "ATGCTTCAGAAAGGTCTTACG"
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')
print(f"{a} {c} {g} {t}")
# %%
dna_t = "GATGGAACTTGACTACGTAAATT"
rna_u = dna_t.replace('T', 'U')
print(rna_u)
# %%

# %%
def is_caught(s):
    distance = abs(s.find('C') - s.find('m'))
    return distance <= 3

print(is_caught('C..m'))
print(is_caught('C.....m'))
# %%
def write_number(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    else:
        return tens[n // 10] + (("-" + ones[n % 10]) if n % 10 != 0 else "")

print(write_number(32))
# %%
import random

def nt_dictionary(n):
    d = {}
    while len(d) < n:
        key = random.randint(1, 1000)
        d[key] = key ** 2
    return d


print(nt_dictionary(20))
# %%
def split_the_bill(group):
    average = sum(group.values()) / len(group)
    return {name: average - amount for name, amount in group.items()}

group = {'Amy': 20, 'Bill': 15, 'Chris': 10}
print(split_the_bill(group))
# %%

# %%
def get_intersection(A, B):
    set_a = set(A)
    set_b = set(B)
    return list(set_a.intersection(set_b))

A = [1, 2, 3, 4, 5]
B = [0, 1, 3, 7]
print(get_intersection(A, B))
# %%
def max_product(nums):
    nums.sort()
    option1 = nums[-1] * nums[-2] * nums[-3]
    option2 = nums[0] * nums[1] * nums[-1]
    return max(option1, option2)

A = [1, 3, 4, 5]
B = [-2, -4, 5, 3]

print(max_product(A))
print(max_product(B))
# %%
def k_closest(points, k):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

pts = [[2, -1], [3, 2], [4, 1], [-1, -1], [-2, 2]]
print(k_closest(pts, 3))
# %%
def kth_smallest(matrix, k):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    flat_list.sort()
    return flat_list[k-1]

mat = [
    [1, 4, 7],
    [3, 5, 9],
    [6, 8, 11]
]
print(kth_smallest(mat, 4))
# %%
def max_subarray(nums):
    max_so_far = 0
    current_max = 0
    for x in nums:
        current_max = max(0, current_max + x)
        max_so_far = max(max_so_far, current_max)
    return max_so_far

arr = [-1, -3, 5, -4, 3, -6, 9, 2]
print(max_subarray(arr))
# %%
def get_max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

stock_prices = [10, 5, 20, 32, 25, 12]
print(get_max_profit(stock_prices))
# %%
def get_profit_dates(prices, dts):
    min_p = prices[0]
    buy_date = dts[0]
    max_p = 0
    best_buy = dts[0]
    best_sell = dts[0]
    for i in range(len(prices)):
        if prices[i] < min_p:
            min_p = prices[i]
            buy_date = dts[i]
        if prices[i] - min_p > max_p:
            max_p = prices[i] - min_p
            best_buy = buy_date
            best_sell = dts[i]
    return max_p, best_buy, best_sell

prices = [10, 5, 20, 32, 25, 12]
dts = ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06']
print(get_profit_dates(prices, dts))
# %%
