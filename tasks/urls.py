from django.urls import path

from tasks.views import TaskBookList, TaskBookDetail, TaskBookCreate

urlpatterns = [
    path('', TaskBookList.as_view(), name='menu'),
    path('your_task_books/', TaskBookList.as_view(), name='menu'),
    path('your_task_books/<uuid:pk>', TaskBookDetail.as_view(),
         name='book_detail'),
    path('your_task_books/create_task_book/', TaskBookCreate.as_view(),
         name='create_task_book')
]
