import urllib.request
import checks

def lines(url: str):
    content = urllib.request.urlopen(url).read()
    lines = [l.decode() for l in content.splitlines()]
    return lines

def spl(s: str):
    l = s.rindex(":")
    return (s[0:l], s[l+1:len(s)])

def proxies(url: str):
    ls = [spl(p) for p in lines(url)]

    pr = []
    for a, p in ls:
        pr.append((a, p))
        pass

    return pr

def proxy(url: str):
    pr = proxies(url)
    for p in pr:
        if checks.check(p[0], int(p[1])):
            return p
        pass
    return None

if __name__ == "__main__":
    p = proxy("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt")
    print("%s %s" % (p[0], p[1]))
