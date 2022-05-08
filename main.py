from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

ui.run()
# テキストを表示します
ui.label('some label')

ui.run()

# 画像を表示します。
ui.image('http://placeimg.com/640/360/tech')
base64 = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAASABIAAD/4QCMRXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAACKgAwAEAAAAAQAAACMAAAAA/8IAEQgAIwAiAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAMCBAEFAAYHCAkKC//EAMMQAAEDAwIEAwQGBAcGBAgGcwECAAMRBBIhBTETIhAGQVEyFGFxIweBIJFCFaFSM7EkYjAWwXLRQ5I0ggjhU0AlYxc18JNzolBEsoPxJlQ2ZJR0wmDShKMYcOInRTdls1V1pJXDhfLTRnaA40dWZrQJChkaKCkqODk6SElKV1hZWmdoaWp3eHl6hoeIiYqQlpeYmZqgpaanqKmqsLW2t7i5usDExcbHyMnK0NTV1tfY2drg5OXm5+jp6vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAQIAAwQFBgcICQoL/8QAwxEAAgIBAwMDAgMFAgUCBASHAQACEQMQEiEEIDFBEwUwIjJRFEAGMyNhQhVxUjSBUCSRoUOxFgdiNVPw0SVgwUThcvEXgmM2cCZFVJInotIICQoYGRooKSo3ODk6RkdISUpVVldYWVpkZWZnaGlqc3R1dnd4eXqAg4SFhoeIiYqQk5SVlpeYmZqgo6SlpqeoqaqwsrO0tba3uLm6wMLDxMXGx8jJytDT1NXW19jZ2uDi4+Tl5ufo6ery8/T19vf4+fr/2wBDAAwMDAwMDBUMDBUeFRUVHikeHh4eKTQpKSkpKTQ+NDQ0NDQ0Pj4+Pj4+Pj5LS0tLS0tXV1dXV2JiYmJiYmJiYmL/2wBDAQ8QEBkXGSsXFytnRjlGZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2f/2gAMAwEAAhEDEQAAAeqBgCIareozvbaK3avBqa52teT6He3z0TqCUZa22r//2gAIAQEAAQUCaVVKTjGnLFqSqqlGuciX+87YgM8ScWhAx5KWUJUdJClKadMye6O//9oACAEDEQE/AUxI86A0ynfb/9oACAECEQE/ASaYZBLxpKNinFh2dv8A/9oACAEBAAY/AmUniHVXxfVx7ZIP9x0GlOJdfa+BeVentkSWR66jsI1HUfF+f4l1UykiqR/CypAorg6n/hvuH5nv/8QAMxABAAMAAgICAgIDAQEAAAILAREAITFBUWFxgZGhscHw0RDh8SAwQFBgcICQoLDA0OD/2gAIAQEAAT8hrchP08Nlp8V+7MHK/wCcEXw8q94vkT4K5DD0fpsJBFkwYvy/8cJBuuX7l82UhL9HmlzVKCOfi+3/ADe6Z2jgePxcMYN/xxYQtAu8UCj/ALXDvn/sBxRB/g3/AL//2gAMAwEAAhEDEQAAEE5gPHEUEAP/xAAzEQEBAQADAAECBQUBAQABAQkBABEhMRBBUWEgcfCRgaGx0cHh8TBAUGBwgJCgsMDQ4P/aAAgBAxEBPxAN4PZaNJuOW/g//9oACAECEQE/EAGt2fwmfzBp3X8P/9oACAEBAAE/ELGubg74j5M+RuAgxMrE4g5c4qAjQh1Oh9GL3/xggJDuHs5H2fY1rQIGDISTZ3KuGYzkk8dSkh4Ah8TJ8c0SsIco+yPRD76/486QSwOdnIpjvmvjAQ8pEx4ixlVcDldAdtawTzP5CSqs1wAPeJDMz0nwvHVlRSYTI1ic6b58RUC4kuSTXmFOJuxknJgsgDQMkjQgj/gCBHee6QjzflUA4/5//9k='
ui.image(base64).style('width:30px')

ui.run()

# マークダウン要素
ui.markdown('### Headline\nWith hyperlink to [GitHub](https://github.com/zauberzeug/nicegui).')

ui.run()

# ボタン要素
def button_increment():
    global button_count
    button_count += 1
    button_result.set_text(f'pressed: {button_count}')

button_count = 0
ui.button('Button', on_click=button_increment)
button_result = ui.label('pressed: 0')

ui.run()

# HTML要素
ui.html('<p>demo paragraph in <strong>html</strong></p>')

ui.run()

ui.checkbox('check me', on_change=lambda e: checkbox_state.set_text(e.value))
with ui.row():
    ui.label('the checkbox is:')
    checkbox_state = ui.label('False')

ui.run()

# スイッチ
ui.switch('switch me', on_change=lambda e: switch_state.set_text('ON' if e.value else'OFF'))
with ui.row():
    ui.label('the switch is:')
    switch_state = ui.label('OFF')

