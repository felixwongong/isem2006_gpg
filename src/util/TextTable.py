class TextTable:
    def __init__(self, colNum, xPadding):
        """TextTable

        Args:
            colNum (int): number of column in a row
            xPadding (int): number of spacing between column
        """
        self.tableContent = []
        self.zPadding = xPadding
        self.colNum = colNum
        self.heading = ''

    def __str__(self):
        """Table output as string when str(Textable)

        Returns:
            str: formatted table string with spacing, \n and \t
        """
        initStr = ''
        if self.heading:
            initStr += f'{self.heading}\n'
        for row in self.tableContent:
            rowStr = ''
            for col in row:
                rowStr += f'{col.ljust(self.zPadding)}'
            initStr += rowStr + '\n'
        return initStr + '\n'

    def AddHeading(self, content):
        """Add a underlined heading to table

        Args:
            content (str): content in the title

        Returns:
            str: formatted heading string
        """
        self.heading = content + '\n' + '-' * len(content)
        return self

    def AddRow(self, rowContent):
        """Add a row to the table with table's number of column

        Args:
            rowContent (list<any>): array of each column in this row with size = number of column

        Returns:
            TextTable: this constant of the object, return for method chaining
        """
        if len(rowContent) != self.colNum:
            print(f"Column error, column number should be: {self.colNum}")
        rowContent = [str(col) for col in rowContent]
        self.tableContent.append(rowContent)
        return self
