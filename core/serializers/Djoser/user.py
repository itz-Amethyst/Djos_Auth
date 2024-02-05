from djoser.serializers import UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name', 'username', 'email', 'last_login', 'is_staff', 'date_joined', 'country', 'phone_number', 'gender', 'company_name']
