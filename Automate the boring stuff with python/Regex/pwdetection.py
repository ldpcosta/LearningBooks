###
# REGEX
###

import re

def strongPassDetection(pw):
    if len(pw)<8:
        return False
    testLower = re.compile(r'[a-z]+')
    testUpper = re.compile(r'[A-Z]+')
    testDigit = re.compile(r'[0-9]+')

    if testLower.search(pw) == None or testUpper.search(pw)==None or testDigit.search(pw)==None:
        return False

    return True
