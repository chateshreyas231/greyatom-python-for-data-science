# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census=np.concatenate((data,new_record),axis=0)
print(census) 
print(data.shape,census.shape)

age=[row[0] for row in census]


max_age=max(age)
min_age=min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)

#step3

race_0=[row[2] for row in census if row[2]==0]
race_1=[row[2] for row in census if row[2]==1]
race_2=[row[2] for row in census if row[2]==2]
race_3=[row[2] for row in census if row[2]==3]
race_4=[row[2] for row in census if row[2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print(len_0,len_1,len_2,len_3,len_4)
a=[len_0,len_1,len_2,len_3,len_4]
minority_race=(a.index(min(a)))
print(minority_race)

#step4

senior_citizens=[row[0] for row in census if row[0]>60]
w=[row[6] for row in census if row[0]>60]
working_hours_sum=sum(w)
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)

avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


#step5

high=[row[1] for row in census if row[1]>10]
h=[row[7] for row in census if row[1]>10]
low=[row[1] for row in census if row[1]<=10]
l=[row[7] for row in census if row[1]<=10]
avg_pay_high=np.mean(h)
avg_pay_low=np.mean(l)
print(avg_pay_high,avg_pay_low)















