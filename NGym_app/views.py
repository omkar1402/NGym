from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import LoginForm,RegisterForm,Calories
from django.contrib.auth.models import User
from requests.compat import quote_plus
import requests
from bs4 import BeautifulSoup
from .forms import EmployeeForm
from .models import Employee,Calories1

# import mysql.connector as mcdb
# conn = mcdb.connect(host="localhost", user="root", passwd="root", database='ngym')
# print('Successfully connected to database')
# cur = conn.cursor()
# from .models import form

# Create your views here.
def employee_list(request):
    context={
        'employee_list':Employee.objects.all(),
    }
    return render(request,'employee_list.html',context=context)

def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            context={
                'form' : EmployeeForm(),
            }
        else:
            employee=Employee.objects.get(pk=id)
            context={
                'form' : EmployeeForm(instance=employee),
            }
        return render(request, 'register.html',context)
    else:
        if id==0:
            context={
                'form':EmployeeForm(request.POST),
            }
        else:
            employee=Employee.objects.get(pk=id)
            context = {
                'form': EmployeeForm(request.POST,instance=employee),
            }
        if context['form'].is_valid():
            context['form'].save()
        return redirect('/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')


# Differs from the Harris-Benedict formula, this formula is simpler and does not calculate body height. WHO Formula is categorized based on one’s age. For example, to find out the needs of energy for women between 18-29 years old, we use a formula of 14.7 x (body weight in kilogram) + 496. Whereas for men age 18-29 years old, formula used is 15.3 x (body weight in kilogram) + 679. The result is then multiplied by physical activity factor.
def home(request):
    if request.method == "GET":
        context = {
            'form': Calories(),
        }
    else:
        context = {
            'form': Calories(request.POST),
        }
        if context['form'].is_valid():
            context['form'].save()

            # for men age 18-29 years old, formula used is 15.3 x (body weight in kilogram) + 679.
            # The result is then multiplied by physical activity factor
            cal = (context['form'].cleaned_data['Weight'] * 15.3)+679
            print(cal)
            name=context['form'].cleaned_data['Name']
            context['cal']=cal
            context['name']= name
        redirect('/')
    print(context)
    return render(request,'home.html',context=context)

def bulky(request):
    return render(request,'Bulk.html')

def lean(request):
    return render(request,'Cut.html')

def maintain(request):
    return render(request,'Maintain.html')  

def gain(request):
    return render(request,'Gain.html')  

def loss(request):
    return render(request,'Loss.html')  

def diet_maintain(request):
    return render(request,'Diet_Maintain.html')

def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form,
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("Error")
    return render(request,'login.html',context=context)

def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password_first')
        first_name=form.cleaned_data.get('First_Name')
        last_name = form.cleaned_data.get('Last_Name')
        # new_user=User.objects.create_user(username,email,password,first_name,last_name)
        # new_user = User.objects.create_user(first_name,last_name)
        new_user = User.objects.create_user(
            form.cleaned_data['username'],
            first_name=form.cleaned_data['First_Name'],
            last_name=form.cleaned_data['Last_Name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password_first']
        )

    return render(request,"register.html",context=context)

def logout_page(request):
    logout(request)
    return redirect('/')


def chest(request):
    return render(request,'workouts/chest.html')

def back(request):
    return render(request,'workouts/back.html')

def shoulder(request):
    return render(request,'workouts/shoulder.html')

def bicep(request):
    return render(request,'workouts/bicep.html')

def tricep(request):
    return render(request,'workouts/tricep.html')

def legs(request):
    return render(request,'workouts/legs.html')

def chest_back(request):
    return render(request,'workouts/chest_back.html')

def shoulder_legs(request):
    return render(request,'workouts/shoulder_legs.html')

def bicep_tricep(request):
    return render(request,'workouts/bicep_tricep.html')

def push(request):
    return render(request,'workouts/push.html')

def pull(request):
    return render(request,'workouts/pull.html')

def fruits(request):
    name = ['Apple', 'Avocado', 'Banana','Grapes','Kiwifruit','Lime','Orange','Pineapple','Strawberries','Plums','Watermelon']
    amount = ['1 large','1/5 medium','1 medium','3/4 cup','2 medium','1 medium','1 medium','2 slices','8 medium','2 medium','2 cups diced pieces']
    calories = [130,50,110,90,90,20,80,50,50,70,80]

    context={
        'list':name,
        'list1':amount,
        'list2':calories,
    }

    return render(request,'diet/fruits.html',context=context)
#
# protein=['Rawas (Indian Salmon)','Katla (Indian Carp or Bengal Carp)','Rohu (Roho or Carpo Fish)','Bangda (Indian Mackerel)','Surmai (Seer Fish / King Mackerel / King Fish)','Paplet (Pomfret / Indian Butter Fish)','Kekda (Crab)','Jhinga (Prawns and Shrimps)']
# serving=[100,100,100,100,100,100,100,100]
# calories=['206(25 to 26 grams of protein)','162(23 grams of protein)','97(17gms of protein)','205(17gms of protein)','134(26gms of protein)','175(18gms of protein)','115(21gms of protein)','99(21gms of protein)']

def heavy(request):
    m=['Rice (Brown)','Rice Parboiled','Rice Raw milled','Wheat flour','Refined flour','Ragi','Bajra','Jowar']
    a=[100,100,100,100,100,100,100,100]
    c=[353.7,351.5,356.3,320.2,351.8,320,347.9,334.1,]

    protein = ['Rawas (Indian Salmon)', 'Katla (Indian Carp or Bengal Carp)', 'Rohu (Roho or Carpo Fish)',
               'Bangda (Indian Mackerel)', 'Surmai (Seer Fish / King Mackerel / King Fish)',
               'Paplet (Pomfret / Indian Butter Fish)', 'Kekda (Crab)', 'Jhinga (Prawns and Shrimps)','Tuna',
               'Soya Chunks','Chicken Breast',"Paneer","Whole Egg"]
    serving = [100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,"One Egg"]
    calories = ['206(25 to 26 grams of protein)', '162(23 grams of protein)', '97(17gms of protein)',
                '205(17gms of protein)', '134(26gms of protein)', '175(18gms of protein)', '115(21gms of protein)',
                '99(21gms of protein)','225(33gm of protein)','345(52gms of protein)','165(31gms of protein)','293(14gms of protein)','72(14gms of protein)']

    context={
        'list':m,
        'list1':a,
        'list2':c,
        'p':protein,
        's':serving,
        'c':calories,
    }

    return render(request,'diet/heavy.html',context=context)

def light(request):
    m = ['Fruit smoothie','Egg and cheese English muffin','Peanut butter and banana sandwich','Trail mix','Cereal, milk, and banana','Yogurt and granola']
    i = ['Blend 8 ounces whole milk vanilla yogurt + ½ cup orange juice + 1 cup frozen berries','1 whole wheat English muffin + 2 teaspoons margarine spread or butter + 1 ounce cheese + 1 egg','2 slices of bread + 2 tablespoons peanut butter + 1 sliced banana','½ cup nuts, seeds, and dried fruit','1 cup presweetened wheat cereal + 8 ounces whole milk + 1 banana','1 cup whole milk flavored yogurt + ½ cup low-fat granola']
    c = [360,365,400,350,360,440]

    context = {
        'list': m,
        'list1': i,
        'list2': c,
    }

    return render(request, 'diet/light.html', context=context)