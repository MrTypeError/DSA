# 383. Ransom Note


def RansomNote(ransomNote,magazine):
    for c in ransomNote:
        if c not in magazine:
            return False
        magazine = magazine.replace(c, '', 1)
    return True



print(RansomNote("ababa" , "aabaaba"))