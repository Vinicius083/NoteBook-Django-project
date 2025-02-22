from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import User

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password: return JsonResponse({"error": "Preencha todos os campos"}, status=400)

        try: 
            user = User.objects.get(email=email)
            if user.password == password:
                return HttpResponseRedirect(reverse('notes:get_notes_from_user', args=[user.id]))
            else:
                return JsonResponse({"error": "Senha incorreta"}, status=401)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario não encontrado"}, status=404)
    return render(request, "user/login.html")


def create_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not name or not email or not password: return JsonResponse({"error": "Preencha todos os campos"}, status=400)

        userExists = User.objects.filter(email=email).exists()
        if userExists: return JsonResponse({"error": "Email já cadastrado"}, status=400)

        try: 
            user = User(name=name, email=email, password=password)
            user.save()
            return HttpResponseRedirect(reverse("login_usuario"))
        except Exception as e:
            return JsonResponse({"error": f"Erro ao criar usuário: {str(e)}"}, status=400)
        
    return render(request, "user/register.html")

def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    except User.DoesNotExist:
        return JsonResponse({"error": "Usuario não encontrado"}, status=404)