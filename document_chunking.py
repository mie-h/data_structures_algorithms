def sol(chunks):
    res = [0]
    actual_chunks = set()

    for c0, c1 in chunks:
        # assume no overlap
        size = c1 - c0 + 1
        rm = []
        add = True
        addl, addr = c0, c1
        for (l, r) in actual_chunks:
            # current chunk is fully inside prev chunk
            # l    r
            #  c0c1
            if l <= c0 and r >= c1:
                size = 0
                add = False
                break

            # previous chunk fully inside current chunk
            #   lr
            # c0  c1
            elif c0 <= l and c1 >= r:
                size -= r - l + 1
                rm.append((l, r))

            # current chunk overlaps with prev left
            #   l    r
            # c0  c1
            elif c0 < l and c1 >= l and c1 < r:
                size -= c1 - l + 1
                rm.append((l, r))
                addr = r

            # current chunk overlaps with prev right
            #   l    r
            #      c0  c1
            elif c0 > l and c0 <= r and c1 > r:
                size -= r - c0 + 1
                rm.append((l, r))
                addl = l

        for rl, rr in rm:
            actual_chunks.remove((rl, rr))
        if add:
            actual_chunks.add((addl, addr))

        res.append(res[-1]+size)

    res.pop(0)
    return res
chunks = [[242319992485,888494425039],[890253050257,893986666716],[888022315788,983197327824],[375477269778,544174442651],[372646369775,471869607388],[104710990462,767613232623],[885899371431,984870237450],[590383734375,800503393032],[605928833001,947931236759],[948695791408,988903707680],[773919986477,782808658175],[251948207514,573096090660],[90130840141,347207472243],[111095701427,417671009162],[697732084372,898883057010]]
print(sol(chunks))


output:
[
  646174432555,
  649908049015,
  740877335340,
  740877335340,
  740877335340,
  878486337363,
  880159246989,
  880159246989,
  880159246989,
  884192717219,
  884192717219,
  884192717219,
  898772867540,
  898772867540,
  898772867540
]
