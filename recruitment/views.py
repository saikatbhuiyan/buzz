import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timezone, timedelta

from .models import Apply, Cv

BASE_URL = "https://recruitment.fisdev.com"



def create_post(request):
  try:
    token = request.COOKIES['token']
    if token:
      payload = {}
      if request.method == 'POST':

        if 'name' in  request.POST:
          name = request.POST['name']
          payload['name'] = name

        if 'email' in request.POST:
          email = request.POST['email']
          payload['email'] = email

        if 'full_address' in request.POST:
          full_address = request.POST['full_address']
          payload['full_address'] = full_address

        if 'name_of_university' in request.POST:
          name_of_university = request.POST['name_of_university']
          payload['name_of_university'] = name_of_university

        if 'phone' in request.POST:
          phone = request.POST['phone']
          payload['phone'] = phone

        if 'graduation_year' in request.POST:
          graduation_year = request.POST['graduation_year']
          payload['graduation_year'] = graduation_year

        if 'cgpa' in request.POST:
          cgpa = request.POST['cgpa']
          payload['cgpa'] = cgpa

        if 'experience_in_months' in request.POST:
          experience_in_months = request.POST['experience_in_months']
          payload['experience_in_months'] = experience_in_months

        if 'current_work_place_name' in request.POST:
          current_work_place_name = request.POST['current_work_place_name']
          payload['current_work_place_name'] = current_work_place_name

        if 'expected_salary' in request.POST:
          expected_salary = request.POST['expected_salary']
          payload['expected_salary'] = expected_salary

        if 'field_buzz_reference' in request.POST:
          field_buzz_reference = request.POST['field_buzz_reference']
          payload['field_buzz_reference'] = field_buzz_reference

        if 'github_project_url' in request.POST:
          github_project_url = request.POST['github_project_url']
          payload['github_project_url'] = github_project_url

        if 'applying_in' in request.POST:
          applying_in = request.POST['applying_in']
          payload['applying_in'] = applying_in
    
        if payload:
          payload["cv_file"] = {}
          headers={'Content-Type':'application/json', 'Authorization': f'Token {token}'}
          POST_URL = f"{BASE_URL}/api/v1/recruiting-entities/"
          response = requests.post(POST_URL, headers=headers, json=payload)
          response = response.json()
          if response['success'] == False:
            error = response['message']
            messages.error(request, error)
            return redirect('posts')
          elif response['success'] == True:
            if response["cv_file"]["id"]:
              cv_file_token_id = response["cv_file"]["id"]
              payload["cv_file_token_id"] =  cv_file_token_id
              print(payload)
              payload.pop("cv_file")
              applying = Apply(**payload)
              applying.save()
              messages.success(request, "Your request successfully send.")
              return redirect('posts')
      
      else:
        return render(request, 'listings/create_post.html')
  
 
  except:
    return redirect('login')


def posts(request):
  try:
    token = request.COOKIES['token']
    if token:

      posts = Apply.objects.all()
      context = {
        'posts': posts
      }
      return render(request, 'listings/listings.html', context)

  except:
    return redirect('login')


