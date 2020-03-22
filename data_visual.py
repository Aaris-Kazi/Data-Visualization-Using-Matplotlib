import pandas as pd
import matplotlib.pyplot as plt

def data_vis():
    print('\t\tWelcome to Attendace Stats')
    x = input('Enter the Name:\t')
    test_data = pd.read_csv(r'Test.csv')
    i = test_data[test_data.Name == x]
    print(i)


    plt.bar(i.Subject,i.Attendance)
    plt.legend([x])
    plt.xlabel('Subject Code')
    plt.ylabel('Attendace Percentage')
    plt.grid(True)
    plt.title('Attendance of every subject')
    plt.show()

    result = test_data[test_data.Subject =='AVG TH + PR']
    print(result)
