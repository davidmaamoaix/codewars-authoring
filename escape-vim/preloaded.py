valid_keys = [*list('abcdefghijklmnopqrstuvwxyz'), 'shift', 'enter', ';']

class Keyboard:

    def __init__(self):
        self.__down = set()
        self.__broken = False
        self.__saved = False
        self.__exited = False
        self.__cmd_mode = False
        self.__curr = ''
        self.__side = ''

    @property
    def broken(self):
        return self.__broken

    @property
    def pressed(self):
        return list(self.__down)

    @property
    def saved(self):
        return self.__saved

    @property
    def closed(self):
        return self.__exited

    def __run(self):
        if self.__exited or not self.__cmd_mode: return
        self.__cmd_mode = False

        if self.__curr == 'w':
            self.__saved = True
        elif self.__curr == 'q':
            self.__exited = True
        elif self.__curr == 'wq' or self.__curr == 'x':
            self.__saved = True
            self.__exited = True

        self.__curr = ''

    def __check_side(self):
        if self.__side[-2 :] == 'ZZ':
            self.__saved = True
            self.__exited = True

    def key_down(self, key):
        key = key.lower()
        if key in self.__down: self.__broken = True
        if self.__broken: return

        if not key in valid_keys:
            raise ValueError(f'"{key}" is not a valid key!')

        self.__down.add(key)
        if self.__exited: return

        if key == 'enter':
            self.__run()
        elif key == ';':
            k = ':' if 'shift' in self.__down else ';'
            if self.__cmd_mode:
                self.__curr += k
            else:
                self.__cmd_mode = True
                self.__side = ''
        elif key == 'shift':
            pass
        else:
            key = key.upper() if 'shift' in self.__down else key
            if self.__cmd_mode:
                self.__curr += key
            else:
                self.__side += key
                self.__check_side()

    def key_up(self, key):
        key = key.lower()
        if not key in self.__down: self.__broken = True
        if self.__broken: return

        if not key in valid_keys:
            raise ValueError(f'"{key}" is not a valid key!')

        self.__down.remove(key)