import pandas as pd
import matplotlib.pyplot as plt


def data():
    test_data = pd.read_csv(r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\Test.csv')
    print(test_data)
    
    i = test_data[test_data.Name == 'Afif plaavkar']
    
    j = test_data[test_data.Name == 'Sakib Arkate']
    
    k = test_data[test_data.Name == 'Khan Osama']
    
    result = test_data[test_data.Subject =='AVG TH + PR']
    print(result)

    plt.plot(i.Subject,i.Attendance)
    plt.plot(j.Subject,j.Attendance)
    plt.plot(k.Subject,k.Attendance)
    plt.legend(['Afif', 'Sakib','Osama'])
    plt.xlabel('Subject Code')
    plt.ylabel('Attendace Percentage')
    plt.grid(True)
    plt.title('Attendance of every subject')
    plt.tight_layout(True)
    plt.subplots_adjust(left = 0.05, right = 1.0)
    plt.show()

    
def show():
    test_data = pd.read_csv(r'Test.csv')
    return test_data