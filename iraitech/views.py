from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json


# iterative method for question one
def q1_iterative(x, n):
    result = 0

    for i in range(1, n + 1):
        result += 1 / (x ** i)

    return result


# recursive method for question one
def q1_recursive(x, n):
    if n == 0:
        return 0

    tempResult = 1 / (x ** n)
    return tempResult + q1_recursive(x, n - 1)


def q2(n):
    if n % 2 == 0:
        return (n + 1) ** 2 + 1

    return (n + 1) ** 2 - 1


def q3(x, y, a, b):
    return (x / y) ** (a + b)


@login_required()
def calculate(req):
    if(req.method == "POST"):
        data = json.loads(req.body)
        x = int(data.get('x'))
        n = int(data.get('n'))
        print(x)
        print(n)
        ans = q1_recursive(x, n)
        return JsonResponse({"answer": ans})
    return render(req, 'iraitech/question1.html')
