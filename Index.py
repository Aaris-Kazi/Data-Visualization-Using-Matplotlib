import test_database as td
import Data_Graph as dg
import data_visual as dv
def main():
    while(True):
        print('\t\t\tMENU')
        print('\n1.To show all defaulter\n2.To show all Graph Data\n3.To show Specific Graph Data\n4.To Exit')
        n = int(input('Enter your choice:\t'))
        if n == 1:
            td.td()

        elif n==2:
            dg.data()
        
        elif n==3:
            dv.data_vis()
        
        elif n==4:
            print('\t\tThanks For using Our Program')
            return False

if __name__ == "__main__":
    main()