import time
from aiy.board import Led


def led_on(board):
    board.led.state = Led.ON


def led_off(board):
    board.led.state = Led.OFF


def led_blink(board, duration = 1, times = 1):
    for _ in range(times):
        led_on(board)
        time.sleep(duration)
        led_off(board)
        time.sleep(0.25)
