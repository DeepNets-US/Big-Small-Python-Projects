class Bitmap:
    """
    A class for displaying a message on a bitmap.
    """

    def __init__(self, message: str = "Start", path_to_bitmap="./world_bitmap.txt") -> None:
        """
        Initialize the Bitmap object with a message and a path to the bitmap.

        Parameters:
        - message (str): The message to be displayed on the bitmap.
        - path_to_bitmap (str): The path to the bitmap file.

        Returns:
        None
        """
        self.message = "Start" if message == "" else message
        self.path_to_bitmap = "./world_bitmap.txt" if path_to_bitmap == "" else path_to_bitmap

    def read_bitmap(self):
        """
        Read the content of the specified bitmap file.

        Returns:
        str: The content of the bitmap file.
        """
        with open(self.path_to_bitmap, encoding='utf8', mode='r') as rawBitmap:
            bitmap = rawBitmap.read()
        return bitmap

    def gen_bitmap(self):
        """
        Generate and display a bitmap with the provided message.

        Returns:
        None
        """
        step = len(self.message)
        bitmap = self.read_bitmap().splitlines()

        for line in bitmap:
            for idx, char in enumerate(line):
                if char != " ":
                    print(self.message[idx % step], end="")
                else:
                    print(char, end="")
            print()


if __name__ == "__main__":
    while True:
        # Get user input for message and bitmap path
        msg = input(
            "Enter a Message to display in Bitmap (press enter to use default): ")
        bitmap_path = input(
            "Enter the bitmap path (press enter to use default): ")

        # Create a Bitmap object and generate the bitmap
        gen = Bitmap(msg, bitmap_path)
        gen.gen_bitmap()
