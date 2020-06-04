from django.contrib.auth import authenticate, models as auth_models
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from core import serializers as core_serializers
from core import models as core_models
from ThrottleLabs import utils


# Create your views here.

class SignUpViewSet(APIView):
    def post(self, request):
        serializer_instance = core_serializers.SignUpSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return utils.create_response(serializer_instance.errors, 400, message="Bad request")

        serializer_instance.save()
        return utils.create_response({}, 200, message="Success, Now You can sign in")


class SignInViewset(APIView):
    def post(self, request):

        serializer_instance = core_serializers.SignInSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return utils.create_response(serializer_instance.errors, 400, message="Bad request")

        user = authenticate(
            username=serializer_instance.validated_data.get("username"),
            password=serializer_instance.validated_data.get("password"),
        )

        if user and user.is_active:
            token_instance, _ = Token.objects.get_or_create(user=user)
            return utils.create_response(
                {"token": token_instance.key}, 200, message="Success"
            )
        else:
            return utils.create_response([], 403, message="Unauthorized")


class ActivitiesViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer_instance = core_serializers.PaginationSerializer(data=request.GET)

        if not serializer_instance.is_valid():
            return utils.create_response(serializer_instance.errors, 400, message="Bad request")

        page_no = serializer_instance.validated_data.get('page')
        user_qs = auth_models.User.objects.all().order_by('first_name')
        paginated_res = utils.pagination_on_queryset(user_qs, page_no)
        response_data = []

        for user in paginated_res[1]:
            user_data = {}
            user_data['real_name'] = user.first_name + " " + user.last_name
            user_data["tz"] = user.info.tz
            activities_qs = core_models.ActivityPeriods.objects.filter(user=user)
            user_data["activities"] = activities_qs.values('start_time', 'end_time')

            response_data.append(user_data)

        return utils.create_response(response_data, 200, name="members", message="success",
                                     extra={"page_total": paginated_res[0],
                                            "curr_page": page_no})


class DemoViewset(APIView):
    """to test some opertations outside main logic """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return utils.create_response(
            {"user_id": "1"}, 200, message="Success"
        )
