from django.shortcuts import render,redirect
from myapp.models import Register, Join
# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method == "POST":
		Name = request.POST['Name']
		Email=request.POST['Email']
		Mobile_no=request.POST['Mobile_no']
		Course=request.POST['Course']
		Source=request.POST['Source']
		Lead_status = request.POST['Lead_status']
		Demo_date = request.POST['Demo_date']
		Counsler = request.POST['Counsler']
		Remark = request.POST['Remark']
		Register.objects.create(Name=Name,Email=Email,Mobile_no=Mobile_no,Course=Course,Source=Source,Lead_status=Lead_status,Demo_date=Demo_date,Counsler=Counsler,Remark=Remark)
		return redirect('Walkins')
	return render(request,'Register.html')

# def single_data(request,pk):
# 	data = Register.objects.get(pk=pk)

	# return render(request,'single_data.html')	

def data_page(request):
	data = Register.objects.all()
	return render(request,'data_page.html',{'details':data})

def Walkins(request):
	data1 = Register.objects.all()
	return render(request,'Walkins.html',{'details':data1})


def Calling(request):
	return render(request,'Calling.html')

def Calling1(request):
	if request.method == "POST":
		Course = request.POST['Course']
		Name = request.POST['Name']
		regi = Register.objects.filter(Course=Course,Name=Name)
		return render(request,'Calling1.html',{'details':regi})
	return render(request,'Calling1.html')
	

def Counselling(request):
	return render(request,'Counselling.html')

def Counselling1(request):
	if request.method == "POST":
		Course = request.POST['Course']
		Demo_date = request.POST['Demo_date']
		regi = Register.objects.filter(Course=Course,Demo_date=Demo_date)
		return render(request,'Counselling1.html',{'details':regi})
	return render(request,'Counselling1.html')
 	
def joinning(request):
	if request.method == "POST":
		name = request.POST['name']
		Course = request.POST['Course']
		DOJ = request.POST['DOJ']
		DOC = request.POST['DOC']
		Course_fee = request.POST['Course_fee']
		Instructor = request.POST['Instructor']
		Aadhar = request.POST['Aadhar']
		mobile = request.POST['mobile']
		email = request.POST['email']
		remark = request.POST['remark']
		status = request.POST['status']
		Join.objects.create(name=name,Course=Course,DOJ=DOJ,DOC=DOC,Course_fee=Course_fee,Instructor=Instructor,Aadhar=Aadhar,
			mobile=mobile,email=email,remark=remark,status=status)
		return redirect('current')
	return render(request,'joinning.html')


def current(request):
	data=Join.objects.all()
	return render(request,'current.html',{'details':data})

def edit(request,id):
	form = Register.objects.get(id=id)
	return render(request,'edit.html',{'details':form})

def Willing(request,id):
	data = Register.objects.get(id=id)
	if request.method=="POST":
		Demo_date=request.POST['Demo_date']
		Name = request.POST['Name']
		data.Demo_date=Demo_date
		data.Name=Name
		data.save()
		return redirect('Walkins')
	return render(request, 'edit.html',{'details':data})

def Dead(request,id):
	data = Register.objects.get(id=id)
	data.delete()
	return redirect('Walkins')	

def complete(request,id):
	data = Join.objects.get(id=id)
	data.status='complete'
	data.save()
	return redirect('students')

def delay(request,id):
	data = Join.objects.get(id=id)
	data.status='delay'
	data.save()
	return redirect('students')

def rejoin(request,id):
	data = Join.objects.get(id=id)
	data.status='stoped'
	data.save()
	return redirect('students')


def students(request):
	data1 = Join.objects.filter(status='complete')
	data2 = Join.objects.filter(status='delay')
	data3 = Join.objects.filter(status='stoped')
	return render(request,'students.html',{'details1':data1,'details2':data2,'details3':data3})


def Register_modelform(request):
	return render(request,'Register_modelform')





 
