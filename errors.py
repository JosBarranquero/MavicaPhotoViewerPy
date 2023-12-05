class EmptyDiskError(FileNotFoundError):
    """Exception raised when the source directory does not contain any Mavica images"""
    def __init__(self):
        self.message = 'The drive does not contain any SONY Mavica images'
        super().__init__(self.message)