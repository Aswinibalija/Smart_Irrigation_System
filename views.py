from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData, IrrigationControl
from .serializers import SensorDataSerializer, IrrigationControlSerializer

@api_view(['GET', 'POST'])
def sensor_data(request):
    if request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        latest = SensorData.objects.last()
        serializer = SensorDataSerializer(latest)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
# def control_irrigation(request):
#     if request.method == 'POST':
#         control = IrrigationControl.objects.first()
#         control.status = not control.status
#         control.save()
#         return Response({'status': control.status})
#     elif request.method == 'GET':
#         control = IrrigationControl.objects.first()
#         serializer = IrrigationControlSerializer(control)
#         return Response(serializer.data)

def control_irrigation(request):
    control = IrrigationControl.objects.first()  # Get the first control record
    
    if request.method == 'POST':
        # Example: Toggle irrigation status
        control.status = not control.status
        control.save()
        return Response({'status': 'success', 'irrigation_status': control.status})

    return Response({
        'status': control.status,
        'mode': control.mode,
        'pump_status': control.pump_status,
        'flow_rate': control.flow_rate,
        'schedule_time': control.schedule_time,
        'last_updated': control.last_updated,
    })

def dashboard(request):
    return render(request, 'dashboard.html')

def history(request):
    records = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'history.html', {'records': records, 'section': 'History of the Smart Irrigation Project'})

# def irrigation_control_page(request):
#     control = IrrigationControl.objects.first()
#     return render(request, 'control.html', {'control': control})

def about(request):
    return render(request, 'about.html', {'section': 'About the Smart Irrigation Project'})

def history(request):
    records = SensorData.objects.order_by('-timestamp')[:10]
    return render(request, 'history.html', {
        'records': records,
        'section': 'History of the Smart Irrigation Project'
    })

def irrigation_control_page(request):
    control = IrrigationControl.objects.first()  # Retrieve the first control record
    return render(request, 'control.html', {'control': control})
