from components.base import Base

class LeftFilter(Base):
    LOCATOR = "//*"

    def select_option(self, option, visible=False):
        print(self.BASE_VAR)
        print(self.LOCATOR)
        print(option)
        print(visible)

