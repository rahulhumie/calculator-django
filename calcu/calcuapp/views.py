from django.shortcuts import render

def calculator(request):
    result1 = None
    if request.method == 'POST':
        fn = float(request.POST.get('fn'))
        sn = float(request.POST.get('sn'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result1 = fn + sn
        elif operation == 'subtract':
            result1 = fn - sn
        elif operation == 'multiply':
            result1 = fn * sn
        elif operation == 'divide':
            if sn != 0:
                result1 = fn / sn
            else:
                result1 = "Cannot divide by zero!"

    return render(request, 'calcu/cal.html', {'result': result1})
