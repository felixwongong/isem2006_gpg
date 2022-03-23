class TextTable:
    def __init__(self, colNum, zPadding):
        self.tableContent = []
        self.zPadding = zPadding
        self.colNum = colNum
        self.heading = ''

    def __str__(self):
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
        self.heading = content + '\n' + '-' * len(content)
        return self

    def AddRow(self, rowContent):
        if len(rowContent) != self.colNum:
            print(f"Column error, column number should be: {self.colNum}")
        rowContent = [str(col) for col in rowContent]
        self.tableContent.append(rowContent)
        return self
