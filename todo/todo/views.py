from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from add_task.models import Tasks
from . forms import UserRegistrationForm
from django.contrib.auth import login


#def login_page(request):
    #return render(request,'register/login.html')

@login_required
def todo_list(request):
    if request.method=="POST":
        task=request.POST.get('task')
        user=request.user
        
        save_task=Tasks(tasks=task,user=user)
        save_task.save()
        
        return redirect("todo_list")
    
    tasks=Tasks.objects.filter(user=request.user)  
    return render(request,'to-do.html',{'tasks':tasks})

@login_required
def edit_todo(request,task_id):
    task=get_object_or_404(Tasks,pk=task_id,user=request.user)
    
    if request.method=="POST":
        update_task=request.POST.get('task')
        task.tasks = update_task
        task.save()
        
        return redirect("todo_list")

    return render(request,'update.html',{'task':task})

@login_required
def delete_todo(request,task_id):
    task=get_object_or_404(Tasks,pk=task_id,user=request.user)
    task.delete()
    return redirect('todo_list')
   
#Registration

def register(request):
    
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            
            return redirect("todo_list")
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
      
        