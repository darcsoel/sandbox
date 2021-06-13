"""Simple example of tkinter gui"""

from tkinter import Button, Label, Tk


class MainWindow:
    """
    Main GUI window
    """

    window_width = 700
    window_height = 700

    def __init__(self, root):
        self._root = root

        self._lbl = None
        self._button = None

        self._label_text = 'Hello'
        self._button_text = 'First button'
        self._button_on_click_text = 'Hello from button'

    def first_button(self):
        """onclick listener"""

        self._lbl.configure(text=self._button_on_click_text)

    def _add_label(self):
        self._lbl = Label(self._root, text=self._label_text)
        self._lbl.grid(column=0, row=0)
        return self

    def _add_button(self):
        self._button = Button(self._root, text=self._button_text,
                              command=self.first_button)
        self._button.grid(column=1, row=0)
        return self

    def build(self):
        """build window"""
        self._add_label()._add_button()


def main():
    """run window"""

    window = Tk()
    window.title = 'Simple GUI'

    program = MainWindow(window)
    program.build()

    window.geometry(f'{program.window_width}x{program.window_height}')
    window.mainloop()


if __name__ == '__main__':
    main()
