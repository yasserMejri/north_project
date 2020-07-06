from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# from wagtail_svgmap import ImageMapBlock

# class ColumnBlock(blocks.StreamBlock):
#     heading = blocks.CharBlock(classname="full title")
#     paragraph = blocks.RichTextBlock()
#     image = ImageChooserBlock()

#     class Meta:
#         template = '500.html'


class Hero_1(blocks.StructBlock):
    hero_img = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    paragraph = blocks.CharBlock(required=False)
    # theme = blocks.ChoiceBlock(choices=[
    #     ('white', 'White'),
    #     ('black', 'Black'),
    # ], default='white')
    class Meta:
        template = "blocks/hero_1.html"


class TwoCol_2(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, classname="full title")
    col1 = blocks.CharBlock(required=False)
    col2 = blocks.CharBlock(required=False)

    class Meta:
        template = "blocks/twocol_2.html"


class ImgText_3(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    preamble = blocks.RichTextBlock(required=False)
    body = blocks.RichTextBlock(required=False)
    call_to_action = blocks.PageChooserBlock(required=False)
    order = blocks.ChoiceBlock(
        choices=[("left", "Left Image"), ("right", "Right Image")], default="white"
    )

    class Meta:
        template = "blocks/imgtext_3.html"


class ImgOnText_4(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(default="", classname="full title")
    preamble = blocks.RichTextBlock(required=False)

    class Meta:
        template = "blocks/imgontext_4.html"

class Featured_5(blocks.StructBlock):
    class Meta:
        template = "blocks/featured_5.html"

class Services_11(blocks.StructBlock):
    class Meta:
        template = "blocks/services_11.html"

class Staff_6(blocks.StructBlock):
    title = blocks.CharBlock(required=False, classname="full title")

    class Meta:
        template = "blocks/staff_6.html"


class CImgText_8(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    richtext = blocks.RichTextBlock(required=False)
    order = blocks.ChoiceBlock(
        choices=[("left", "Left Image"), ("right", "Right Image")]
    )

    class Meta:
        template = "blocks/cimgtext_8.html"


class ImgColorText_9(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    preamble = blocks.RichTextBlock(required=False)
    call_to_action = blocks.PageChooserBlock(required=False)
    order = blocks.ChoiceBlock(
        choices=[("left", "Left Image"), ("right", "Right Image")]
    )
    
    class Meta:
        template = "blocks/imgcolortext_9.html"


class DoubleImgText_10(blocks.StructBlock):
    image1 = ImageChooserBlock()
    image2 = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    preamble = blocks.RichTextBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)

    order = blocks.ChoiceBlock(
        choices=[("left", "Left Image"), ("right", "Right Image")]
    )

    class Meta:
        template = "blocks/doubleimgtext_10.html"


class QuestionBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(required=False, classname="full title")
    paragraph = blocks.RichTextBlock(required=False)

    class Meta:
        template = "blocks/question.html"


class USP_12(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(required=False, classname="full title")
    paragraph = blocks.CharBlock(required=False)
    question1 = blocks.CharBlock(required=False)
    paragraph1 = blocks.CharBlock(required=False)
    question2 = blocks.CharBlock(required=False)
    paragraph2 = blocks.CharBlock(required=False)
    question3 = blocks.CharBlock(required=False)
    paragraph3 = blocks.CharBlock(required=False)
    question4 = blocks.CharBlock(required=False)
    paragraph4 = blocks.CharBlock(required=False)
    order = blocks.ChoiceBlock(
        choices=[("left", "Left Image"), ("right", "Right Image")]
    )

    class Meta:
        template = "blocks/usp_12.html"


# class TwoColumnBlock(blocks.StructBlock):

#     left_column = ColumnBlock(icon='arrow-right', label='Left column content')
#     right_column = ColumnBlock(icon='arrow-right', label='Right column content')

#     class Meta:
#         template = '404.html'
#         icon = 'placeholder'
#         label = 'Two Columns'
