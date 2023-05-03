import unittest
from unittest.mock import MagicMock
from g_all_once import GameAllOnce

import pygame
pygame.init()  # Initialize the pygame video system
from g_all_once import GameAllOnce
import unittest

class TestGameAllOnce(unittest.TestCase):
    def setUp(self):
        self.game = GameAllOnce()

    def test_init(self):
        self.assertEqual(self.game.mode_name, "Game All Once")

    def test_handle_key_pressed(self):
        key = pygame.event.Event(pygame.KEYDOWN, unicode='a', key=pygame.K_a, mod=pygame.KMOD_NONE)
        self.game.handle_key_pressed(key)
        self.assertEqual(self.game.current_letter, "a")

    def test_handle_correct_key_pressed(self):
        key = pygame.event.Event(pygame.KEYDOWN, unicode='a', key=pygame.K_a, mod=pygame.KMOD_NONE)
        self.game.handle_key_pressed(key)
        self.game.handle_correct_key_pressed(key)
        self.assertEqual(self.game.current_letter, "b")

    def test_win(self):
        self.game.current_letter = "z"
        key = pygame.event.Event(pygame.KEYDOWN, unicode='z', key=pygame.K_z, mod=pygame.KMOD_NONE)
        self.game.handle_key_pressed(key)
        self.game.handle_correct_key_pressed(key)
        self.assertEqual(self.game.mode_name, "You Won!")


if __name__ == '__main__':
    unittest.main()
