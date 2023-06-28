import os, sys, time, datetime
import threading
import django
base_apth = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(base_apth)
# 将项目路径加入到系统path中，这样在导入模型等模块时就不会报模块找不到了
sys.path.append(base_apth)
os.environ['DJANGO_SETTINGS_MODULE'] ='dorm_management_system.settings' # 注意：base_django_api 是我的模块名，你在使用时需要跟换为你的模块
django.setup()
# from base.models import ConfDict
import schedule


def job():
    print("定时")


def confdict_handle():
    # 设置定时任务
    schedule.every().day.at("10:24").do(job)
    # 运行定时任务
    while True:
        schedule.run_pending()
        time.sleep(1)



def main():
    '''
    主函数，用于启动所有定时任务，因为当前定时任务是手动实现，因此可以自由发挥
    '''
    try:
        # 启动定时任务，多个任务时，使用多线程
        task1 = threading.Thread(target=confdict_handle)
        task1.start()
    except Exception as e:
        print('发生异常：%s' % str(e))


if __name__ == '__main__':
    main()
