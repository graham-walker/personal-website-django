from personal.models import Bio

def bio(request):
    bio = Bio.objects.all().first()
    return {
        'bio': bio
    }
