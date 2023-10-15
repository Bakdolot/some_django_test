def brackets_validator(parametr_string: str) -> bool:
    all_brackets = "()[]{}"
    close_brackets = ")]}"
    brackets = {")": "(", "]": "[", "}": "{"}

    tmp: list[str] = []
    for i in parametr_string:
        if i not in all_brackets:
            continue
        if i in close_brackets:
            if not tmp or brackets[i] != tmp.pop():
                return False
        else:
            tmp.append(i)

    return not tmp


def get_client_ip(request):
    x_forwarded_for = request.headers.get("x-forwarded-for")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
