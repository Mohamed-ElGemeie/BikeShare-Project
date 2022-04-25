import pandas as pd
import time
from datetime import datetime
import os
def get_filters():
          city_data = [  'chicago.csv','new_york_city.csv', 'washington.csv']           
          print('Hello! Let\'s explore some US bikeshare data!')
          months={'January':'JAN','Feburary':'FEB','March':'MAR','April':'API','June':'JUN','all':'ALL'}
          days={'Sunday':'SU','Monday':'MO','Tuesday':'TU','Wedensday':'WE','Thrusday':'TH','Friday':'FR','Saturday':'SA',"all":'ALL'}
          month_list=list(months.values())
          
          print("please enter a corresponding number fo the city you want to look up(chicago:1, new york city:2, washington:3)")   
          
          while True:         
                    x=input()           
                    try:                
                              x=int(x)
                    except:   
                              print("please enter a corresponding number of the city you want to look up(chicago:1, new york city:2, washington:3)")
                              continue
                    if(x<0 or x>3):
                              print("\nplease enter a number from 1-3 (chicago:1, new york city:2, washington:3)")
                              continue
                    else:
                              filter_city=x
                              print('-'*30)                              
                              break
          print("Do you want a month filter?\nselect one of the following options:")
          print("if no filter is required, please type \"all\"")
          y=0
          for i in months:
                    print("{}:{}{}".format(i,' '*(14-(3+len(i))),months[i]))
          while True:
                    x=input()          
                    if(x.isdigit()):  
                              print("Don't type a number.")
                              print("please type one of the months' short names above\nif no filter is required, please type \"all\"")
                              continue
                    x=x.upper()
                    if(x not in month_list):
                              print("please select one of the following month codes:")
                              if (y/2):
                                        for i in months:
                                                  print("{}:{}{}".format(i,' '*(14-(3+len(i))),months[i])) 
                              y+=1
                              continue
                    else:
                              filter_month=list(months.keys())[list(months.values()).index(x)]
                              print('-'*30)
                              break
                    
          y=0
          month_list=list(days.values())
          print("filter a certain day?\nselect one of the following options:")
          print("if no filter is required, please type \"all\"")
          for i in days:
                    print("{}:{}{}".format(i,' '*(14-(3+len(i))),days[i]))
          while True:
                    x=input()          
                    if(x.isdigit()):  
                              print("Don't type a number.")
                              print("please type one of the days' short names above\nif no filter is required, please type \"all\"")
                              continue
                    x=x.upper()
                    if(x not in month_list):
                              print("please select one of the following day codes:")
                              if (y/2):
                                        for i in days:
                                                  print("{}:{}{}".format(i,' '*(14-(3+len(i))),days[i])) 
                              y+=1
                              continue
                    else:
                              filter_days=list(days.keys())[list(days.values()).index(x)]
                              
                              print('-'*30)                             
                              break
          
          
          print('-------------Selected Filters-------------\n',
                "\nSelected File:",city_data[filter_city-1],
                "\nSelected Month:",filter_month,
                "\nSelected Day:",filter_days)
          return (filter_city,filter_month,filter_days)

def load_data(city, month, day):
          city_data = [ [1, 'chicago.csv'],
                        [2, 'new_york_city.csv'],
                        [3, 'washington.csv'] ]
          dic_days={'Sunday':0,'Monday':1,'Tuesday':2,'Wedensday':3,'Thrusday':4,'Friday':5,'Saturday':6}
          path=os.path.dirname(os.path.abspath(__file__))
          path=f'{path}\{city_data[city-1][1]}'
          print(path)
          df = pd.read_csv(path)
          df['Start Time'] = pd.to_datetime(df['Start Time'])
          
          df['month'] = df['Start Time'].dt.month
          df['day_of_week'] = df['Start Time'].dt.weekday
          
          
          if month != 'all':
                    months = ['January', 'February', 'March', 'April', 'May', 'June']          
                    month = months.index(month) + 1
                    df = df[df['month'] == month]        
          
          if day != 'all':
                    
                    df = df[df['day_of_week'] == dic_days[day]]
          df.name='{}'.format(city_data[city-1][1])
          return df

def time_stats(df):
          """Displays statistics on the most frequent times of travel."""       
          l_days=['Sunday','Monday','Tuesday','Wedensday','Thrusday','Friday','Saturday']
          months = ['January', 'February', 'March', 'April', 'May', 'June']          
          
          print('\nCalculating The Most Frequent Times of Travel...\n')
          start_time = time.time()
          
          popular_month=df['month'].mode()[0]
          
          print('The most common month is {}'.format(months[popular_month-1]))

          popular_day= df['day_of_week'].mode()[0]
          print('The most common day is {}'.format(l_days[popular_day]))
          

          df['hour'] = df['Start Time'].dt.hour
          popular_hour = df['hour'].mode()[0]
          
          print('The most common hour is {}'.format(popular_hour))

          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)

