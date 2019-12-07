# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter = ",",skip_header = 1)
print("\nDate: \n\n",data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,new_record))
print("Census: ",census)
#Code starts here



# --------------
#Code starts here
age = np.array([])

for i in range(0,census.shape[0]):
    age = np.append(age,census[i][0])
print(age)

max_age = age.max()
print("Max Age: ",max_age)
min_age = age.min()
print("Min Age: ",min_age)
age_mean = age.mean()
print("Mean of Age: ",age_mean)
age_std = np.std(age)
print("Standard Deviation of Age: ",age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

#print('Race 0: ', race_0)
#print('Race 1: ', race_1)
#print('Race 2: ', race_2)
#print('Race 3: ', race_3)
#print('Race 4: ', race_4)

len_0 = len(race_0)
print('Citizen of race 0: ', len_0)
len_1 = len(race_1)
print('Citizen of race 1: ', len_1)
len_2 = len(race_2)
print('Citizen of race 2: ', len_2)
len_3 = len(race_3)
print('Citizen of race 3: ', len_3)
len_4 = len(race_4)
print('Citizen of race 4: ', len_4)

len_arr = np.array([len_0,len_1,len_2,len_3,len_4])
min_race = len_arr.min()
for i in range(0,len_arr.size):
    if min_race == len_arr[i]:
        minority_race = i
print(len_arr)
print(min_race)
print('Minimum no. of citizen is in Race ',minority_race)


# --------------
#Code starts here
#senior_citizens = np.empty((0,1))
#print(senior_citizens)


senior_citizens = census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum = 0
for i in range(0,len(senior_citizens)):
    working_hours_sum = working_hours_sum + senior_citizens[i][6]

print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print('Average: ', avg_working_hours)


# --------------
#Code starts here

avg_pay_high = 0
avg_pay_low = 0

high = census[census[:,1]>10]
low = census[census[:,1]<=10]
print(high)
print(low)     
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)

print(avg_pay_high > avg_pay_low)



