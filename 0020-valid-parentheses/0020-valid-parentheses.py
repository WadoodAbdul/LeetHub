class Solution:
    def isValid(self, s: str) -> bool:
        o = set(["(", "{", "["])
        c = set([")", "}", "]"])
        oc = {"{":"}", "(":")", "[":"]", "a":"a"}
        p = []
        for b in s:
            if b in o:
                p.append(b)
            elif b in c:
                d = p.pop() if p else "a"
                if b != oc[d]:
                    return False
        return p == []
        