ui.run()

# スライダー
slider = ui.slider(min=0, max=100, value=50).props('label')
ui.label().bind_text_from(slider, 'value')

ui.run()

# テキスト入力
ui.input(
    label='ここに入力',
    placeholder='press ENTER to apply',
    on_change=lambda e: result.set_text('you typed: ' + e.value),
).classes('w-full')
result = ui.label('')

ui.run()

# 数値入力
number_input = ui.number(label='Number', value=3.1415927, format='%.2f')
with ui.row():
    ui.label('underlying value: ')
    ui.label().bind_text_from(number_input, 'value')

ui.run()

# ラジオ選択
radio = ui.radio([1, 2, 3], value=1).props('inline')
ui.radio({1: 'A', 2: 'B', 3: 'C'}, value=1).props('inline').bind_value(radio, 'value')

ui.run()

# トグル要素
toggle = ui.toggle([1, 2, 3], value=1)
ui.toggle({1: 'A', 2: 'B', 3: 'C'}, value=1).bind_value(toggle, 'value')

ui.run()

# ドロップダウン選択
with ui.row():
    select = ui.select([1, 2, 3], value=1).props('inline')
    ui.select({1: 'One', 2: 'Two', 3: 'Three'}, value=1).props('inline').bind_value(select, 'value')

ui.run()

# ファイルアップロード

ui.upload(on_upload=lambda files: content.set_text(files))
content = ui.label()

ui.run()

# グラフプロット
import numpy as np
from matplotlib import pyplot as plt

with ui.plot(figsize=(2.5, 1.8)):
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x, y, '-')
    plt.xlabel('time (s)')
    plt.ylabel('Damped oscillation')

ui.run()

# 折線

lines = ui.line_plot(n=2, limit=20, figsize=(2.5, 1.8)).with_legend(['sin', 'cos'], loc='upper center', ncol=2)
line_updates = ui.timer(0.1, lambda: lines.push([datetime.now()], [
    [np.sin(datetime.now().timestamp()) + 0.02 * np.random.randn()],
    [np.cos(datetime.now().timestamp()) + 0.02 * np.random.randn()],
]), active=False)
ui.checkbox('グラフ描写').bind_value(line_updates, 'active')

ui.run()

# ログ表示
from datetime import datetime

log = ui.log(max_lines=10).classes('h-16')
ui.button('ボタンを押すと、ログを表示', on_click=lambda: log.push(datetime.now().strftime("%X.%f")[:-5]))

ui.run()

#3D表示

with ui.scene(width=200, height=200) as scene:
    scene.sphere().material('#4488ff')
    scene.cylinder(1, 0.5, 2, 20).material('#ff8800', opacity=0.5).move(-2, 1)
    scene.extrusion([[0, 0], [0, 1], [1, 0.5]], 0.1).material('#ff8888').move(-2, -2)

    with scene.group().move(z=2):
        box1 = scene.box().move(x=2)
        scene.box().move(y=2).rotate(0.25, 0.5, 0.75)
        scene.box(wireframe=True).material('#888888').move(x=2, y=2)

    scene.line([-4, 0, 0], [-4, 2, 0]).material('#ff0000')
    scene.curve([-4, -2, 0], [-4, -1, 0], [-3, -1, 0], [-3, 0, 0]).material('#008800')

    logo = "https://avatars.githubusercontent.com/u/2843826"
    scene.texture(logo, [[[0, 3, 0], [3, 3, 0]], [[0, 0, 0], [3, 0, 0]]]).move(1, -2)

    teapot = 'https://upload.wikimedia.org/wikipedia/commons/9/93/Utah_teapot_(solid).stl'
    scene.stl(teapot).scale(0.2).move(-3, 4)

ui.run()

#　チャート
from numpy.random import random

def update():
    chart.options.series[0].data[:] = random(2)

chart = ui.chart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
}).classes('max-w-full h-64')
ui.button('Update', on_click=update)

ui.run()

# テーブル
def update():
    table.options.rowData[0].age += 1

table = ui.table({
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
    ],
    'rowData': [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol', 'age': 42},
    ],
}).classes('max-h-40')
ui.button('Update', on_click=update)

ui.run()

# ツールチップ
with ui.row():
    ui.button().props('icon=thumb_up').tooltip('I like this')
    ui.label('tooltips').classes('q-mt-sm').tooltip('tooltips are shown on mouse over')

ui.run()


# タイマー
from datetime import datetime

with ui.row().classes('items-center'):
    clock = ui.label()
    t = ui.timer(interval=0.1, callback=lambda: clock.set_text(datetime.now().strftime("%X.%f")[:-5]))
    ui.checkbox('active').bind_value(t, 'active')

with ui.row():
    def lazy_update():
        new_text = datetime.now().strftime('%X.%f')[:-5]
        if lazy_clock.text[:8] == new_text[:8]:
            return False
        lazy_clock.text = new_text
    lazy_clock = ui.label()
    ui.timer(interval=0.1, callback=lazy_update)

ui.run()