from django.views import View
from django.http import JsonResponse
from django_serverside_datatable import datatable


class ServerSideDatatableView(View):
    queryset = None
    columns = None

    def get(self, request, *args, **kwargs):
        result = datatable.DataTablesServer(request, self.columns, self.queryset).output_result()
        return JsonResponse(result, safe=False)



