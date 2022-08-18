from django.shortcuts import render,HttpResponse
from django.db.models import Q
from .models import *
# Create your views here.
def ResultView(request):
    result_ob=Result.objects.order_by('-score')
    print(result_ob)
    context={
        "result":result_ob,
    }
    return render(request,'result.html',context)




def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    result = Result.objects.filter(Student_id__icontains=q)
    results = []
    for p in result:
      product_json = {}
      result_json = p.Student_id
      results.append(result_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)


def Search(request):
    if request.method == 'POST':
        key=request.POST['search']
        result=Result.objects.filter(Q(Student_id__icontains=key) | Q(student_name__icontains=key) | Q(score__icontains=key)).order_by('-score')

        context={
            's_r':result,
        }
    return render(request,'search.html',context)


def test4(request):
    return render(request,'test4.html')


def test(request):
    return render(request,'test.html')