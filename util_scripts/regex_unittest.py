import unittest
import re

def convert_markdown_to_html(markdown_text):
    # error pattern
    # pattern = r'!\[([^\]]+)(?:\\\[.*?\\\])?\]\(([^ ]+?)(?: "([^"]+)")?\)'

    pattern = r'!\[([^\]]+)(?:\\\[.*?\\\])?.*?\]\(([^ ]+?)(?: \"([^\"]+)\")?\)'
    match = re.search(pattern, markdown_text)

    if not match: return
    return ""

class TestMarkdownToHtmlConversion(unittest.TestCase):
    def test_convert_markdown_to_html(self):
        markdown_samples = [
            '![图10.11：常用面光源的形状。从左到右依次：球形、矩形（卡牌光源）、管状（线光源）、管状的聚焦发射光源（辐射能量在半球上的分布不均匀，集中在光源的法线方向上）。请注意它们所生成的、不同形状的高光。](images/Chapter-10/202306161234847.png "图10.11：常用面光源的形状。从左到右依次：球形、矩形（卡牌光源）、管状（线光源）、管状的聚焦发射光源（辐射能量在半球上的分布不均匀，集中在光源的法线方向上）。请注意它们所生成的、不同形状的高光。")',
            '![图10.12：一个管状光源。使用了代表性点方法来计算图像中的光照效果。 \[807\]](images/Chapter-10/202306161343643.png "图10.12：一个管状光源。使用了代表性点方法来计算图像中的光照效果。 \[807\]")',
            '![图10.12：这幅图像中的所有高光效果，都是使用随机屏幕空间反射算法渲染的 \\[1684\\]。 \[807\]](images/Chapter-10/202306161343643.png "图10.12：一个管状光源。使用了代表性点方法来计算图像中的光照效果。 \[807\]")',
            '![图11.40：这幅图像中的所有高光效果，都是使用随机屏幕空间反射（stochastic screen-space reflflection）算法渲染的 \[1684\] 。请注意反射效果的垂直拉伸，这是微表面模型反射的特点。](images/Chapter-11/202307051524918.png "图11.40：这幅图像中的所有高光效果，都是使用随机屏幕空间反射（stochastic screen-space reflflection）算法渲染的 \[1684\] 。请注意反射效果的垂直拉伸，这是微表面模型反射的特点。")',
            '![表14.1：用于散射和参与介质的符号。这些参数都可以依赖于波长（即RGB），从而实现彩色光线的吸收或者散射。其中相位函数 p 的单位是立体弧度（steradians，简写为sr）的逆（详见 章节8.1.1 ）。](images/Chapter-14/202308221938428.png "表14.1：用于散射和参与介质的符号。这些参数都可以依赖于波长（即RGB），从而实现彩色光线的吸收或者散射。其中相位函数 p 的单位是立体弧度（steradians，简写为sr）的逆（详见 章节8.1.1 ）。")'
        ]
        
        for sample in markdown_samples:
            result = convert_markdown_to_html(sample)
            self.assertNotEqual(result, None)

if __name__ == '__main__':
    unittest.main()