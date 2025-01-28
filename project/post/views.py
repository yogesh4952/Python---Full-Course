from django.shortcuts import render
from .models import Post
from .models import FormData

def home(request):
    # Fetch all posts from the database
    posts = Post.objects.all()
    
    # Pass posts to the template through context
    context = {
        'posts': posts
    }
    
    return render(request, 'post/home.html', context)


def post_list(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)  # Get post by its primary key
    return render(request, 'post/post_detail.html', {'post': post})


def form(request):
    if request.method == 'POST':
        email = request.POST['email']  # Get the email from the form
        password = request.POST['password']  # Get the password
        name = request.POST['name']  # Get the name
        check = request.POST.get('check')  # Get the checkbox value (optional)

        # Create a new FormData instance and save the form data
        form_data = FormData(
            email=email,
            password=password,
            name=name,
            check=check if check else False  # Default to False if checkbox is not checked
        )
        form_data.save()  # Save to the database

        # Optionally, show a success message or redirect to another page
        return render(request, 'post/form.html', {'message': 'Form submitted successfully!'})

    return render(request, 'post/form.html')