# title: Pyxel Experiment
# author: Suzuki Takafumi
# desc: A Pyxel Experiment
# license: MIT
# version: 0.1

import pyxel


class App:
    def __init__(self):
        # ウィンドウサイズの指定
        pyxel.init(160, 120)
        # リソースの読み込み
        pyxel.load("my_resource.pyxres")

        self.player_x = 80
        self.player_y = 50

        pyxel.run(self.update, self.draw)

    def update(self):
        # キー入力の処理
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= 1

    def draw(self):
        pyxel.cls(0)

        # プレイヤーを描画
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            0,
            0,
            7,
            7,
        )


# Pyxelアプリケーションの開始
app = App()
