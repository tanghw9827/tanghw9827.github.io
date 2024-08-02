from PIL import Image
import os

def resize_image(input_path, width_ratio):
    # 打开原始图片
    original_image = Image.open(input_path)
    
    # 获取原始图片尺寸
    original_width, original_height = original_image.size
    
    # 计算新的宽度和高度
    new_width = int(original_width * width_ratio)
    new_height = int(original_height * width_ratio)
    
    # 调整图片大小
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    
    # 生成输出路径
    directory, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(directory, f"resized_{name}{ext}")
    
    # 保存调整后的图片
    resized_image.save(output_path)
    
    print(f"Resized image saved to {output_path}")

# 设置输入图片路径和宽度比例
input_image_path = '/home/sti/myblog/source/images/Dynamic_Bicycle_Model.png'
width_ratio = 1.0  # 比如将图片宽度调整为原始图片的50%

# 调整图片大小
resize_image(input_image_path, width_ratio)
