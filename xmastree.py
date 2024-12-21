def create_postcard():
    width, height = 50, 30
    postcard = []

    for y in range(height):
        if y == 0 or y == height - 1:  # Top and Bottom Borders
            postcard.append("-" * width)
        else:
            postcard.append("|" + " " * (width - 2) + "|")

    # Add 'Merry Xmas' to line 27
    merry_xmas_line = 27
    message = "Merry Xmas"
    message_start = (width - len(message)) // 2
    postcard[merry_xmas_line] = (
            postcard[merry_xmas_line][:message_start] +
            message +
            postcard[merry_xmas_line][message_start + len(message):]
    )

    return postcard


def print_postcard(postcard):
    for line in postcard:
        print(line)


def draw_tree(treeHeight, decorationInterval, postcard=None, start_line=0, start_column=0):
    """
    Draws a Christmas tree standalone or on a postcard.

    Args:
        treeHeight (int): Height of the tree.
        decorationInterval (int): Interval for decorations.
        postcard (list of str, optional): Postcard to draw the tree on. If None, a standalone tree is drawn.
        start_line (int, optional): Starting line (Y-axis). Needed if using a postcard.
        start_column (int, optional): Starting column (X-axis).

    Returns:
        list of str: The updated postcard if provided, otherwise prints a standalone tree.
    """
    # Handle decorations and basic tree drawing
    maxWidth = 2 * (treeHeight - 1) + 1  # Total width of the tree base
    decorationsPrinted = 0

    if postcard:  # If drawing on a postcard
        mutable_postcard = [list(line) for line in postcard]

        for y in range(treeHeight + 2):  # Includes tree above and trunk
            rowWidth = y * 2 - 1 if y > 0 else 1
            rowStart = (maxWidth - rowWidth) // 2
            rowEnd = maxWidth - rowStart - 1
            center = maxWidth // 2
            firstStilt = center - 1
            secondStilt = center + 1

            for x in range(maxWidth):
                current_row = start_line + y  # Map tree row to postcard row
                current_column = start_column + x - (maxWidth // 2)  # Map to postcard column

                # Skip positions outside the postcard bounds
                if current_row < 0 or current_row >= len(mutable_postcard):
                    continue
                if current_column < 0 or current_column >= len(mutable_postcard[0]):
                    continue

                # Top of the tree: star "X"
                if y == 0:
                    if x == center:
                        mutable_postcard[current_row][current_column] = "X"

                # First row under the star has "^"
                elif y == 1:
                    if x == rowStart or x == rowEnd:
                        mutable_postcard[current_row][current_column] = "^"

                # Branch edges ("/" and "\")
                elif y > 1 and (x == rowStart or x == rowEnd):
                    if x == rowStart:
                        mutable_postcard[current_row][current_column] = "/"
                    elif x == rowEnd:
                        mutable_postcard[current_row][current_column] = "\\"

                # Trunk
                elif y == treeHeight + 1:
                    if x == firstStilt or x == secondStilt:
                        mutable_postcard[current_row][current_column] = "|"

                # Tree decorations
                elif rowStart < x < rowEnd:
                    if (x - rowStart) % 2 == 0:
                        if decorationsPrinted % decorationInterval == 0:
                            mutable_postcard[current_row][current_column] = "O"
                        else:
                            mutable_postcard[current_row][current_column] = "*"
                        decorationsPrinted += 1
                    else:
                        mutable_postcard[current_row][current_column] = "*"

        return ["".join(line) for line in mutable_postcard]

    else:  # Standalone tree rendering (no postcard)
        for y in range(treeHeight + 2):
            rowWidth = y * 2 - 1 if y > 0 else 1
            rowStart = (maxWidth - rowWidth) // 2
            rowEnd = maxWidth - rowStart - 1
            center = maxWidth // 2
            firstStilt = center - 1
            secondStilt = center + 1

            line = []  # Row of the tree
            for x in range(maxWidth):
                # Top of the tree
                if y == 0:
                    if x == center:
                        line.append("X")
                    else:
                        line.append(" ")

                # First row under the star has "^"
                elif y == 1:
                    if x == rowStart or x == rowEnd:
                        line.append("^")
                    else:
                        line.append(" ")

                # Branch edges ("/" and "\")
                elif y > 1 and (x == rowStart or x == rowEnd):
                    if x == rowStart:
                        line.append("/")
                    elif x == rowEnd:
                        line.append("\\")

                # Trunk
                elif y == treeHeight + 1:
                    if x == firstStilt or x == secondStilt:
                        line.append("|")
                    else:
                        line.append(" ")

                # Tree decorations
                elif rowStart < x < rowEnd:
                    if (x - rowStart) % 2 == 0:
                        if decorationsPrinted % decorationInterval == 0:
                            line.append("O")
                        else:
                            line.append("*")
                        decorationsPrinted += 1
                    else:
                        line.append("*")

                else:
                    line.append(" ")

            print("".join(line))  # Print each row directly


def handle_input(input_data):
    numbers = list(map(int, input_data.split()))

    if len(numbers) == 2:  # Only treeHeight and decorationInterval
        treeHeight, decorationInterval = numbers
        draw_tree(treeHeight, decorationInterval)

    elif len(numbers) % 4 == 0:  # Multiples of four (trees on postcard)
        postcard = create_postcard()
        for i in range(0, len(numbers), 4):
            treeHeight = numbers[i]
            decorationInterval = numbers[i + 1]
            start_line = numbers[i + 2]
            start_column = numbers[i + 3]
            postcard = draw_tree(treeHeight, decorationInterval, postcard, start_line, start_column)
        print_postcard(postcard)

    else:
        print("Invalid input!")


# Example usage:
input_data = input()
handle_input(input_data)
