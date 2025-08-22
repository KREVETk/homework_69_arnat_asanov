import json
from json import JSONDecodeError
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest


def calculate(request, operation):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        body = json.loads(request.body)
        a = body.get("A")
        b = body.get("B")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return JsonResponse({"error": "Both A and B must be numbers"}, status=400)

        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                return JsonResponse({"error": "Division by zero!"}, status=400)
            result = a / b
        else:
            return HttpResponseBadRequest("Unknown operation")

        return JsonResponse({"answer": result})

    except JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
