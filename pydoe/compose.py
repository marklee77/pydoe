from itertools import cycle 

def compose(arrayspec=None, parameters=None):

    array = []
    if arrayspec.startswith('file:'): 
        arrayfile = arrayspec[5:]
        try:
            array = [[int(x) for x in r.split()] for r in open(arrayfile, 'r')]
        except IOError:
            raise SystemExit("not a valid array file: %s" % (arrayfile))
    elif arrayspec == 'full-factorial':
        col_idx = 0
        levels = []
        for pspec in parameters.values():
            pspec['col'] = col_idx
            col_idx += 1
            levels.append([[x] for x in range(len(pspec['values']))])
        # convert list of lists of levels to list of lists representing
        # combindations of levels...
        array = reduce(lambda x, y: [w+v for w in x for v in y], levels)
    else:
        # FIXME: add support for named arrays / mongo or other db...
        pass

    array_cols = list(zip(*array))
    array_avail_col_idxs = set(range(len(array_cols)))

    # FIXME: should properly handle only specifying some columns
    selection = []
    for pname, pspec in parameters.items():
        pcolidx = pspec.get('col', -1)
        if pcolidx < 0:
            # FIXME: exception if out of columns?
            pcolidx = array_avail_col_idxs.pop()
        else:
            # FIXME: exception if column not available?
            array_avail_col_idxs.discard(pcolidx)
                
        pvalues = pspec.get('values', [])
        pcol = array_cols[pcolidx]

        num_values = len(pvalues)
        num_indexes = len(set(pcol))

        if num_values > num_indexes:
            raise SystemExit("The number of parameter values exceeds the " +
                             "number of indexes available")
        
        maxidx = (num_indexes / num_values) * num_values - 1
        pvalcycle = cycle(pvalues)
        selection.append([(pname, pvalues[i % num_values]) if i <= maxidx
                         else next(pvalcycle) for i in pcol])
 
    return [dict(list(r) + [('index', i)]) for i, r in enumerate(zip(*selection))]
