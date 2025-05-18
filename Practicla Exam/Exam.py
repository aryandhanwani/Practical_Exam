import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

try:
    class fitness:
        def log_activity(self,activity_type, duration,calories ):
            self.__activity_type__=activity_type
            self.__duration__=duration
            self.__calories__=calories
            self.__date__=datetime.now().strftime("%Y-%m-%d")
    
            self.__fitness_data__=pd.read_csv("fitness_activities.csv")
            new_entries=pd.DataFrame({
                "date":[self.__date__],
                "activity_type":[self.__activity_type__],
                "duration":[self.__duration__],
                "calories_burned":[self.__calories__]
            })
    
            df=pd.concat([self.__fitness_data__,new_entries],ignore_index=True)
    
            df.to_csv("fitness_activities.csv",index=False)
    
            print("New entry added successfully!\n")
            print("===============================\n")
    
        def calculate_metrics(self):
            self.__fitness_data__=pd.read_csv("fitness_activities.csv")
            
            print(f"Total Calories Burned: {self.__fitness_data__["calories_burned"].sum()}\n")
    
            print("===============================\n")
    
            print(f"Activity Frequency: {self.__fitness_data__.groupby("activity_type")[["duration","calories_burned"]].sum()}\n")
    
            print("===============================\n")
    
        def filter_activities(self):
            print("1. Filter Data Using Activity")
            print("2. Filter Data Using Date")
            
            choice4=int(input("Enter your Choice: "))
    
            if choice4==1:
                self.__fitness_data__=pd.read_csv("fitness_activities.csv")
    
                l=["Running","Yoga","Cycling", "Strength Training", "Swimming",
                "Walking"]
    
                activity_name=input("Enter the Activity name from (Running,Yoga,Cycling, Strength Training, Swimming, Walking): ")
    
                if activity_name in l:   
                    filtered = self.__fitness_data__[self.__fitness_data__["activity_type"] == activity_name]
                    
                    print(filtered[["duration", "calories_burned"]].agg(["mean", "min", "max", "sum"]))
    
                else:
                    print("Catergory is Different from Given Categories\n")       
                    print("==================================\n")
                    
                        
            elif choice4==2:
                self.__fitness_data__=pd.read_csv("fitness_activities.csv")
    
                date_range=input("Enter the Date to Filter(YYYY-MM-DD): ")
    
                filtered=self.__fitness_data__[self.__fitness_data__["date"]==date_range]
    
                print(filtered[["duration", "calories_burned"]].agg(["mean","min","max","sum"]))
          
            else:
                print("Invalid Choice\n")
                print("==================================\n")
    
    fit=fitness()
    
    while True:
        print("==================================\n")
        print("Personal Fitness Data Tracker\n")
        print("==================================\n")
    
        print("1. Add Fitness Entries")
        print("2. Data Loading and Cleaning")
        print("3. Analysis and Metrics")
        print("4. Filter Datas")
        print("5. Generate Graphs")
        print("6. Generate Data Report")
        print("7. Exit")
    
        choice1=int(input("Enter your choice: "))
        print()
    
        if choice1==1:
            l=["Running","Yoga","Cycling", "Strength Training", "Swimming", "Walking"]
            
            activity_type=input("Enter your Activity Type from (Running,Yoga, Cycling, Strength Training, Swimming, Walking): ")
    
            if activity_type in l:
                pass
            else:
                print("Catergory is Different from Given Categories\n")
    
            duration=int(input("Enter the Duration in Minutes: "))
            
            if duration <= 0:
                print("Duration Should be in Positive Numbers\n")
            else:
                pass
            
            calories=int(input("Enter the Amount of Caloreis Burned: "))
    
            if calories <= 0:
                print("Calories Must be in Positive Numbers\n")
            else:
                pass
            
            fit.log_activity(activity_type, duration, calories)
        
        elif choice1==2:
            dataset=pd.read_csv("fitness_activities.csv")   
    
            while True:
            
                print("1. Load the First 5 Rows of Data Set")
                print("2. Load the Last 5 Rows of Data Set")
                print("3. Check the Null Values")
                print("4. Fill the Null Values")
                print("5. Check the Duplicated Entries")
                print("6. Remove the Duplicated Entries")
                print("7. Go Back to main menu")    
    
                choice2=int(input("Enter your Choice: "))
                print()
    
                if choice2==1:
                    print(dataset.head())
                    print("===========================\n")
    
                elif choice2==2:
                    print(dataset.tail())
                    print("===========================\n")
                
                elif choice2==3:
                    print(dataset.isna().sum())
                
                elif choice2==4:
                    print("1. Fill Average Values")
                    print("2. Fill Sum of all Values")
                    print("3. Fill the Custom Values")
    
                    choice3=int(input("Enter your choice for filling the values"))
    
                    if choice3==1:
                        row=input("Enter the null value column name: ")
                        dataset.fillna(dataset[row].mean(),inplace=True)
                        print("Data Filled Successfully\n")
                        print("===========================\n")
    
    
                    elif choice3==2:
                        row=input("Enter the null value column name: ")
                        dataset.fillna(dataset[row].sum(),inplace=True)
                        print("Data Filled Successfully\n")
                        print("===========================\n")
    
                    elif choice3==3:
                        value=input("Enter the value to fill: ")
                        dataset.fillna(value,inplace=True)
                        print("Data Filled Successfully\n")
                        print("===========================\n")
    
                    else:
                        print("Invalid Choice\n")
                        print("=========================\n")
                
                elif choice2==5:
                    print(dataset.duplicated().sum())
                    print("===========================\n")
    
                elif choice2==6:
                    print(dataset.drop_duplicates())
                    print("Duplicated Data Removed Successfully\n")
                    print("===========================\n")
    
                elif choice2==7:
                    print("Getting Back to Main Menu\n")
                    print("===========================\n")
                    break
                
        elif choice1==3:
            fit.calculate_metrics()
        
        elif choice1==4:
            fit.filter_activities()
        
        elif choice1==5:
            
            dataset = pd.read_csv("fitness_activities.csv")
            
            plt.figure(figsize=(8, 10))
            plt.bar(dataset["activity_type"], dataset["duration"], color="skyblue")
            plt.xlabel("Activity Type")
            plt.ylabel("Duration (minutes)")
            plt.title("Activity vs Duration")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig("activity_duration_plot.png")
            plt.show()
            
            plt.figure(figsize=(8, 10))
            plt.plot(dataset["calories_burned"], dataset["duration"], color="skyblue", marker="o", markersize=8)
            plt.xlabel("Calories Burned")
            plt.ylabel("Duration (minutes)")
            plt.title("Calories Burned vs Duration")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig("calories_duration_plot.png")
            plt.legend(dataset["calories_burned"])
            plt.show()
            
            plt.figure(figsize=(8, 10))
            plt.pie(dataset.groupby("activity_type")["duration"].sum(), autopct="%1.0f%%")
            plt.xlabel("Calories Burned")
            plt.ylabel("Duration (minutes)")
            plt.title("Calories Burned vs Duration")
            plt.xticks(rotation=45)
            plt.legend(dataset["activity_type"])
            plt.tight_layout()
            plt.savefig("acitivty_duration_percentage.png")
            plt.show()
    
            plt.figure(figsize=(6, 4))
            heat=dataset[["duration", "calories_burned"]].corr()
            sb.heatmap(heat, annot=True)
            plt.title("Correlation Between Duration and Calories Burned")
            plt.tight_layout()
            plt.savefig("calories_duration_heatmap.png")
            plt.show()
    
        elif choice1==6:
            
            dataset = pd.read_csv("fitness_activities.csv")
            print(dataset.describe())
    
        elif choice1==7:
            print("Thanks for using Fitness Program")
            break
        
        else:
            print("Invalid Choice\n")

except Exception as e:
    print(f"An error occurred: {e}")