def update_post(request, pk):
  try:
    token = request.COOKIES['token']
    if token:
      payload = {}
      post = get_object_or_404(Apply, pk=pk)

      payload['tsync_id'] = post.tsync_id
      
      if request.method == 'POST':
    
        if 'name' in  request.POST:
          name = request.POST['name']
          payload['name'] = name

        if 'email' in request.POST:
          email = request.POST['email']
          payload['email'] = email

        if 'full_address' in request.POST:
          full_address = request.POST['full_address']
          payload['full_address'] = full_address

        if 'name_of_university' in request.POST:
          name_of_university = request.POST['name_of_university']
          payload['name_of_university'] = name_of_university

        if 'phone' in request.POST:
          phone = request.POST['phone']
          payload['phone'] = phone

        if 'graduation_year' in request.POST:
          graduation_year = request.POST['graduation_year']
          payload['graduation_year'] = graduation_year

        if 'cgpa' in request.POST:
          cgpa = request.POST['cgpa']
          payload['cgpa'] = cgpa

        if 'experience_in_months' in request.POST:
          experience_in_months = request.POST['experience_in_months']
          payload['experience_in_months'] = experience_in_months

        if 'current_work_place_name' in request.POST:
          current_work_place_name = request.POST['current_work_place_name']
          payload['current_work_place_name'] = current_work_place_name

        if 'expected_salary' in request.POST:
          expected_salary = request.POST['expected_salary']
          payload['expected_salary'] = expected_salary

        if 'field_buzz_reference' in request.POST:
          field_buzz_reference = request.POST['field_buzz_reference']
          payload['field_buzz_reference'] = field_buzz_reference

        if 'github_project_url' in request.POST:
          github_project_url = request.POST['github_project_url']
          payload['github_project_url'] = github_project_url

        if 'applying_in' in request.POST:
          applying_in = request.POST['applying_in']
          payload['applying_in'] = applying_in

        if payload:
          payload["cv_file"] = {}
          on_spot_update_time = int(round((datetime.now(timezone.utc)).timestamp()) * 1e3)
          payload["on_spot_update_time"] = on_spot_update_time
          headers={'Content-Type':'application/json', 'Authorization': f'Token {token}'}
          POST_URL = f"{BASE_URL}/api/v1/recruiting-entities/"
          response = requests.post(POST_URL, headers=headers, json=payload)
          response = response.json()
          if response['success'] == False:
            error = response['message']
            messages.error(request, error)
            return redirect('/' + f'{pk}')

          elif response['success'] == True:

            if response["cv_file"]["id"]:
              payload.pop("cv_file")
              applying = get_object_or_404(Apply, pk=pk)

              if applying:
                applying.name = name
                applying.email = email
                applying.phone = phone
                applying.current_work_place_name = current_work_place_name
                applying.field_buzz_reference = field_buzz_reference
                applying.full_address = full_address
                applying.name_of_university = name_of_university
                applying.cgpa = cgpa
                applying.expected_salary = expected_salary
                applying.applying_in = applying_in
                applying.save()
                messages.success(request, "Your request successfully send.")
                return redirect('posts')
              else:
                return redirect('posts')
    
      context = {
            'post': post
          }
      return render(request, 'listings/listing.html', context)
  except:
    return redirect('login')

def upload_file(request, pk):
  token = request.COOKIES['token']
  if token:
    context = {}
    post = get_object_or_404(Apply, pk=pk)

    if request.method == 'POST':
      try:
        file = request.FILES['file']
        print(file)
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        print(filename)        
        url = fs.url(filename)
        print(url)        
        file_type = filename.split('.')[-1]
        if str(file_type) == "pdf":
            if file.size < 400000 :
                file_id = post.cv_file_token_id
                FILE_URL = f"https://recruitment.fisdev.com/api/file-object/{file_id}/"
                headers={ 'Content-Type'  : 'multipart/form-data; boundary=something', 'Authorization': f'Token {token}'}
                response = requests.put(FILE_URL, headers=headers, data=filename)
                response = response.json()
                if response['success'] == False:
                  error = response['message']
                  messages.error(request, error)
                  return redirect('/upload/' + f'{pk}')

                elif response['success'] == True:

                  cv = Cv(apply_id=file_id, file=file)
                  cv.save()
                  messages.success(request, "Your request successfully send.")
                  return redirect('posts')
            else:
                error = "File Size Is More Than 4 MB!"
                messages.error(request, error)
                return redirect('/upload/' + f"{pk}")

        else:
            fs.delete(filename)
            error = "File Type Is Not Supported, Please upload a pdf file"
            messages.error(request, error)
            return redirect("/upload/" + f"{pk}")
      except:
        error = "Please upload a file!"
        messages.error(request, error)
        return redirect('/upload/' + f"{pk}")

    context['post'] = post
    

    return render(request, 'listings/file_upload.html', context)
  else:
    return redirect('login')


def login_helper(request):
      if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        LOGIN_URL = "https://recruitment.fisdev.com/api/login/"
        user = requests.post(LOGIN_URL, json={
          "username": username,
          "password": password
        })

        user = user.json()

        if user['success'] == False:
          error = user['message']
          messages.error(request, error)
          return redirect('login')
        elif user['success'] == True:
          if user["token"]:
            token = user["token"]
            messages.success(request, "You are successfully logged in.")
            response = redirect(reverse('posts'))
            response.set_cookie('token', token)
            return response
      else:
        return render(request, 'accounts/login.html')

def login(request):
  try:
    token = request.COOKIES['token']
    if not token:
      return login_helper(request)
    else:
      return redirect('posts')
  except :
    return login_helper(request)
    # return redirect('/')
      
def logout(request):
  if request.method == 'POST':
    response = redirect('login')
    response.set_cookie('token', '')
    messages.success(request, 'You are now logged out')
    return response
