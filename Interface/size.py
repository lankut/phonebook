def X_POS(window, width):
    return (window.winfo_screenwidth() - width) // 2

def Y_POS(window, height):
    return (window.winfo_screenheight() - height) // 2

def window_geometry(window, width, height):
    return f'{width}x{height}+{X_POS(window, width)}+{Y_POS(window, height)}'

MWW = MAIN_WINDOW_WIDTH = 500
MWH = MAIN_WINDOW_HEIGHT = 260

AWW = ADD_WINDOW_WIDTH = 300
AWH = ADD_WINDOW_HEIGHT = 100