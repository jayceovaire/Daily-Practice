def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3

    match average:
        case x if 90 <= x <= 100:
            return 'A'
        case x if 80 <= x < 90:
            return 'B'
        case x if 70 <= x < 80:
            return 'C'
        case x if 60 <= x < 70:
            return 'D'
        case x if 0 <= x < 60:
            return 'F'
