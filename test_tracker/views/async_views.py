from django.http import JsonResponse
from django.template.loader import render_to_string

from test_tracker.models.test_result import TestResult


def async_update_results(request, pk):
    print(pk)
    print(type(pk))
    data = dict()
    if request.method == 'GET':
        result = TestResult.objects.get(id=pk)
        # asyncSettings.dataKey = 'result'
        data['result'] = render_to_string(
            'test_tracker/_dashboard_table_result.html',
            {'result': result, 'product': result.testcase.product},
            request=request
        )
        return JsonResponse(data)

def async_update_case():
    pass
