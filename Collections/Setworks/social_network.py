

users=["rahul","rohit","kohli","rishab","pandya","siraj","sanju"]

rahul_followers=["rohit","kohli","rishab","rahul"]

#follow_suggestion [sanju,pandya,siraj]

rahul_followers_suggestion=set(users).difference(set(rahul_followers))

print(rahul_followers_suggestion)



rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

#mutual friends

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)