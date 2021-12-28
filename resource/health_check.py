from flask_restful import Resource

class Healthcheck(Resource):
    def get(self):
        try:
            return {'msg': 'App Running', 'code': 200}
        except Exception as e:
            print(e)