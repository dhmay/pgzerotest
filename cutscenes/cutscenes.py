from abc import ABC, abstractmethod
import time

class CutScene(ABC):
    """Base class for cutscenes. All cutscenes must inherit from this class.
    """
    
    def __init__(self):
        """Initializes the cutscene.
        """

        # Whether or not the cutscene is finished.
        # Set this variable to True to stop the cutscene.
        self.finished = False
        
        # Keep track of the start time
        self.start_time = None

    def start(self) -> None:
        """Starts the cutscene.
        """
        self.start_time = time.time()

    @abstractmethod
    def update(self) -> None:
        """Updates the cutscene.
        """
        pass

    @abstractmethod
    def draw(self, screen) -> None:
        """Draws the cutscene.
        """
        pass


class CutSceneManager:
    """Manages cutscenes.
    """
    def __init__(self):
        self.running_cutscene = None

    def show_cutscene(self, cutscene: CutScene) -> None:
        """Shows a cutscene.
        """
        self.running_cutscene = cutscene
        cutscene.start()


class StupidTextCutScene(CutScene):
    def __init__(self):
        # Calls the superclass init method, to set finished to False.
        super().__init__()

    def start(self) -> None:
        super().start()
        print("Starting StupidTextCutScene")

    def update(self) -> None:
        # show the text for 5 seconds
        if time.time() - self.start_time > 5:
            self.finished = True
            print("Ending StupidTextCutScene")
            return

    def draw(self, screen) -> None:
        screen.fill((100, 0, 100))
        screen.draw.text("This is some boring text!", (60, 100),
                         color="red", fontsize=60)
        screen.draw.text("It obv needs more farts.", (60, 200),
                         color="red", fontsize=60)
        screen.draw.text("Natalie or Elena should really", (60, 300),
                         color="orange", fontsize=60)
        screen.draw.text("get off their butt and change it!", (60, 400),
                         color="yellow", fontsize=60)