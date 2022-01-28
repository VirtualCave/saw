from django.shortcuts import render

from aws.infrastructure import scan_resources


def credentials(request):
    context = {}
    return render(request, "web/credentials.html")


def resources(request):
    context = dict()
    access_key = secret_access = None
    if request.method == "POST":
        access_key = request.POST.get("access_key_id")
        secret_access = request.POST.get("secret_access_key")
        aws_region = request.POST.get("aws_region")

    if access_key and secret_access and aws_region:
        context["aws_resources"] = scan_resources(access_key, secret_access, aws_region)

        return render(request, "web/resources.html", context=context)
    else:
        return render(request, "web/credentials.html", context=context)
