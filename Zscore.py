from math import sqrt
import numpy as np
import pandas as pd

def zscore(obs, pop):
    # Size of population.
    number = float(len(pop))
    # Average population value.
    avg = sum(pop) / number
    # Standard deviation of population.
    std = sqrt(sum(((c - avg) ** 2) for c in pop) / number)
    # Zscore Calculation.
    if std ==0:
        return 0;
    return (obs - avg) / std

my_data = pd.read_csv('NASA/nasa_data.csv', delimiter=',')
# print my_data.shape
my_data=my_data.values
# print my_data

ans = []
#print my_data[0].astype(int)    
for i in range(len(my_data)):
    answer=[]
    for j in range (12,29):
        answer.append(zscore(my_data[i,j],my_data[i,1:j-1]))
    ans.append(answer)
# print len(ans)
# print len(ans[0])
zs = np.array(ans)
# print zs.shape  
final=[]
# print zs[1:5]
'''
# 
# for i in range(len(my_data)):
#     final.append(zscore(zs[i,13],zs[i,0:13]))
'''   

for i in range(len(my_data)):
    final.append(sum(zs[i]))
# print len(final)
#print np.array( [ i for i in range(len(final)) if final[i] > 0 ] )
trending_index = np.argsort(np.array(final))[-5:][::-1] #top5
# print trending_index
#print np.array( [ final[i] for i in range(len(final)) if final[i] > 0 ] )
trending=[]
names=[]
# print my_data
for x in trending_index:
#     print final[x]
    trending.append(my_data[x][1:])
#     print my_data[x][1]
    names.append(str(my_data[x][0]))

# print trending
# print names
import matplotlib.pyplot as plt
# 
# plt.xlabel('July 1995')
# plt.ylabel('Requests')
# plt.title('NASA Trending Hosts')
# 
# plt.plot([i for i in range(28)],trending)#,label=names)
# #plt.gca().invert_xaxis()
# plt.legend()
# plt.show()
print trending
print names
# fig1 = plt.figure('NASA Trending Hosts')
# ax1 = fig1.add_subplot(111)
colors = ['b','r','c','g','k']
# for i in range(0,5):
#     ax1.bar([j for j in range(28)],trending[i],colors[i],label=names[i])
# ax1.set_xlabel("July 1995")
# ax1.set_ylabel("Requests")
# plt.title('NASA Trending Hosts')
# plt.legend()
# plt.show()

objects = [j for j in range(28)]
y_pos = np.arange(len(objects))

for i in range(0,5):
    plt.bar(y_pos, trending[i], align='center', alpha=0.5,color=colors[i],label=names[i])
plt.xticks(y_pos, objects)
plt.xlabel("1995,July 1st to 28th")
plt.ylabel('No of requests')
plt.title('NASA Trending Hosts')
plt.legend()
plt.show()


