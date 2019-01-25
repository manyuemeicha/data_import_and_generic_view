# from django.shortcuts import render
# from django.views.generic import TemplateView


# class IndexView(TemplateView):
#     template_name = 'index.html'


from test_im.models import Blog, Student
from django.views.generic import ListView


class ShowListView(ListView):
    template_name = 'index.html'
    # context_object_name = "a_list"  #这句的变量指的是返回的对象列表，在模板文件里遍历用，不写这句的话
    # 默认用model名_list变为结果集的变量，例如Blog的结果集变量是blog_list
    model = Blog

    # 可以对返回的列表数据做编辑
    def get_queryset(self):
        blog_list = Blog.objects.all()
        # for blog in blog_list:
            # blog.content += '列表项'
        return blog_list

    # 可以返回其他对象数据到模板中，添加一些变量(student_list)到上下文变量中，模板中用添加的变量来访问
    def get_context_data(self, **kwargs):
        # 代码相当于给父类即DetailView的关键字入参kwargs变量添加了一些变量
        kwargs['student_list'] = Student.objects.all().order_by('name')
        return super(ShowListView, self).get_context_data(**kwargs)


from django.views.generic import DetailView


class ShowDetailView(DetailView):
    template_name = 'detail.html'
    # context_object_name = "a_list"  #这句的变量指的是返回的对象列表，在模板文件里遍历用，不写这句的话
    # 默认用model名_list变为结果集的变量，例如Blog的结果集变量是blog_list
    model = Blog
    pk_url_kwarg = 'id'

    # 可以对返回的数据做编辑
    def get_object(self, queryset=None):
        obj = super(ShowDetailView, self).get_object()
        # obj.title += "的标题"
        return obj

    # 可以返回其他对象数据到模板中，添加一些变量到上下文变量kwargs中，模板中用添加的变量来访问
    # 代码相当于给父类即DetailView的关键字入参kwargs变量添加了一些变量
    def get_context_data(self, **kwargs):
        # kwargs['comment_list'] = self.object.blogcomment_set.all()   获取该文章的评论，注意是self，
        # self代表该子视图类对象，object不带s，带s会报错：'ShowDetailView' object has no attribute 'objects'
        # ，因为此处的object是DetailView类的属性，不是数据库API方法，后边的语法不太明白，
        # self.object的值是该主键的一条对象

        kwargs['this_blog_content'] = self.object.content  # 这句返回的是该条信息的content属性
        # 这里应该写到get_object方法里，因为是对该条数据进行编辑，这里是返回额外的数据到模板
        # 我想说的重点是self和object不带s，object不带s，带s会报错：'ShowDetailView' object has no attribute 'objects',
        # 因为此处的object是DetailView类的属性，不是数据库API方法
        # self.object的值是该主键的一条对象，因为self.object.content，返回的是该条信息的content
        return super(ShowDetailView, self).get_context_data(**kwargs)




