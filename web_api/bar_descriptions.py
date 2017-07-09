import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333666", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = ["httpie", "django", "flask"]

plot_dicts = [
    {'value': 16101, 'label': 'Despcription of httpie'},
    {'value': 15028, 'label': 'Despcription of django'},
    {'value': 14798, 'label': 'Despcription of flask'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')