from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import PersonalInformation,IDCard,House,Marriage
from django.contrib import messages
from django.urls import reverse
from django.views import View







def house_info(request):
 if request.method == 'POST':
        
    try:
       
        p_information = PersonalInformation.objects.get(pk=request.POST['PI_ID'])
        
        PI_ID=p_information
        House_No = request.POST.get('House_No')
        Woreda = request.POST.get('Woreda')
        Region = request.POST.get('Region')
        House_type = request.POST.get('House_type')
        Family_size = request.POST.get('Family_size')
        Family_names = request.POST.get('Family_names')
        
  
        
        house_info = House(
            PI_ID= PI_ID,
            House_No=House_No,
            Woreda=Woreda,
            Region=Region,
            House_type=House_type,
            Family_size=Family_size,
            Family_names=Family_names
        )
        
        house_info.save()
        messages.success(request, "House Information Added Successfully!")
        
    except PersonalInformation.DoesNotExist:
        messages.error(request, "Personal Information not found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        
 personal_info_list = PersonalInformation.objects.all()
 context = {'p_info_list': personal_info_list,}
 return render(request, 'Hregistration.html', context)   

def Marriage_info(request):
    if request.method == 'POST':
       
            H_ID_No = PersonalInformation.objects.get(pk=request.POST['H_ID_No'])
            W_ID_No = PersonalInformation.objects.get(pk=request.POST['W_ID_No'])
            
            MAR_ID=request.POST.get('MAR_ID')
            Given_date = request.POST.get('Given_date')
            Marriage_type = request.POST.get('Marriage_type')
            witness_1 = request.POST.get('witness_1')
            witness_2 = request.POST.get('witness_2')
            Witness_1_sign = request.POST.get('Witness_1_sign')
            Witness_2_sign = request.POST.get('Witness_2_sign')
            
            marriage_info = Marriage(
                H_ID_No=H_ID_No,
                W_ID_No=W_ID_No,
                MAR_ID=MAR_ID,
                Given_date=Given_date,
                Marriage_type=Marriage_type,
                witness_1=witness_1,
                witness_2=witness_2,
                Witness_1_sign=Witness_1_sign,
                Witness_2_sign=Witness_2_sign,
            )
            marriage_info.save()
            messages.success(request, "Marriage Information Added Successfully!")
       
    
    idcard_info_list = PersonalInformation.objects.all()
    context = {
        'I1_info_list': idcard_info_list,
        'I2_info_list': idcard_info_list,
    }
    return render(request, 'Marriage.html', context)
 
def Birth_info(request):
    if request.method == 'POST':
       
            H_ID_No = PersonalInformation.objects.get(pk=request.POST['H_ID_No'])
            W_ID_No = PersonalInformation.objects.get(pk=request.POST['W_ID_No'])
            
            MAR_ID=request.POST.get('MAR_ID')
            Given_date = request.POST.get('Given_date')
            Marriage_type = request.POST.get('Marriage_type')
            witness_1 = request.POST.get('witness_1')
            witness_2 = request.POST.get('witness_2')
            Witness_1_sign = request.POST.get('Witness_1_sign')
            Witness_2_sign = request.POST.get('Witness_2_sign')
            
            marriage_info = Marriage(
                H_ID_No=H_ID_No,
                W_ID_No=W_ID_No,
                MAR_ID=MAR_ID,
                Given_date=Given_date,
                Marriage_type=Marriage_type,
                witness_1=witness_1,
                witness_2=witness_2,
                Witness_1_sign=Witness_1_sign,
                Witness_2_sign=Witness_2_sign,
            )
            marriage_info.save()
            messages.success(request, "Marriage Information Added Successfully!")
       
    
    idcard_info_list = PersonalInformation.objects.all()
    context = {
        'I1_info_list': idcard_info_list,
        'I2_info_list': idcard_info_list,
    }
    return render(request, 'Marriage.html', context)

 
 

 
 
 
 
 
 
def Id_info_detail(request, pk):
    id_info = get_object_or_404(IDCard, pk=pk)
    return render(request, 'Id_info_detail.html', {'id_info': id_info}) 

def id_list(request):
    id_info = IDCard.objects.all()
    return render(request, 'id_info_list.html', {'id_info': id_info})   







def personal_info_list(request):
    personal_info = PersonalInformation.objects.all()
    return render(request, 'personal_info_list.html', {'personal_info': personal_info})
def personal_info_detail(request, pk):
    personal_info = get_object_or_404(PersonalInformation, pk=pk)
    return render(request, 'personal_info_detail.html', {'personal_info': personal_info})

def update_personal_info(request, pk):
    personal_info = get_object_or_404(PersonalInformation, pk=pk)
    success_message = None
    if request.method == 'POST':
        PI_ID=request.POST.get('PI_ID')
        F_Name = request.POST.get('F_Name')
        M_Name = request.POST.get('M_Name')
        L_Name = request.POST.get('L_Name')
        sex = request.POST.get('sex')
        Dob = request.POST.get('Dob')
        Place_of_birth = request.POST.get('Place_of_birth')
        Date_of_registration=request.POST.get('Date_of_registration')
        Nationality = request.POST.get('Nationality')
        Phone_number = request.POST.get('Phone_number')
        photograph = request.FILES.get('photograph')
        
        personal_info = PersonalInformation(
            PI_ID=PI_ID,
            F_Name=F_Name,
            M_Name=M_Name,
            L_Name=L_Name,
            sex=sex,
            Dob=Dob,
            Place_of_birth=Place_of_birth,
            Date_of_registration=Date_of_registration,
            Nationality=Nationality,
            Phone_number=Phone_number,
            photograph=photograph
        )
        personal_info.save()
        
        success_message = 'Personal information updated successfully!'
        
        return redirect('personal_info_list.html')
    
    return render(request, 'update_personal_info.html', {
    'personal_info': personal_info,
    'success_message': success_message
    })
def delete_personal_info(request, pk):
    personal_info = get_object_or_404(PersonalInformation, pk=pk)
    if request.method == 'POST':
        personal_info.delete() 
        return redirect('personal_info_list')
    return render(request, 'delete_personal_info.html', {'personal_info': personal_info})





def id_info(request):
    if request.method == 'POST':
        try:
            p_information = PersonalInformation.objects.get(pk=request.POST['PI_ID'])
            h_information = House.objects.get(pk=request.POST['House_No'])
            House_No = h_information
            PI_ID = p_information
            Emergency_cont_name = request.POST.get('Emergency_cont_name')
            Emergency_cont_number = request.POST.get('Emergency_cont_number')
            Given_date = request.POST.get('Given_date')
            Expire_date = request.POST.get('Expire_date')
            Blood_Type = request.POST.get('Blood_Type')

            
            if not Emergency_cont_name.isalpha():
                messages.error(request, "Emergency contact name should contain only letters.")
                raise ValueError("Validation Error")

            
            if not (Emergency_cont_number.isdigit() and len(Emergency_cont_number) == 13 and Emergency_cont_number.startswith('+251')):
                messages.error(request, "Emergency contact number should be 13 digits and start with 0.")
                raise ValueError("Validation Error")

            
            if datetime.strptime(Expire_date, '%Y-%m-%d') < datetime.strptime(Given_date, '%Y-%m-%d'):
                messages.error(request, "Expire date should not be before the given date.")
                raise ValueError("Validation Error")

            id_info = IDCard(
                House_No=House_No,
                PI_ID=PI_ID,
                Emergency_cont_name=Emergency_cont_name,
                Emergency_cont_number=Emergency_cont_number,
                Given_date=Given_date,
                Expire_date=Expire_date,
                Blood_Type=Blood_Type
            )

            id_info.save()
            messages.success(request, "ID Information Added Successfully!")

        except House.DoesNotExist:
            messages.error(request, "House Information not found.")
        except ValueError:
            pass  # Handled validation error
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    house_info_list = House.objects.all()
    context = {'h_info_list': house_info_list}
    return render(request, 'IDcard.html', context)

def personal_info(request):
    if request.method == 'POST':
        try:
            PI_ID = request.POST.get('PI_ID')
            F_Name = request.POST.get('F_Name')
            M_Name = request.POST.get('M_Name')
            L_Name = request.POST.get('L_Name')
            Mother_Name = request.POST.get('Mother_Name')
            sex = request.POST.get('sex')
            Dob = request.POST.get('Dob')
            Place_of_birth = request.POST.get('Place_of_birth')
            Date_of_registration = request.POST.get('Date_of_registration')
            Nationality = request.POST.get('Nationality')
            Phone_number = request.POST.get('Phone_number')
            photograph = request.FILES.get('photograph')

          
            if not (F_Name.isalpha() and M_Name.isalpha() and L_Name.isalpha() and Mother_Name.isalpha()):
                messages.error(request, "Names should contain only letters.")
                return render(request, 'p_form.html')

            
            if not (Phone_number.isdigit() and len(Phone_number) == 10 and Phone_number.startswith('0')):
                messages.error(request, "Phone number should be 10 digits and start with 0")
                return render(request, 'p_form.html')

            personal_info = PersonalInformation(
                PI_ID=PI_ID,
                F_Name=F_Name,
                M_Name=M_Name,
                L_Name=L_Name,
                Mother_Name=Mother_Name,
                sex=sex,
                Dob=Dob,
                Place_of_birth=Place_of_birth,
                Date_of_registration=Date_of_registration,
                Nationality=Nationality,
                Phone_number=Phone_number,
                photograph=photograph
            )
            
            personal_info.save()
            messages.success(request, "Personal information added successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'p_form.html')


def home(request):
    return render(request, "Home.html")
def Rofficer(request):
    return render(request, "Rofficer.html")

def Services(request):
    return render(request, "services.html")

def About(request):
    return render(request, "About.html")




