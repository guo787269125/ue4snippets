#!/usr/bin/env python

from string import Template


class Delegate:

    paramSuffix = ['', '_OneParam', '_TwoParams', '_ThreeParams', '_FourParams', '_FiveParams', '_SixParams', '_SevenParams', '_EightParams']
    
    def __init__(self, kind, name, paramNames, paramTypes):
        self.kind = kind
        self.name = name
        self.paramNames = paramNames
        self.paramTypes = paramTypes

    def Generate(self):
        a =  'DECLARE_${kind}'
        b = self.paramSuffix[len(self.paramNames)]
        c = '(${name}'
        d = ''
        if len(self.paramTypes) > 0:
            d = '' if len(self.paramNames) == 0 else (''.join([', {0}, {1}'.format(str(pn), str(pt)) for pn, pt in zip(self.paramNames, self.paramTypes)]))
        else:
            d = '' if len(self.paramNames) == 0 else (''.join([', {0}'.format(str(pn)) for pn in self.paramNames]))
        e = ')'
        print(Template('%s%s%s%s%s' % (a,b,c,d,e)).substitute(kind = self.kind, name = self.name))


class DelegateGeneratorTest:

    def __init__(self, maxParams):
        self.maxParams = maxParams
    
    def TestEvents(self):
        for n in range(1, self.maxParams + 2):
            Delegate('EVENT', '$name$', ['$$arg{0}$$'.format(p) for p in range(1,n)], []).Generate()

    
    def TestDelegates(self):
        for n in range(1, self.maxParams + 2):
            Delegate('DELEGATE', '$name$', ['$$arg{0}$$'.format(p) for p in range(1,n)], []).Generate()

    
    def TestMulticastDeleates(self):
        for n in range(1, self.maxParams + 2):
            Delegate('MULTICAST_DELEGATE', '$name$', ['$$arg{0}$$'.format(p) for p in range(1,n)], []).Generate()

    
    def TestDynamicDelegates(self):
        for n in range(1, self.maxParams + 2):
            Delegate('DYNAMIC_DELEGATE', '$name$', ['$$arg{0}$$'.format(p) for p in range(1,n)], ['$$type{0}$$'.format(p) for p in range(1,n)]).Generate()

    
    def TestDynamicMulticastDelegates(self):
        for n in range(1, self.maxParams + 2):
            Delegate('DYNAMIC_MULTICAST_DELEGATE', '$name$', ['$$arg{0}$$'.format(p) for p in range(1,n)], ['$$type{0}$$'.format(p) for p in range(1,n)]).Generate()