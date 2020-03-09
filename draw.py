import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# fig, ax = plt.subplots()
# plt.figure(figsize=(6, 6.5))

ax = plt.gca()

outer_origin_x = 0
outer_origin_y = 0
label_span = 0.05


def draw_outer(outer_origin_x, outer_origin_y, outer_x, outer_y):
    outer_origin_x = outer_origin_x
    outer_origin_y = outer_origin_y
    outer_x = outer_x
    outer_y = outer_y

    outer = np.array([outer_origin_x, outer_origin_y])
    outer_x = outer_x / 100
    outer_y = outer_y / 100
    p_outer_x = outer_x / 2
    p_outer_y = outer_y / 2

    rect = plt.Rectangle(outer, outer_x, outer_y, fill=False, color='r')
    rect.set_transform(ax.transAxes)
    rect.set_clip_on(False)
    ax.add_patch(rect)

    ax.text(outer_origin_x + p_outer_x, outer_origin_y - label_span, outer_x * 100,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes)

    ax.text(outer_origin_x - label_span, outer_origin_y + p_outer_y, outer_y * 100,
            horizontalalignment='right',
            verticalalignment='center',
            rotation='vertical',
            transform=ax.transAxes)


def draw_inner(outer_origin_x, outer_origin_y, outer_x, outer_y, inner_x, inner_y, inner_type, inner_offset=None):
    label_offset = False
    outer_x = outer_x / 100
    outer_y = outer_y / 100
    inner_x = inner_x / 100
    inner_y = inner_y / 100
    p_inner_x = outer_origin_x
    p_inner_y = outer_origin_y
    p_label_x = outer_origin_x
    p_label_y = outer_origin_y
    if inner_type == 1:
        # E开口
        if not inner_offset:
            inner_offset = (outer_x - inner_x) / 2
            inner_origin_x = outer_origin_x + (outer_x - inner_x) / 2
        else:
            inner_offset = inner_offset / 100
            label_offset = True
            inner_origin_x = outer_origin_x + inner_offset
        inner_origin_y = outer_origin_y
        p_inner_x = inner_origin_x + inner_x / 2
        p_inner_y = inner_origin_y + inner_y / 2
        p_label_x = outer_origin_x + inner_offset / 2
        p_label_y = outer_origin_y - label_span
    elif inner_type == 2:
        # D开口
        if not inner_offset:
            inner_offset = (outer_x - inner_x) / 2
            inner_origin_y = outer_origin_y + (outer_y - inner_y) / 2
        else:
            inner_offset = inner_offset / 100
            inner_origin_y = outer_origin_y + inner_offset
            label_offset = True
        inner_origin_x = 0
        p_inner_x = inner_origin_x + inner_x / 2
        p_inner_y = inner_origin_y + label_span
        p_label_x = inner_origin_x - label_span
        p_label_y = outer_origin_y + inner_offset / 2
        print('p_label_y:', p_label_y)
    elif inner_type == 3:
        # D开口
        inner_origin_x = outer_origin_x + (outer_x - inner_x)
        if not inner_offset:
            inner_offset = (outer_x - inner_x) / 2
            inner_origin_y = outer_origin_y + (outer_y - inner_y) / 2
        else:
            inner_offset = inner_offset / 100
            inner_origin_y = outer_origin_y + inner_offset
            label_offset = True
        p_inner_x = inner_origin_x + inner_x / 2
        p_inner_x = outer_origin_x + outer_x - label_span
        print('p_inner_x:', p_inner_x)
#         p_inner_y = inner_origin_y + inner_y / 2 + label_span
        p_label_x = outer_origin_x + outer_x - label_span
        p_label_y = outer_origin_y + inner_offset / 2
    elif inner_type == 4:
        # B开口
        inner_origin_x = outer_origin_x
        inner_origin_y = outer_origin_y
        inner_offset = 0
        p_inner_x = inner_origin_x + inner_x / 2
        p_inner_y = inner_origin_y + inner_y / 2
        p_label_x = inner_origin_x - label_span
        p_label_y = inner_origin_y - label_span
    elif inner_type == 5:
        # A开口
        inner_origin_x = outer_origin_x + outer_x - inner_x
        inner_origin_y = outer_origin_y
        inner_offset = 0
        p_inner_x = inner_origin_x + inner_x / 2
        p_inner_y = inner_origin_y + inner_y / 2
        p_label_x = inner_origin_x - label_span
        p_label_y = inner_origin_y - label_span
        pass
    print('inner:', inner_x, inner_y)
    print('inner_origin_x,y', inner_origin_x, inner_origin_y, p_inner_x, p_inner_y, p_label_x, p_label_y)
    inner = np.array([inner_origin_x, inner_origin_y])
    rect1 = plt.Rectangle(inner, inner_x, inner_y, fill=False, color='b')
    rect1.set_transform(ax.transAxes)
    rect1.set_clip_on(False)
    ax.add_patch(rect1)

#     p_inner_x = inner_origin_x + inner_x / 2
#     p_inner_y = inner_origin_y + inner_y / 2
    ax.text(p_inner_x, inner_origin_y + label_span, inner_x * 100,
            horizontalalignment='left',
            verticalalignment='top',
            color='b',
            transform=ax.transAxes)

    ax.text(inner_origin_x + label_span, p_inner_y, inner_y * 100,
            horizontalalignment='right',
            verticalalignment='center',
            rotation='vertical',
            color='b',
            transform=ax.transAxes)
    if label_offset:
        ax.text(p_label_x, p_label_y, inner_offset * 100,
                horizontalalignment='left',
                verticalalignment='top',
                color='b',
                transform=ax.transAxes)


# draw_inner(50, 25, 2)


plt.title('Black180', loc='left', y=-0.1)
draw_outer(0, 0, 200, 50)
draw_inner(0, 0, 200, 50, 100, 25, 4, 15)
draw_outer(2.1, -0, 60, 70)
draw_inner(2.1, -0, 60, 70, 30, 20, 5)

draw_outer(2.9, -0, 70, 80)
draw_inner(2.9, -0, 70, 80, 30, 20, 5)

draw_outer(0, -2.5, 60, 120)
draw_inner(0, -2.5, 60, 120, 30, 20, 2)
plt.axis('equal')
plt.axis('off')
# plt.gcf().set_size_inches(20, 20)
# plt.gca().xaxis.set_major_locator(plt.NullLocator())
# plt.gca().yaxis.set_major_locator(plt.NullLocator())
# plt.subplots_adjust(top=0.5, bottom=0.1, right=0.3, left=0.1, hspace=0.2, wspace=0.2)
# plt.margins(0, 0)
# plt.savefig('./test2.jpg', dpi=100, bbox_inches='tight')
plt.savefig('./test2.jpg', dpi=100, bbox_inches='tight')
# plt.show()
