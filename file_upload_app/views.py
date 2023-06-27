from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile


def upload_file(request):
    uploaded_files = UploadedFile.objects.all()

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            new_file = UploadedFile(file=uploaded_file)
            new_file.save()
            return render(request, 'file_list.html', {'uploaded_files': uploaded_files, 'success_message': 'File uploaded successfully!'})
    else:
        form = FileUploadForm()

    return render(request, 'upload_file.html', {'form': form, 'uploaded_files': uploaded_files})




from django.shortcuts import render, get_object_or_404

def view_file_content(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id)
    with open(uploaded_file.file.path, 'r') as file:
        file_content = file.read()
    return render(request, 'file_content.html', {'file_content': file_content})

from file_upload_app.models import UploadedFile

def delete_all_files(request):
    uploaded_files = UploadedFile.objects.all()
    for file in uploaded_files:
        file.file.delete()  
        file.delete()  
    return redirect('upload_file')

def delete_file(request, file_id):
    file = UploadedFile.objects.get(id=file_id)
    file.file.delete()  
    file.delete()  
    return redirect('upload_file')


# Cmd promy - curl -X POST -F "file=@C:\Users\jhnithi\OneDrive - Johnson Controls\Desktop\windoscurltest.txt" -H "X-CSRFToken: Y78n7YwmPZqY3nSlpcc6lSXP08lFEmCv" http://localhost:8000/upload/
# CSRF_TOKEN - Y78n7YwmPZqY3nSlpcc6lSXP08lFEmCv