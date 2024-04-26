WIDTH, HEIGHT = 1300, 950
ROWS, COLS = 8, 8
SQUARE_SIZE = 90
TOP_PADDING = 90
BOARD_FRAME_WIDTH = 50
LEFT_SIDE_PADDING = BOARD_FRAME_WIDTH

BOARD_FILES = ('a','b','c','d','e','f','g','h')
BOARD_RANKS = (1,2,3,4,5,6,7,8)

DARKER_WHITE_COLOR = (200, 200, 200)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
WHITE_PIECE_COLOR = (255, 255, 255)
BLACK_PIECE_COLOR = (0, 0, 0)
LIGHT_SQUARE_COLOR = (215, 160, 110)
DARK_SQUARE_COLOR = (105, 75, 51)
GREEN_COLOR = (50, 205, 50)
DARK_GREEN_COLOR = (139, 230, 46)
RED_COLOR = (255, 68, 51)
GRAY_COLOR = (105, 105, 105)
DARK_GRAY_COLOR = (50, 50, 50)
LIGHT_GRAY_COLOR = (128, 116, 93)
YELLOW_COLOR = (204, 204, 0)
LIGHT_GREEN_COLOR = (144,238,144)
CHECK_COLOR = (173, 89, 83)
BOARD_FRAME_COLOR = (69, 49, 32)
TEST_COLOR = (105,75,55)

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
TEST_FEN = "r1b1k2r/p2p1p1p/1p3p2/2p3q1/2B1P1N1/5PP1/P6P/n2Q1K1R"
TEST2_FEN ="3r3r/p3kp1p/1p1p1p2/2p1q2P/P1B3P1/2Q3P1/7K/4R3"


EASY_MODE = {"depth": 1, "depth_change": False}
MED_MODE = {"depth": 3, "depth_change": False}
HARD_MODE = {"depth": 3, "depth_change": True}