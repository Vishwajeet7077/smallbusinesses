from django.urls import path, include
from .views import EventList, EventDetail, EventCreate, EventDelete, EventUpdate

urlpatterns = [
    path('events/', EventList.as_view(), name='events'),
    path('event-detail/<int:pk>', EventDetail.as_view(), name='event-detail'),
    path('event-create/', EventCreate.as_view(), name='event-create'),
    path('event-delete/<int:pk>', EventDelete.as_view(), name='event-delete'),
    path('event-update/<int:pk>', EventUpdate.as_view(), name='event-update'),
]