def station_stats(df):
          """Displays statistics on the most popular stations and trip."""

          print('\nCalculating The Most Popular Stations and Trip...\n')
          start_time = time.time()

          
          start_stations = df['Start Station'].value_counts()

          print("The most visited start station is: {}".format(start_stations.index[0]))


          end_stations = df['End Station'].value_counts()

          print("The most visited end station is: {}".format(end_stations.index[0]))
          
          
          both_stations = df.groupby(['End Station','Start Station']).size().sort_values(ascending=False)
          
          print("The common start and end station combination: {}".format(both_stations.index[0]))
         
          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)


def trip_duration_stats(df):
          """Displays statistics on the total and average trip duration."""

          print('\nCalculating Trip Duration...\n')
          start_time = time.time()

          travel_time=df['Trip Duration'].sum()
          formated_travel_time= time.strftime('%H:%M:%S', time.gmtime(travel_time))
          print('The Total travel time : {} (Hours,Minutes,Seconds)\n'.format(formated_travel_time))
          travel_ave=df['Trip Duration'].mean()
          formated_travel_ave=time.strftime('%H:%M:%S', time.gmtime(travel_ave))    
          print('The most average travel time : {} (Hours,Minutes,Seconds)'.format(formated_travel_ave))

          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)


def user_stats(df):
          """Displays statistics on bikeshare users."""

          print('\nCalculating User Stats...\n')
          start_time = time.time()


          
          users = df['User Type'].value_counts()
          print('User types and count:\n')
          print(users.to_string(),'\n')
          if df.name=='washington.csv':
                    print("There is no user 'Gender' or 'Age' Stats available in {}".format(df.name))
                    print("\nThis took %s seconds." % (time.time() - start_time))
                    time.sleep(1.7)                    
                    print('-'*40)                    
                    return()

          genders = df['Gender'].value_counts()
          print('Genders:')
          print(genders.to_string())                


          year_birth_er=df['Birth Year'].min()
          year_birth_re=df['Birth Year'].max()
          year_birth_ave=df['Birth Year'].mean()
          
          print('The oldest user was born in {}'.format(int(year_birth_er)))
          print('The youngest user was born in {}'.format(int(year_birth_re)))
          print('The average user was born in {} and has {} years'.format(int(year_birth_ave),str(datetime.now().year-year_birth_ave)))
          
          print("\nThis took %s seconds." % (time.time() - start_time))
          print('-'*40)
def raw_data(df):
          x=0
          while True:
                    x+=5   
                    y=x-5
                    print('-'*50)
                    print('These are 5 Lines of Raw Data:\n')
                    raw=df.iloc[ y:x , 0: ]
                    print(raw)
                    confirm=input("Would you like 5 more? type 'yes' , 'no'\n")
                    if confirm.lower() != 'yes':
                              break
def info_choice(df):
          
          choice=0
          choice_list=['Time Stats','Station Stats','Trip Duration Stats','User Stats','Raw Data']
          print('-'*50)
          print("Which one of these stats would you like to know about?\n")
          while True:         
                    print("1:Time Stats\n2:Station Stats\n3:Trip Duration Stats\n4:User Stats\n5:Raw Data\n6:None (Type 'none')\n")
                    print("Choose one and type it's corresponding number:\n")                                           
                    x=input()  
                    if(x.lower()=='none'):
                              break
                    try:                
                              x=int(x)
                    except:   
                              print("please enter a corresponding number of one of the stats, without letters or spaces")
                              continue
                    if(x<0 or x>5):
                              print('-'*50)                              
                              print("\nplease enter a number from 1-5:")
                              continue
                    else:
                              
                              confirm=input("---You choose {}, If Yes Type 'yes' to confirm or 'no' to choose again---\n".format(choice_list[x-1]))
                              if confirm.lower() != 'yes':
                                        continue    
                              time.sleep(1.3)
                              
                              run=eval(choice_list[x-1].lower().replace(' ','_')+"(df)")
                              
          
          
def main():
          while True:
                    city, month, day = get_filters()
                    time.sleep(0.5)
                    df = load_data(city, month, day)
                    time.sleep(1.5)
                    info_choice(df)         
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                              thanks='Thank you for using this project!'
                              for i in range(6):
                                        print(thanks.split()[i])
                                        time.sleep(0.4)                                        
                              break


if __name__ == "__main__":
          main()
