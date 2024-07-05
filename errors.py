class EmptyDiskError(FileNotFoundError):
    """Exception raised when the source directory does not contain any Mavica images"""
    def __init__(self):
        self.message = "The drive does not contain any SONY Mavica images"
        super().__init__(self.message)

class InvalidDirection(IndexError):
    """Exception raised when the image advance direction isn't in the [-1, 1] integer range"""
    def __init__(self, *args: object) -> None:
        self.message = "Invalid direction value"
        super().__init__(*args)