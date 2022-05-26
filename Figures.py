class Figures:
    name = 'Figures'

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class Coan(Figures):
    def __init__(self, name: str, s: float):
        self.name = name
        self.s = s

    def get_info(self):
        return self.name, self.s


class parallelepiped(Figures):
    def __init__(self, name: str, s: int):
        self.name = name
        self.s = s

    def get_info(self):
        return self.name, self.s

class cube(Figures):
      def __init__(self, name: str, s: int):
        self.name = name
        self.s = s

      def get_info(self):
        return self.name, self.s

class sphere(Figures):
        def __init__(self, name: str, s: int):
          self.name = name
          self.s = s

        def get_info(self):
          return self.name, self.s

class elipse(Figures):
          def __init__(self, name: str, s: int):
            self.name = name
            self.s = s

          def get_info(self):
            return self.name, self.s

class culindr(Figures):
            def __init__(self, name: str, s: int):
              self.name = name
              self.s = s

            def get_info(self):
              return self.name, self.s