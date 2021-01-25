from ctypes import WinDLL, byref, Structure, sizeof
from ctypes.wintypes import SHORT, WCHAR, UINT, ULONG, DWORD
from functools import reduce
from os import get_terminal_size
class COORD(Structure): _fields_ = [("X", SHORT), ("Y", SHORT)]
class CONSOLE_FONT_INFOEX(Structure): _fields_ = [("cbSize", ULONG), ("nFont", DWORD), ("dwFontSize", COORD), ("FontFamily", UINT), ("FontWeight", UINT), ("FaceName", WCHAR * 32)]
font = CONSOLE_FONT_INFOEX()
font.cbSize, font.dwFontSize.Y = sizeof(CONSOLE_FONT_INFOEX), 1
WinDLL("kernel32.dll").SetCurrentConsoleFontEx(WinDLL("kernel32.dll").GetStdHandle(-11), False, byref(font))
WinDLL('user32').ShowWindow(WinDLL('user32').GetForegroundWindow(), 3)
print((lambda a, b, c, d, e, f, g: reduce(lambda x, y: x + y, map(lambda y, c = c, d = d, a = a, b = b, g = g, L = lambda yc, c = c, d = d, a = a, b = b, i = e, f = f, g = g: reduce(lambda x, y: x + y, map(lambda x, xc = a, yc = yc, a = a, b = b, i = i, f = f, F = lambda xc, yc, x, y, k, f = lambda xc, yc, x, y, k, f: (k <= 0) or (x * x + y * y >= 4.0) or 1 + f(xc, yc, x * x - y * y + xc, 2.0 * x * y + yc, k - 1, f): f(xc, yc, x, y, k, f): chr(63 - F(a + x * (b - a) / f, yc, 0, 0, i)), range(f))): L(c + y * (d - c) / g), range(g))))(-2.1, 0.7, -1.2, 1.2, 30, get_terminal_size().columns, get_terminal_size().lines))
