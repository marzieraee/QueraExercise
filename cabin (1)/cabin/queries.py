from os import access
from .models import *
from django.db.models import Sum, Count
from django.db.models import F  
from django.db.models.functions import Coalesce



def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    q = Payment.objects.aggregate(income=Sum('amount'))
    return q


def query_2(x):
    q = Payment.objects.filter(ride__request__rider=x).aggregate(payment_sum=Sum('amount'))
    return q


def query_3():
    q = Driver.objects.filter(car__car_type='A').distinct().count()
    return q


def query_4():
    q = RideRequest.objects.filter(ride=None)
    return q


def query_5(t):
    q = Rider.objects.annotate(amount=Sum(
        'riderequest__ride__payment__amount')).filter(amount__gte=t)
    return q


def query_6():
    q2 =  Driver.objects.extra(select={'length':'Length("account__last_name")'}
                               ).annotate(cars=Count('car')).order_by(
                                'length').order_by('-cars').first()
    q=q2.account.get()
    
    return q


def query_7():
    q = Rider.objects.filter(riderequest__ride__car__car_type='A').annotate(n=Count('riderequest__ride__car__car_type'))
    return q


def query_8(x):
    
    
    q = Driver.objects.filter(car__model__gte=x).values('account__email').distinct()
    
    
    return q


def query_9():
    q = Driver.objects.all().annotate(n=Count('car__ride'))
    return q


def query_10():
    q = Driver.objects.values('account__first_name').annotate(n=Count('car__ride'))
    return q


def query_11(n, c):
    q2=Car.objects.filter(color=c,model__gte=n)
    q=Driver.objects.filter(car__in=q2).distinct()
    return q


def query_12(n, c):
    q = Driver.objects.filter(car__color=c).filter(car__model__gte=n).distinct()
    return q


def query_13(n, m):
    
    q = Ride.objects.filter(car__owner__account__first_name= n,
                        request__rider__account__first_name=m).annotate(
                        duration=Coalesce(F('dropoff_time'),0)-Coalesce(F('pickup_time'),0)).aggregate(
                        sum_duration=Sum('duration'))
                        
    return q                    


def query_14(x, y, r):
    q = 'your query here'
    return q


def query_15(n, c):
    q = 'your query here'
    return q


def query_16(x, t):
    q = 'your query here'
    return q


def query_17():
    q = 'your query here'
    return q


def query_18():
    
    q = 'your query here'
    return q


def query_19(n, t):
    q = 'your query here'
    return q


def query_20():
    q = 'your query here'
    return q
