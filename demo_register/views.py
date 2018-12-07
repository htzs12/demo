from django.shortcuts import render
from .forms import RegisterForm,ImageForm
from .models import UserProfile
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import redirect,reverse
from .models import Image
from django.views.decorators.http import require_POST,require_GET
from django.core.paginator import Paginator


@require_GET
def index(request):
    all_user = UserProfile.objects.all()

    sort = request.GET.get('sort', '')

    if sort:
        if sort == 'birthday':
            all_user = UserProfile.objects.all().order_by('-birthday')
        elif sort == 'height':
            all_user = UserProfile.objects.all().order_by('-height')

    paginator = Paginator(all_user, 5)  # 每页分5
    page = request.GET.get('page')  # 获取浏览器页数请求参数
    page_demo = paginator.get_page(page)  # 获取分页数据对象
    current_page = page_demo.number  # 获取当前页码
    num_pages = paginator.num_pages  # 获取总页数

    around_count = 2  # 当前页前后2页

    left_has_more = False
    right_has_more = False

    if current_page <= around_count + 2:
        left_pages = range(1, current_page)
    else:
        left_has_more = True
        left_pages = range(current_page - around_count, current_page)

    if current_page >= num_pages - around_count - 1:
        right_pages = range(current_page + 1, num_pages + 1)
    else:
        right_has_more = True
        right_pages = range(current_page + 1, current_page + around_count + 1)

    return render(request,'index.html',locals())


class RegisterView(View):
    def get(self,request):
        return render(request,'regist.html')

    def post(self,request):
        register_form = RegisterForm(request.POST,request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('index'))
        else:
            return HttpResponse('注册失败，请检查格式！！！')


def image_demo(request):
    image_form = ImageForm(request.POST,request.FILES)
    if image_form.is_valid():
        image_form.save()


class modifyView(View):
    def get(self, request):
        return render(request,'modify.html')

    def post(self,request):
        register_form = RegisterForm(request.POST,request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect(reverse('index'))
        else:
            return HttpResponse('注册失败，请检查格式！！！')


@require_POST
def del_demo(request):
    user_id = request.POST.get('del')
    print(user_id)
    user = UserProfile.objects.get(id=user_id)
    user.delete()
    return render(request,'index.html')