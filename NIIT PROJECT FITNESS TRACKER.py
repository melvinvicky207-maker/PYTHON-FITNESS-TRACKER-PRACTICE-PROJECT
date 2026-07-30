
import pandas as pd
import os
import numpy as np

class Fitness_Tracker:

    ## STAGE 1

    def __init__(self):
        self.activities = {}
        self.filename = 'fitness_data.xlsx'

    def add_activities(self):

        ## 1
        print('---add new activity of your choice---')
        act_id = input('enter your unique activity id (eg:A001) : ').strip().upper()

        if act_id in self.activities:
            print('the activity id you have entered is already enrolled, please enter your unique id')
            return
        ## 2
        act_type = input('enter activity type (walking/cycling/yoga) : ').strip().capitalize()
        ## 3
        try:
            act_duration = float(input('enter the duration of you workout in minutes : '))
            act_calories = float(input('enter the calories you have burnt : '))
            if act_duration <= 0 or act_calories < 0 :
                return 
        except ValueError as chg_value:
            print(f'error {chg_value} as occured, please enter the value of the duration and calories in numbers')
            return
        ## 4
        act_date = input('enter the date (dd-mm-yyyy) : ').strip()
        ## 5
        self.activities[act_id] = {
            'type' : act_type,
            'duration' : act_duration,
            'calories' : act_calories,
            'date' : act_date
        }
        print(f'activity type {act_type} logged in successfully!! ')
        self.save_to_excel()
        ## 6
    def update_activity(self):
        print('---update existing activity---')
        act_id = input('enter the activity id if you want to update : ').strip().upper()

        if act_id not in self.activities:
            print('error: activity id does not found')
            return
        
        print(f'current data : {self.activities[act_id]}')
        print('enter new data if you wnat to update')
        
        ##
        new_type = input(f"new type [{self.activities[act_id]['type']}] : ").strip().capitalize()
        if new_type: self.activities[act_id]['type'] = new_type

        ##
        try:
            new_duration = input(f'new duration[{self.activities[act_id]['duration']}] : ').strip()
            if new_duration: self.activities[act_id]['duration'] = float(new_duration)

            new_calories = input(f'new calories [{self.activities[act_id]['calories']}] : ').strip()
            if new_calories: self.activities[act_id]['calories'] = float(new_calories)
        except ValueError as value_error:
            print(f'the error{value_error} has occured')
            return
        
        ##
        new_date = input(f'new date [{self.activities[act_id]['date']}] : ').strip()
        if new_date: self.activities[act_id]['date'] = new_date

        print(f'activity {act_id} updated successfully')
        self.save_to_excel()
        ## 7
    def delete_activity(self):
            print('---delete activity---')
            act_id = input('enter the activity id you want to delete : ').strip().upper()

            if act_id in self.activities:
                confirm = input(f'are you sure , you want to dele this act id {act_id}? (yes/no) : ').lower()
                if confirm == 'yes':
                    del self.activities[act_id]
                    print(f'act if {act_id} successfully deleted')
                    self.save_to_excel()
                else:
                    print('deletion cancelled')
            else:
                print('activity not found')
        ## 8
    def view_all(self):

            if not self.activities:
                print('there are not activities found yet')
                return
            
            print('activity log is : ')
            for aid,info in self.activities.items():
                print(f"id : {aid} | {info['date']} | {info['type']} | {info['duration']} min | {info['calories']} kcal")
        ## 9
    def save_to_excel(self):

            if self.activities:
                df = pd.DataFrame.from_dict(self.activities, orient = 'index')
                df.index.name = 'id'
                df.to_excel(self.filename)

    ## STAGE 2

    ## 1
    def load_data(self):
         
        if os.path.exists(self.filename):
            try:
                df = pd.read_excel(self.filename)
                self.activities = df.set_index('id').to_dict(orient='index')            
            except:
                 print('starting with a fresh log')

    ## 2
    def analyze_data(self):
         
        if not self.activities:
              print("no activities yet")
              return
         
        types = np.array([info['type'] for info in self.activities.values()])
        
        names, counts = np.unique(types, return_counts = True)
        favorite = names[np.argmax(counts)]

        check_intensity = lambda mins: 'high' if mins > 45 else 'low'

        print('---fitness analytics---')
        print(f'your most performed activity is : {favorite}')
        print(f'total workouts logged : {len(types)}')

    ## STAGE 3

    def get_ai_insights(self):
         
        if not self.activities:
              print('please add activities first to get ai insights')
              return
        
        total_cals = sum(info['calories'] for info in self.activities.values())

        if total_cals > 1000:
             status = 'active user'
             advice = 'excellent work! keep it up'

        elif total_cals > 500:
             status = 'moderate user'
             advice = 'you are doing well. try to add one or more sessions per week'

        else:
             status = 'needs imporvement'
             advice = 'small steps count! try a 15 min walk daily'

        print('---ai fitness insights---')
        print(f'status : {status}')
        print(f'advice : {advice}')

## STAGE 4

def main():
     tracker = Fitness_Tracker()
     tracker.load_data()

     while True:
          print('---fitness tracker menue---')
          print('1. add activity')
          print('2. view all activities')
          print('3. update activity')
          print('4. delete activity')
          print('5. view analytics')
          print('6. get ai insights')
          print('7. exit')

          choice = input('choose an option : ')
          
          if choice == '1':
            tracker.add_activities()
        
          elif choice == '2':
            tracker.view_all()

          elif choice == '3':
            tracker.update_activity()

          elif choice == '4':
            tracker.delete_activity()
          
          elif choice == '5':
            tracker.analyze_data()
          
          elif choice == '6':
            tracker.get_ai_insights()

          elif choice == '7':
            print('goodbye, stay hyderated')
            break

          else:
            print('invalid choice, please try again')

## STAGE 5

if __name__ =='__main__':
    main()
