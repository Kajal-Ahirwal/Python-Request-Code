import requests
from pprint import pprint
url = "http://saral.navgurukul.org/api"

def course(link):
    res = requests.get(link)
    ret = res.json()
    return ret
url1 = url+"/"+"courses" 
full_courses = course(url1)
def home_data ():
    def space():
        user=(input("enter n for exit and any key for home:-"))
        return user
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%welcome to saral%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    course_list = []
    def courses_fun():
        index = 0
        while index < len(full_courses["availableCourses"]):
            courses_ex = full_courses["availableCourses"][index]
            course_name = courses_ex["name"]
            courses_id = courses_ex["id"]
            course_list.append(courses_id)
            print (str(index)+"----",course_name )
            index= index +1
            
            
    courses_fun()          

    user = int(input("enter your exercise?")) 
    user_id = course_list[user]

    
    print ("%%%%%%%%%%%%%choose your exercise%%%%%%%%%%%%%%%%%%%%%%%")
    url2 = url1+"/"+str(user_id)+"/"+'exercises'
    urlx = url1+"/"+str(user_id)+"/"+'exercise'

    exercise=course(url2)
    sub_exercises = []
    parentExerciseId2=[]
    slug_list=[]
    def exercise_func():
        index1 = 0
        while index1 < len(exercise["data"]):
            data_ex = exercise["data"][index1]
            all_exercise = data_ex["parentExerciseId"]
            child_ex = data_ex["childExercises"]
            exercise_id = data_ex["id"]
            sub_exercises.append(child_ex)
            parentExerciseId2.append(all_exercise)
            if all_exercise != []:
                exercise_name = data_ex["name"]
                exercise_slug = data_ex["slug"]

                slug_list.append(exercise_slug)    
                print (str(index1) + "*", exercise_name )     
            else:
                print("no") 
                
            index1= index1+1

    exercise_func()       
    user1 = int(input("enter your lesson?:-"))
    use_ex=slug_list[user1]
    all_exercise = slug_list[user1]

    url3 = urlx+"/"+"getBySlug?slug="+str(use_ex)
    urly = urlx+"/"+"getBySlug?slug="

    content = course(url3)
    content_name = content["content"]
    print (content_name)
    slug_list1 = []
    sub_name = []
    def child_func():
        if all_exercise != None:
            if sub_exercises[user1] != []:
                index2 = 0
                while index2 < len(sub_exercises[user1]):
                    child_sub_ex = sub_exercises[user1][index2]
                    sub_ex_name = child_sub_ex["name"]
                    sub_name.append(sub_ex_name)
                    sub_ex_slug = child_sub_ex["slug"]
                    slug_list1.append(sub_ex_slug)
                    print (str(index2)+ "%", sub_ex_name)
                    index2= index2+1
            print ("apka exercise finished ho gaya")
    child_func()
    user3 = int(input("enter your topics:-"))
    sub_content = slug_list1[user3]
    url4 = urly +str(sub_content)
    print_cont = course(url4)
    cont_name = print_cont["content"]
    print (cont_name) 
        

    if space() == "n":
        False

home_data()
user4=input("enter h for home")
if user4=="h" or "H":
    home_data()
