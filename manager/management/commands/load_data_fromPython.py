from django.core.management.base import BaseCommand
# 其他必要的导入...

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **options):
        # 这里放置加载数据的代码
        # 例如，你可以调用你之前创建的脚本
        exec(open('student_data.py').read())
        self.stdout.write(self.style.SUCCESS('Successfully loaded student data'))
        exec(open('Teacher_data.py').read())
        self.stdout.write(self.style.SUCCESS('Successfully loaded teacher data'))
        exec(open('Course_data.py').read())
        self.stdout.write(self.style.SUCCESS('Successfully loaded course data'))
        exec(open('Schedule_data.py').read())
        self.stdout.write(self.style.SUCCESS('Successfully loaded schedule data'))
