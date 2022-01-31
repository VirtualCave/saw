from django.shortcuts import render

from aws.infrastructure import scan_resources


def main(request):
    """Main view"""
    context = dict()
    access_key_id = secret_access = aws_region = None
    tags = {}

    if request.method == "POST":
        access_key_id = request.POST.get("access_key")
        secret_access = request.POST.get("secret_access_key")
        aws_region = request.POST.get("aws_region")

        tag_1 = request.POST.get("tag_1")
        value_1 = request.POST.get("value_1")
        if tag_1 and value_1:
            tags[tag_1] = value_1

        tag_2 = request.POST.get("tag_2")
        value_2 = request.POST.get("value_2")
        if tag_2 and value_2:
            tags[tag_2] = value_2

    if access_key_id and secret_access and aws_region:
        context["aws_resources"] = scan_resources(
            access_key_id, secret_access, aws_region, tags
        )

        context["access_key_id"] = mask(access_key_id)
        context["secret_access_key"] = mask(secret_access)

    return render(request, "web/main.html", context=context)


def mask(key):
    head = key[0:3]
    body = "X" * (len(key) - 6)
    tail = key[-3:]
    return f"{head}{body}{tail}"
