from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class JWTQueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        # print(token)
        if not token:
            raise AuthenticationFailed({"code": 401, "error": "登录成功后才能访问"})
        # 切割
        # 解密payload，判断是否过期
        # 验证第三段的合法性
        import jwt
        salt = settings.SECRET_KEY
        try:
            # 从token中获取payload【不校验合法性】
            # unverified_payload = jwt.decode(token, None, False)
            # print(unverified_payload)
            # 从token中获取payload【校验合法性】
            payload = jwt.decode(jwt=token, key=salt, algorithms=["HS256"])
            # print(payload)
            return (payload,token)
        except jwt.exceptions.ExpiredSignatureError:
            error = "token已失效"
            raise AuthenticationFailed({"code": 401, "error": error})
        except jwt.exceptions.DecodeError:
            error = "token已认证失败"
            raise AuthenticationFailed({"code": 401, "error": error})
        except jwt.exceptions.InvalidTokenError:
            error = "非法的token"
            raise AuthenticationFailed({"code": 401, "error": error})
        """ 三种操作
        1. 抛出异常，后续不在执行
        2. return 一个元组(1,2)认证通过，
        在视图中调用request.user就是元组的第一个值；
        另外一个就是request.auth
        3.None 
        """
