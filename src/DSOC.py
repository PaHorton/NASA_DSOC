class Trellis():
    def __init__(self,edges):
        self.edges = edges
        self.length = len(edges)
    def query(self,check):
        return [self.edges[i] for i in range(self.length)
                if all(check[j] == self.edges[i][j] for j in check)]
    def get_edge_schema(self):
        return {"initial":  len(self.edges[0]["initial"]),
                "terminal": len(self.edges[0]["terminal"]),
                "input":    len(self.edges[0]["input"]),
                "output":   len(self.edges[0]["output"])}

def gen_inner(m):
    trel = []
    logm = int(np.log2(m))
    for inp in range(m):
        A = ([int(j) for j in format(inp,'#0'+str(logm + 2) + 'b')[2:]])
        for si in range(2):
            PPM = si
            for i in range(len(A)):
                PPM = 2*PPM*(int(i%logm != 0)) + (PPM & 1 ^ A[i])
                if i%logm == (logm - 1):
                    trel.append(
                        {"initial":tuple([si]),
                         "terminal":tuple([PPM&1]),
                         "input":tuple(A),
                         "output":tuple([int(j == PPM) for j in range(m)])
                        })
                    PPM = PPM & 1
    return trel

# Rate is currently not implemented
def gen_outer(rate):
    trel = []
    for si in [[i,j] for i in range(2) for j in range(2)]:
        out = [None,None]
        for inp in range(2):
            out[0] = inp ^ si[0]
            out[1] = inp ^ si[0] ^ si[1]
            trel.append({"initial":tuple(si),
                         "terminal":tuple([inp,si[0]]),
                         "input":tuple([inp]),
                         "output":tuple(out)})
    return trel
