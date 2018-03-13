from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
# These below library for PDF generating
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO, StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def index(request):
    return render(request, 'membership/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/membership/login')
    else:
        form = RegistrationForm()

    return render(request, 'membership/signup.html', {'form': form})

def profile(request):
    args = {'user': request.user}
    return render(request, 'membership/profile.html', args)

def update_profile(request):
    id = UserProfile.objects.get(user=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('/membership/profile')
    else:
        form = UserProfileForm(instance=id)

    return render(request, 'membership/profile_update.html', {
        'form': form,
        'id' : id,
    })

def some_view(request):
    # Get information from database
    userprofile = UserProfile.objects.get(user=request.user.id)
    user = User.objects.get(id=request.user.id)

    org_name = "SUOMEN VIETNAMILAISTEN BUDDHALAISTEN YHDYSKUNTA"
    id_number = userprofile.social_number
    fullname = user.first_name + " " + user.last_name
    address = userprofile.address
    postal_code = userprofile.postal_code
    city = userprofile.city

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()
    # Create a new PDF, so that later we can merge it with the form
    can = canvas.Canvas(buffer)
    can.drawString(63, 707, org_name)
    can.drawString(63, 527, org_name)
    can.drawString(63, 673, id_number)
    can.drawString(190, 673, fullname )
    can.drawString(63, 637, city )
    can.drawString(190, 637, address)
    can.drawString(100, 63, "Hello world, This is Henry")
    can.save()

    # Move to the beginning of the buffer
    buffer.seek(0)
    new_pdf = PdfFileReader(buffer)

    # Read the form that need to be filled
    form = PdfFileReader(open("/home/duyledinh/Dropbox/Apps/lientamcms/membership/memberform2.pdf", "rb"))
    if form.isEncrypted:
        form.decrypt('');

    # Merge and output the pdf.
    output = PdfFileWriter()
    page = form.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # Send output to response.
    outputStream = BytesIO()
    output.write(outputStream)
    response.write(outputStream.getvalue())

    return response
