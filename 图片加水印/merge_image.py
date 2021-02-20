from PIL import Image, ImageFont, ImageDraw


def merge_image(back_image_path, water_image_path, save_path, content, font_style, font_color='black'):

	"""
	:param back_image_path: str 背景图片路径
	:param water_image_path: str 水印图片路径
	:param save_path: str 保存路径
	:param content: str 文字内容
	:param font_style: str 字体样式
	:param font_color: int (0-255) 字体颜色
	:return:
	"""

	back_image = Image.open(back_image_path)
	water_image = Image.open(water_image_path)
	water_image.resize((100, 100))

	# 获取背景图宽高
	w, h = back_image.size
	# 水印图片坐标
	box = (w - 100, h - 100)
	# 在背景图片上绘制水印图片
	back_image.paste(water_image, box=box)
	# 文字绘制
	back_image_draw = ImageDraw.Draw(back_image)
	font_size = 15
	font_style = font_style
	content = content
	content_width = len(content) * font_size
	# 计算文字坐标
	font_w = w - 100 + ((100 - content_width) // 2)
	font_h = h - 120
	# 字体
	font = ImageFont.truetype(font_style, font_size)
	back_image_draw.text((font_w, font_h), content, font=font, fill=font_color)
	# 保存图片
	back_image.save(save_path)


merge_image('back.jpg', 'water.jpg', 'merge.jpg', '微信公众号', 'font.ttf', 'black')