import sys
import pandas
import re
import numpy as np
#Getting the inputs from the command line:

corpus=sys.argv[1]
text1=sys.argv[2]
text2=sys.argv[3]

# corpus="Corpus.txt"
# text1="Apple Computer is the first product of the company"
# text2="Apple introduced the new version of iPhone in 2008"

text1a=text1.split()
text2a=text2.split()
arr=[]
textc1=[]
#Calculating the unique words in the file:
h = set()
with open(corpus) as fp:
    for cnt, line in enumerate(fp):
        for term in line.split():
            h.add(term)
v=len(h)
print("For sentence 1: Before Smoothing")
for i in range(len(text1a)):
     word=text1a[i]
     wordcount=0
     with open(corpus) as fp:
         for cnt, line in enumerate(fp):
             wordcount = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))
             textc1.append(wordcount)

for i in range(len(text1a)):
    for j in range(len(text1a)):
        arr.append(text1a[i]+" "+text1a[j])

#Printing the count of all bigrams for 1St input:

A=np.array(arr).reshape(len(text1a),len(text1a))

bigrams1count=[]
for i in range(len(arr)):
         word=arr[i]
         wordcount=0
         with open(corpus) as fp:
             for cnt, line in enumerate(fp):
                 wordcount = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))
                 bigrams1count.append(wordcount)

print("The following values are for bigrams of the first sentence:")
B=np.array(bigrams1count).reshape(len(text1a),len(text1a))
print("\n")
print(B)
print("\n")
b1_prob=[]
#Calculating the probabilities of the first sentence:

for i in range(len(text1a)):
    for j in range(len(text1a)):
        b1_prob.append((B[i][j]/textc1[i]))
print("\n")
#The following is the table with probabilities of the first sentence:
print("The following values are the bigram probabilities of the first sentence:")
print("\n")
C=np.array(b1_prob).reshape(len(text1a),len(text1a))
print(C)

#Total probability before smoothing:
prob1=0
for i in range(len(text1a)):
    for j in range(len(text1a)):
        if((i+1)<len(text1a)):
            if(A[i][i+1]!=0):
                prob1=C[i][i+1]+prob1
                break

print("Total Probability before smoothing is "+str(prob1))

#After performing smoothing on the data:
print("For sentence 1: After Smoothing")
for i in range(len(bigrams1count)):
    bigrams1count[i]=bigrams1count[i]+1


D=np.array(bigrams1count).reshape(len(text1a),len(text1a))
#Printing the values after performing smoothing on the bigram counts
print("The following values are for bigrams of the first sentence after performing smoothing on them:")
print("\n")
print(D)
print("\n")





#Calculating the new probability after smoothing:





print("The probabilities after performing smoothing on the data on sentence 1:")
print("\n")
b1_prob=[]
for i in range(len(text1a)):
    for j in range(len(text1a)):
        b1_prob.append((D[i][j]/(textc1[i]+v)))
E=np.array(b1_prob).reshape(len(text1a),len(text1a))
print(E)
print("\n")


#Total probability of sentence 1 after smoothing:

prob1a=0
for i in range(len(text1a)):
    for j in range(len(text1a)):
        if((i+1)<len(text1a)):
            if(E[i][i+1]!=0):
                prob1a=E[i][i+1]+prob1a
                break
print("Total Probability after smoothing is "+str(prob1a))
print("\n")

textc2=[]
#Calulations on sentence two before smoothing:

print("For sentence 2: Before Smoothing")
for i in range(len(text2a)):
     word=text2a[i]
     wordcount=0
     with open(corpus) as fp:
         for cnt, line in enumerate(fp):
             wordcount = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))
             textc2.append(wordcount)



arr2=[]
for i in range(len(text2a)):
    for j in range(len(text2a)):
        arr2.append(text2a[i]+" "+text2a[j])

#Printing the count of all bigrams for 2nd input:
A=[]
A=np.array(arr2).reshape(len(text2a),len(text2a))

bigrams2count=[]
for i in range(len(arr)):
         word=arr[i]
         wordcount=0
         with open(corpus) as fp:
             for cnt, line in enumerate(fp):
                 wordcount = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))
                 bigrams2count.append(wordcount)

print("The following values are for bigrams of the second sentence before smoothing:")
B=[]
B=np.array(bigrams2count).reshape(len(text2a),len(text2a))
print("\n")
print(B)
print("\n")
b2_prob=[]
#Calculating the probabilities of the second sentence:

for i in range(len(text2a)):
    for j in range(len(text2a)):
        b2_prob.append((B[i][j]/textc2[i]))
print("\n")
#The following is the table with probabilities of the second sentence:
print("The following values are the bigram probabilities of the second sentence:")
print("\n")
C=[]
C=np.array(b2_prob).reshape(len(text2a),len(text2a))
print(C)
#Total probability before smoothing


prob2=0
for i in range(len(text2a)):
    for j in range(len(text2a)):
        if((i+1)<len(text2a)):
            if(C[i][i+1]!=0):
                prob2=C[i][i+1]+prob2
                break
print("Total Probability before smoothing is "+str(prob2))
print("\n")




#After performing smoothing on the data:
print("For sentence 2: After Smoothing")
for i in range(len(bigrams2count)):
    bigrams2count[i]=bigrams2count[i]+1


D=[]
D=np.array(bigrams2count).reshape(len(text2a),len(text2a))
#Printing the values after performing smoothing on the bigram counts
print("The following values are for bigrams of the second sentence after performing smoothing on them:")
print("\n")
print(D)
print("\n")





#Calculating the new probability after smoothing:
print("The probabilities after performing smoothing on the sentence 2:")
print("\n")
b2_prob=[]
for i in range(len(text2a)):
    for j in range(len(text2a)):
        b2_prob.append((D[i][j]/(textc2[i]+v)))
E=[]
E=np.array(b2_prob).reshape(len(text2a),len(text2a))
print(E)

# #Total probability of sentence 2:
prob2a=0
for i in range(len(text2a)):
    for j in range(len(text2a)):
        if((i+1)<len(text2a)):
            if(E[i][i+1]!=0):
                prob2a=E[i][i+1]+prob2a
                break
print("Total Probability after smoothing is "+str(prob2a))
print("\n")
