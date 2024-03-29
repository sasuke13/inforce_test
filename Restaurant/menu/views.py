from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Menu
from menu.permissions import IsAdmin
from menu.serializer import MenuRestaurantSerializer, FullMenuSerializer

from datetime import datetime


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = FullMenuSerializer
    permission_classes = (IsAdmin, )


class MenuUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = FullMenuSerializer
    permission_classes = (IsAdmin,)


class TodayMenuListCreateAPIView(APIView):

    def get(self, request, *args, **kwargs):

        WEEKDAYS = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
        current_day = datetime.today().weekday()
        menus = Menu.objects.filter(day=WEEKDAYS[current_day]).order_by('restaurant')
        print(menus)
        results = {}

        for menu in menus:
            print(menu)
            if menu.restaurant in results:
                results[menu.restaurant].append(menu)
            else:
                results.update({menu.restaurant: [menu]})

        result_lst = [{"restaurant": k, "menu": v} for k, v in results.items()]
        print(result_lst)
        serializer = MenuRestaurantSerializer(result_lst, many=True)
        return Response(serializer.data)
