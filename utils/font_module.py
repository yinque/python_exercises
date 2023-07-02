import os
from PIL import ImageFont


class SystemFont:
    def __init__(self):
        self.__font_path_map = dict()  # （字体名，字体样式）-字体文件名map
        self.__name_style_map = dict()  # 字体名-字体样式map
        # self.__path_font_map = dict()  # 字体文件名-字体map
        folder_path = 'C:\\Windows\\Fonts\\'
        # 获取文件夹中的所有文件名
        file_names = os.listdir(folder_path)
        # 筛选出字体文件名
        font_files = [file for file in file_names if file.endswith('.ttf')]
        # 排除不支持的字体文件
        font_files.remove("mstmc.ttf")
        # 遍历所有字体文件名
        for font_file in font_files:
            # 使用ImageFont.TrueType加载字体文件
            font = ImageFont.truetype(font_file)
            # 获取字体的名称
            font = font.getname()
            name = font[0]
            style = font[1]
            if self.__name_style_map.get(name):
                self.__name_style_map[name].append(style)
            else:
                self.__name_style_map[name] = [style]
            self.__font_path_map[font] = font_file
            # self.__path_font_map[font_file] = font_name

    def get_styles(self, name):
        """
        获取字体支持的样式
        :param name: 字体名
        :return: 列表
        """
        return self.__name_style_map[name]

    def get_path(self, font: tuple):
        """
        获取字体路径
        :param font: 字体，格式为(字体名,字体样式)
        :return: 字符串
        """
        return self.__font_path_map[font]


# test
if __name__ == '__main__':
    font_name = "Arial"
    sf = SystemFont()
    font_styles = sf.get_styles(font_name)
    print(f"{font_name}'s style: {font_styles}")
    path = sf.get_path((font_name, font_styles[0]))
    print(f"{font_name} {font_styles[0]}'s path: {path}")
