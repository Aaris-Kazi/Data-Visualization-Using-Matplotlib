import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,4,9]
z = [4,9,6]
plt.plot(x,y)
plt.plot(x,z)
plt.title('Data Graph')
plt.xlabel('X')
plt.ylabel('Y AND Z')
plt.legend(['Y','Z'])
plt.show()

test_data = pd.read_csv(r'/home/aaris-kazi/Desktop/Python/mini project/Test.csv')
print(test_data)
r = test_data.Name
print(r)
i = test_data[test_data.Name == 'Afif plaavkar']
print(i)
j = test_data[test_data.Name == 'Sakib Arkate']
print(j)

plt.plot(i.Subject,i.Attendance)
plt.plot(j.Subject,j.Attendance)
plt.legend(['Afif', 'Sakib'])
plt.xlabel('Subject Code')
plt.ylabel('Attendace Percentage')
plt.grid(True)
plt.show()
