"""
	Lena is preparing for important coding competition that is preceded by N sequential preliminary contests. She believes in "saving luck", 
	and wants to check her theory. Each contest is described by two integers, Li and Ti:

	Li is the amount of luck that can be gained by winning the contest. If Lena wins the contest, her luck balance will decrease by Li; if she 
	loses it, her luck balance will increase by Li.
	Ti denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
	If Lena loses no more than K important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? 
	This value may be negative.

	Input Format

	The first line contains two space-separated integers, N (the number of preliminary contests) and K (the maximum number of important contests 
	Lena can lose), respectively. 
	Each line i of the N subsequent lines contain two space-separated integers, Li (the contest's luck balance) and Ti (the contest's importance rating), 
	respectively.

	Constraints
	1 <= N <= 100
	0 <= K <= N 
	1 <= Li <= 10 ^ 4
	0 <= Ti <= 1

	Output Format

	Print a single integer denoting the maximum amount of luck Lena can have after all the contests.

	Sample Input

	6 3
	5 1
	2 1
	1 1
	8 1
	10 0
	5 0
	Sample Output

	29
	Explanation

	There are N = 6 contests. Of these contests, 4 are important (so she cannot lose any more than K = 3 of them). Lena maximizes her luck if she wins the  
	3rd important contest (where Li = 1) and loses all of the other five contests for a total luck balance of 29.

	Problem's link: https://www.hackerrank.com/contests/w21/challenges/luck-balance
"""

N, K = map(int, raw_input().strip().split())

luck = []

for i in range(N):
    l, r = map(int, raw_input().strip().split())
    luck.append([l, r])

max_amount_of_luck = 0

for lu in sorted(luck, key=lambda u: u[0], reverse=True):
	amount_of_luck = lu[0]
	rating = lu[1]

    if K != 0:
        if rating == 1:
            max_amount_of_luck += amount_of_luck
            K -= 1
    elif K == 0 and rating == 1:
        max_amount_of_luck -= amount_of_luck
    if lu[1] == 0:
        max_amount_of_luck += amount_of_luck
print max_amount_of_luck