from django.shortcuts import render

def pago(request):
    return render (request , 'pagamento/boleto.html')
    
