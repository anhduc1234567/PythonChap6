# Chế độ mở file mode có thể là:
# ‘r’: mở file để đọc(mặc định).
# ‘w’: mở file để ghi. Xóa bỏ nội dung cũ có trong file trước khi ghi.
# ‘x’: mở để tạo file loại trừ, mở thất bại nếu file đã tồn tại.
# ‘a’: mở để ghi thêm nội dung vào cuối file.
# ‘b’: mở để đọc ghi nhị phân.
# ‘t’: mở để đọc ghi file text(mặc định).
# ‘+’: mở để cập nhật(gồm cả đọc và ghi).
# Ở chế độ ‘w’, ‘w+’, ‘a’, ‘a+’, ‘x’ hàm open() sẽ tạo file mới nếu file đó không tồn tại trước khi thao tác.
import os
import shutil

# old ='lesson6.2.py'
# new  = 'lesson62.py'
# # os.remove('le62.py')
# os.rename('lesson6.1.py','lesson61.py')
for i in os.listdir('.'):
    if os.path.isfile(i):
        print(i)
''' os.remove để xóa file trả về lỗi nếu nhữ là thư mục hàm shulti.rm xóa hết file trong thư muục'''
