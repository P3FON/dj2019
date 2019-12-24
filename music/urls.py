"""URLconfig of the music app.
Different URL patterns for an app are typically specified in the following ways:
    - for function-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view function>, name='<the corresponding view name>'>
        ]
    - for class-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view class>.as_view(), name='<the corresponding view name>'>
        ]
"""

from django.urls import path

from music import views
from music.views import PerformerListView, PerformerDetailView, FestivalListView, FestivalDetailView, \
    PerformerCreateView, PerformerUpdateView, PerformerDeleteView, FestivalCreateView, FestivalUpdateView, \
    FestivalDeleteView

urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('performers/', PerformerListView.as_view(), name='performer-list')
]

urlpatterns += [
    path('performers/<int:pk>/', PerformerDetailView.as_view(), name='performer-detail')
]

urlpatterns += [
    path('festivals/', FestivalListView.as_view(), name='festival-list')
]

urlpatterns += [
    path('festivals/<int:pk>/', FestivalDetailView.as_view(), name='festival-detail')
]

urlpatterns += [
    path('performers/create/', PerformerCreateView.as_view(), name='performer-create'), 
    path('performers/<int:pk>/update/', PerformerUpdateView.as_view(), name='performer-update'),
    path('performers/<int:pk>/delete/', PerformerDeleteView.as_view(), name='performer-delete')
]

urlpatterns += [
    path('festivals/create/', FestivalCreateView.as_view(), name='festival-create'), 
    path('festivals/<int:pk>/update/', FestivalUpdateView.as_view(), name='festival-update'),
    path('festivals/<int:pk>/delete/', FestivalDeleteView.as_view(), name='festival-delete')
]


