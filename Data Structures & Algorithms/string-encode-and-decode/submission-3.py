class Solution:

    def encode(self, strs: List[str]) -> str:
        confuse = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
        string = ""
        for s in strs:
            string += confuse + s
        return string

    def decode(self, s: str) -> List[str]:
        confuse = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
        if len(s) == 0:
            return []
        s1 = s.removeprefix(confuse)
        return s1.split(confuse)


