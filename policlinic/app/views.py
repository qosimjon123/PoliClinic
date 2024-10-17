from django.shortcuts import render, redirect
from .models import Records, Doctor
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def register_record(request):
    doctors = Doctor.objects.all()  # Список врачей для отображения в форме
    if request.method == 'POST':
        first_name, second_name, last_name = request.POST['fullName'].split(' ')
        email = request.POST['email']
        phone = request.POST['phone']
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        comment = request.POST.get('comments', '')

        doctor = Doctor.objects.get(id=doctor_id)

        new_record = Records(
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            email=email,
            phone=phone,
            doctor=doctor,
            date=date,
            time=time,
            comment=comment
        )
        new_record.save()

        return redirect('show_user_records')

    return render(request, 'register_record.html', {'doctors': doctors})


def show_all_records(request):
    all_records = Records.objects.all()
    print(all_records)
    print("записи")
    return render(request, 'show_all_records.html', {'records': all_records})


def show_user_records(request):
    user_records = Records.objects.filter(user_id=request.user.id)
    return render(request, 'show_user_records.html', {'records': user_records})
