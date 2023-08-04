def findMinArrowShots(points):
    if not points:
        return 0

    # Sort balloons based on their ending points
    points.sort(key=lambda x: x[1])

    # Initialize the count of arrows and the current end point
    arrows = 1
    end = points[0][1]

    # Iterate through the balloons and shoot arrows
    for i in range(1, len(points)):
        if points[i][0] > end:
            # Balloon's start point is after the current end point
            # Need to shoot another arrow
            arrows += 1
            end = points[i][1]
    
    return arrows