import pytest
from game import Field, Block, Tetromino


class TestField():
    @pytest.fixture
    def field(self):
        return Field([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])

    def test_is_allowed(self, field):
        # T型テトロミノのブロックを置く空間がある
        tetromino = Tetromino(2, 1, 0, 2)
        assert field.is_allowed(tetromino) is True

        # T型テトロミノのブロックが壁と重なる
        tetromino = Tetromino(1, 3, 0, 2)
        assert field.is_allowed(tetromino) is False

    def test_put_block(self, field):
        # プロックを設置
        field.put_block(2, 1, 2)
        assert field.tiles[1][2] == 2

        # 同じ位置に新しいプロックを設置すると重複により9になる
        field.put_block(2, 1, 2)
        assert field.tiles[1][2] == 9

    def test_check_3(self):
        field = Field([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])
        field.check()
        expected = Field([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])
        assert (field.tiles == expected.tiles).all()


class TestTetromino():
    def test_calc_blocks(self):
        # T型テトロミノのブロック位置
        tetromino = Tetromino(10, 10, 0, 2)
        blocks = tetromino.calc_blocks()
        expected = [
            Block(block.x + 10, block.y + 10)
            for block in Tetromino.get_blocks(2)
        ]
        assert blocks == expected

    def test_rotate(self):
        # 90度回転
        blocks = [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        rotated_blocks = Tetromino.rotate(blocks, 1)
        expected = [Block(0, 1), Block(0, 0), Block(-1, 0), Block(0, -1)]
        assert rotated_blocks == expected

        # 180度回転
        blocks = [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        rotated_blocks = Tetromino.rotate(blocks, 2)
        expected = [Block(1, 0), Block(0, 0), Block(0, 1), Block(-1, 0)]
        assert rotated_blocks == expected

        # 270度回転
        blocks = [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        rotated_blocks = Tetromino.rotate(blocks, 3)
        expected = [Block(0, -1), Block(0, 0), Block(1, 0), Block(0, 1)]
        assert rotated_blocks == expected

        # 360度回転
        blocks = [Block(-1, 0), Block(0, 0), Block(0, -1), Block(1, 0)]
        rotated_blocks = Tetromino.rotate(blocks, 4)
        assert rotated_blocks == blocks

    def test_get_blocks_undefined_shape(self):
        # 未定義のテトロミノ: 1
        with pytest.raises(ValueError):
            Tetromino.get_blocks(1)

        # 未定義のテトロミノ: 9
        with pytest.raises(ValueError):
            Tetromino.get_blocks(9)

    def test_next(self):
        # 右に1移動
        tetromino = Tetromino(3, 3, 0, 2)
        future_tetromino = tetromino.next({"x": 1, "y": 0, "rot": 0})
        assert (
            future_tetromino.x == 4
            and future_tetromino.y == 3
            and future_tetromino.rot == 0
        )

        # 左に1移動
        tetromino = Tetromino(3, 3, 0, 2)
        future_tetromino = tetromino.next({"x": -1, "y": 0, "rot": 0})
        assert (
            future_tetromino.x == 2
            and future_tetromino.y == 3
            and future_tetromino.rot == 0
        )

        # 下に1移動
        tetromino = Tetromino(3, 3, 0, 2)
        future_tetromino = tetromino.next({"x": 0, "y": 1, "rot": 0})
        assert (
            future_tetromino.x == 3
            and future_tetromino.y == 4
            and future_tetromino.rot == 0
        )

        # 90度回転
        tetromino = Tetromino(3, 3, 0, 2)
        future_tetromino = tetromino.next({"x": 0, "y": 0, "rot": 1})
        assert (
            future_tetromino.x == 3
            and future_tetromino.y == 3
            and future_tetromino.rot == 1
        )


class TestIntegration():
    @pytest.fixture
    def field(self):
        return Field([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])

    @pytest.fixture
    def tetromino(self):
        # T型テトロミノ
        return Tetromino(3, 1, 0, 2)

    def test_move(self, field, tetromino):
        # 右に1移動
        future_tetromino = tetromino.next({"x": 1, "y": 0, "rot": 0})
        assert field.is_allowed(future_tetromino) is True
        assert future_tetromino.x == 4

        # 下に1移動
        future_tetromino = tetromino.next({"x": 0, "y": 1, "rot": 0})
        assert field.is_allowed(future_tetromino) is True
        assert future_tetromino.y == 2

        # 90度回転
        future_tetromino = tetromino.next({"x": 0, "y": 0, "rot": 1})
        assert field.is_allowed(future_tetromino) is True
        assert future_tetromino.rot == 1
        
    def test_drop_and_fill(self):
        field = Field([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])
        tetromino = Tetromino(3, 2, 0, 2)  # T型テトロミノ

        # テトロミノをフィールドに設置
        for block in tetromino.calc_blocks():
            field.put_block(block.x, block.y, tetromino.shape)
        expected = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        assert (field.tiles == expected).all()

        # 埋まった行を削除
        field.check()
        expected = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        assert (field.tiles == expected).all()

    def test_game_over(self, field, tetromino):
        # テトロミノを重複させてゲームオーバーになるか確認
        for _ in range(2):
            for block in tetromino.calc_blocks():
                field.put_block(block.x, block.y, tetromino.shape)
        assert max(field.tiles.flatten()) == 9  # 9があるとゲームオーバー
