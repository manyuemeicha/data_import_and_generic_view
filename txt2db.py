# import os
# # 如果是外部文件调用django内的模块 文件等，需要设置下环境变量和django.setup（）
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_import.settings") # 设置环境变量
# import django
# if django.VERSION >= (1, 7):
#     django.setup()  # 好像是重新加载什么，目的是为了找模块的机制更新?
#
#
# def main():
#     from test_im.models import Blog
#     with open("oldblog.txt") as file:
#         for line in file:
#             title, content = line.split("****")
#             print(Blog.objects.get_or_create(title=title, content=content))
# if __name__ == "__main__":
#     main()
#     print("Done!!!")


class AA:
    def ad(self, **kwargs):
        a = kwargs
        return a


class Ad(AA):
    def ad(self, **kwargs):
        kwargs["a"] = 1
        return super(Ad, self).ad(**kwargs)

print(Ad().ad(b=2))