from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):

    def process_response(self,request,response):

        response['Access-Control-Allow-Origin'] = "*"

        if request.method == "OPTIONS":
            # 允许你携带Content-Type请求头
            response['Access-Control-Allow-Headers'] = "Content-Type"
            # 允许你发送DELETE,PUT
            response['Access-Control-Allow-Methods'] = "PUT,DELETE"

        return response