from resource.health_check import Healthcheck

def create_api(api):
    try:
        api.add_resource(Healthcheck, '/healthcheck')
    except Exception as ex:
        print(ex)