from .models import Service


class ServiceView():
    def get_service_by_id(self, id):
        if Service.objects.filter(id=id).exists():
            return Service.objects.get(id=id)
        return None